from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from schema.search import a003001 as a003001_schema
from lib.api_constants import RESPONSE_CODE
from utils.utils import error_response

# envファイル読み込み
load_dotenv()

# 認証用設定
client_credentials_manager = SpotifyClientCredentials()

# Spotifyクライアントを生成
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# A003001_歌手取得API Service
def a003001(req: a003001_schema) -> dict:
    try:
        # リクエストに合致する歌手情報を取得する
        result = sp.search(q=req.artist_name, type="artist")
        item = result.get("artists", {}).get("items", [])

        # データなし
        if not item:
            return {
                "success_flg": True,
                "code": RESPONSE_CODE.NOT_FOUND,
                "message": "歌手情報が取得できませんでした。",
                "response_info": None,
            }

        # レスポンスを形成
        response_info = []
        for artist in item:
            response_info.append(
                {
                    "artist_id": artist["id"],
                    "artist_name": artist["name"],
                    "popularity": artist["popularity"],
                    "follower": artist["followers"]["total"],
                    "genre": artist["genres"],
                    "image": artist["images"],
                    "external_url": artist["external_urls"]["spotify"],
                }
            )

        # 歌手情報が取得できた場合、歌手情報を返却
        return {
            "success_flg": True,
            "code": RESPONSE_CODE.SUCCESS,
            "message": None,
            "response_info": response_info,
        }

    # Spotify通信エラー
    except Exception as e:
        return error_response(RESPONSE_CODE.SPOTIFY_ERROR, str(e))
