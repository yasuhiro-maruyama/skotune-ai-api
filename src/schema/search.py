# 検索機能 Schema
from pydantic import BaseModel, Field, model_validator


# A003001_歌手取得API
class a003001(BaseModel):
    artist_name: str = Field(..., min_length=1, max_length=200, description="歌手名")


# A003002_楽曲取得API
class a003002(BaseModel):
    artist_name: str | None = Field(default=None, max_length=200, description="歌手名")
    tune_name: str | None = Field(default=None, max_length=200, description="楽曲名")

    @model_validator(mode="after")
    def condition_required(cls, values):
        if not values.artist_name and not values.tune_name:
            raise ValueError("歌手名または楽曲名のどちらかは必須です。")
        return values


# A003003_全楽曲取得API
class a003003(BaseModel):
    artist_id: str = Field(
        ...,
        min_length=22,
        max_length=22,
        pattern=r"^[A-Za-z0-9]+$",
        description="歌手ID",
    )
