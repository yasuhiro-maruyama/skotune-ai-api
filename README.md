仮想環境作成
　 python -m venv venv

有効化
　.\venv\Scripts\activate.bat

モジュールインストール

FestAPI 起動方法
　 uvicorn src.main:app --reload

Spotify 個別認証方法
　 cd ./auth
　 python spotify_user_auth.py (認証 URL から取得したリダイレクト URL を貼り付け、トークンを取得)
