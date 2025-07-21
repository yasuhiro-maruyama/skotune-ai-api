# 楽曲レコメンド機能 Schema
from pydantic import BaseModel, Field


# A005001_点数推測モデル生成API
class a005001(BaseModel):
    user_id: str = Field(..., min_length=1, max_length=200, description="ユーザーID")
