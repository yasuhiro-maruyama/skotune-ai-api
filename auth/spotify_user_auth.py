# 未使用

# Spotifyユーザー認証(トークン取得)
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# envファイル読み込み
load_dotenv()

# 認証用設定
sp_oauth = SpotifyOAuth(scope="user-read-private user-read-email")

# 認証URLを取得
auth_url = sp_oauth.get_authorize_url()
print("認証URL:", auth_url)

# 上のURLにアクセスして許可 → リダイレクト先にコードが付与されて返却
# その返却値を使ってSpotifyのトークンを取得
redirect_response = input("リダイレクトされたURLを貼り付けてください：\n")

# キャッシュ保存
code = sp_oauth.parse_response_code(redirect_response)
token_info = sp_oauth.get_access_token(code)

# Spotifyクライアントを生成
sp = spotipy.Spotify(auth=token_info["access_token"])
