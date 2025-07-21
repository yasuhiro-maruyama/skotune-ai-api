from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.session import SessionLocal
from utils.utils import load_sql
from schema.mylist import a006001 as a006001_schema
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import error_response

sp_oauth = SpotifyOAuth(
    scope="playlist-read-private",
)

# 最大100件
OFFSET = 100


# A006001_Spotifyプレイリスト取得API Service
def a006001(req: a006001_schema) -> dict:

    try:
        with SessionLocal() as db:
            sql = text(load_sql("mylist", "select_spotify_token.sql"))
            result = db.execute(sql, {"user_id": req.user_id})
            row = result.mappings().first()

            # データなし
            if row["spotify_token"] is None:
                return {
                    "success_flg": False,
                    "code": RESPONSE_CODE.NOT_FOUND,
                    "message": "Spotifyと連携していないユーザーです。",
                    "response_info": None,
                }

            # DBから取得したリフレッシュトークンでアクセストークンを再取得
            token_info = sp_oauth.refresh_access_token(row["spotify_token"])
            access_token = token_info["access_token"]

            # Spotipyクライアントを生成
            sp = spotipy.Spotify(auth=access_token)

            #  プレイリストを取得
            playlist = sp.current_user_playlists()

            response_info = []

            # プレイリストの件数分、ループ処理
            for list in playlist["items"]:
                playlist_tracks = []
                # プレイリストの楽曲を全件取得
                tracks = get_all_playlist_track(sp, list["id"])
                for item in tracks:
                    track = item["track"]

                    playlist_tracks.append(
                        {
                            "artist_id": track["artists"][0]["id"],
                            "artist_name": track["artists"][0]["name"],
                            "tune_id": track["id"],
                            "tune_name": track["name"],
                            "release_date": track["album"]["release_date"],
                            "popularity": track.get("popularity", 0),
                            "image": track["album"]["images"],
                            "external_url": track["external_urls"]["spotify"],
                        }
                    )

                response_info.append(
                    {
                        "playlist_id": list["id"],
                        "playlist_name": list["name"],
                        "tracks": playlist_tracks,
                    }
                )

            # Spotifyプレイリスト情報を返却
            return {
                "success_flg": True,
                "code": RESPONSE_CODE.SUCCESS,
                "message": None,
                "response_info": response_info,
            }

    # ファイル取り込みエラー
    except FileNotFoundError as e:
        return error_response(RESPONSE_CODE.FILE_IMPORT_ERROR, str(e))

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)


# プレイリスト全件取得
def get_all_playlist_track(sp, playlist_id):
    all_track = []
    offset = 0

    while True:
        result = sp.playlist_items(playlist_id, offset=offset, limit=OFFSET)
        items = result.get("items", [])
        all_track.extend(items)

        # 次のページに楽曲が存在しない場合、処理を抜ける
        if result.get("next") is None:
            break

        # 次ページの100件分を確認
        offset += OFFSET

    return all_track
