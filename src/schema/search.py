# 検索機能 Schema
from pydantic import BaseModel, Field


# A003001_歌手取得API
class a003001(BaseModel):
    artist_name: str = Field(..., min_length=1, max_length=200, description="歌手名")


# # A003002_楽曲取得API
# class a003002(BaseModel):
#     artist_name: str = Field(..., min_length=1, max_length=200, description="歌手名")
#     tune_name: str = Field(..., min_length=1, max_length=200, description="楽曲名")


# # A003003_歌手楽曲一覧取得API
# class a003003(BaseModel):
#     artist_id: str = Field(
#         ..., min_length=22, max_length=22, regex=r"^[A-Za-z0-9]+$", description="歌手ID"
#     )
