# Spotifyパブリック認証
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# envファイル読み込み
load_dotenv()

# 認証用設定
client_credentials_manager = SpotifyClientCredentials()

# Spotifyクライアントを生成
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#
def get() -> str:
    results = sp.new_releases(country="JP", limit=5)
    for album in results["albums"]["items"]:
        return album["name"]
