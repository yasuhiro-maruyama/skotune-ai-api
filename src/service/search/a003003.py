from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from schema.search import a003003 as a003003_schema
from lib.api_constants import RESPONSE_CODE
from src.utils.db_utils import error_response

# envファイル読み込み
load_dotenv()

# 認証用設定
client_credentials_manager = SpotifyClientCredentials()

# Spotifyクライアントを生成
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 最大50件
OFFSET = 50


# A003003_全楽曲取得API Service
def a003003(req: a003003_schema) -> dict:
    response_info = []
    deduplication_tune = set()
    offset = 0
    try:
        while True:
            # リクエストに合致する歌手のアルバム/シングル情報を50件ずつ取得する
            # ※ Spotifyでは、最大50件ずつまでしか取得できない
            result = sp.artist_albums(
                req.artist_id, album_type="album,single", limit=OFFSET, offset=offset
            )
            item = result.get("items", [])

            # データが存在しない場合、処理を抜ける
            if not item:
                break

            # アルバムの件数分、ループ処理
            for album in item:
                # アルバムIDを設定し、アルバムのトラックを取得する
                album_id = album["id"]
                tracks = sp.album_tracks(album_id).get("items", [])

                # トラックの件数分、ループ処理
                for track in tracks:
                    tune_id = track["id"]
                    # トラックIDが重複しない場合、その楽曲をレスポンス情報に追加する
                    if tune_id not in deduplication_tune:
                        response_info.append(
                            {
                                "artist_id": track["artists"][0]["id"],
                                "artist_name": track["artists"][0]["name"],
                                "tune_id": tune_id,
                                "tune_name": track["name"],
                                "release_date": album["release_date"],
                                "image": album["images"],
                                "external_url": track["external_urls"]["spotify"],
                            }
                        )
                        deduplication_tune.add(tune_id)

            # 次のページに楽曲が存在しない場合、処理を抜ける
            if result.get("next") is None:
                break

            # 次ページの50件分を確認
            offset += OFFSET

        # データなし
        if not response_info:
            return {
                "success_flg": True,
                "code": RESPONSE_CODE.NOT_FOUND,
                "message": "楽曲情報が取得できませんでした。",
                "response_info": None,
            }

        # リリース日の降順にソートする
        response_info.sort(key=lambda x: x["release_date"], reverse=True)

        # 楽曲情報が取得できた場合、楽曲情報を返却
        return {
            "success_flg": True,
            "code": RESPONSE_CODE.SUCCESS,
            "message": None,
            "response_info": response_info,
        }

    # Spotify通信エラー
    except Exception as e:
        return error_response(RESPONSE_CODE.SPOTIFY_ERROR, str(e))
