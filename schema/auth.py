# 認証機能 Schema
from pydantic import BaseModel, Field


# A001001_ログイン照会API
class a001001(BaseModel):
    user_id: str = Field(..., max_length=200, description="ユーザーID")
    password: str = Field(..., min_length=8, max_length=32, description="パスワード")


# # A001003_Spotify認証API
# class a001003(BaseModel):
#     artist_name: str = Field(..., min_length=1, max_length=200, description="歌手名")
