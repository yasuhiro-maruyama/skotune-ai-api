# マイリスト機能 Schema
from pydantic import BaseModel, Field, model_validator


# A006001_Spotifyプレイリスト取得API
class a006001(BaseModel):
    user_id: str = Field(..., min_length=1, max_length=100, description="ユーザーID")
