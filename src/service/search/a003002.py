from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from schema.search import a003002 as a003002_schema
from lib.api_constants import RESPONSE_CODE
from src.utils.db_utils import error_response

# envファイル読み込み
load_dotenv()

# 認証用設定
client_credentials_manager = SpotifyClientCredentials()

# Spotifyクライアントを生成
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# A003002_楽曲取得API Service
def a003002(req: a003002_schema) -> dict:
    try:
        # リクエストに合致する楽曲情報を取得する
        result = sp.search(q=getQuery(req), type="track")
        item = result.get("tracks", {}).get("items", [])

        # データなし
        if not item:
            return {
                "success_flg": True,
                "code": RESPONSE_CODE.NOT_FOUND,
                "message": "楽曲情報が取得できませんでした。",
                "response_info": None,
            }

        # レスポンスを形成
        tune_list = []
        for tune in item:
            tune_list.append(
                {
                    "artist_id": tune["artists"][0]["id"],
                    "artist_name": tune["artists"][0]["name"],
                    "tune_id": tune["id"],
                    "tune_name": tune["name"],
                    "popularity": tune["popularity"],
                    "release_date": tune["album"]["release_date"],
                    "image": tune["album"]["images"],
                    "external_url": tune["external_urls"]["spotify"],
                }
            )

        # 楽曲情報が取得できた場合、楽曲情報を返却
        return {
            "success_flg": True,
            "code": RESPONSE_CODE.SUCCESS,
            "message": None,
            "response_info": tune_list,
        }

    # Spotify通信エラー
    except Exception as e:
        return error_response(RESPONSE_CODE.SPOTIFY_ERROR, str(e))


# Spotifyと通信を行うためのqueryを作成
def getQuery(req: a003002_schema) -> str:
    query = []
    if req.artist_name:
        query.append(f"artist:{req.artist_name}")
    if req.tune_name:
        query.append(f"track:{req.tune_name}")
    return " ".join(query)
