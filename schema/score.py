# 採点履歴登録機能 Schema
from pydantic import BaseModel, Field, condecimal
from typing import Annotated
from datetime import date

ScoreType = Annotated[
    condecimal(max_digits=6, decimal_places=3, ge=0, le=100),
    Field(description="点数"),
]


# A004001_採点履歴登録API
class a004001(BaseModel):
    user_id: str = Field(..., max_length=200, description="ユーザーID")
    artist_id: str = Field(
        ...,
        min_length=22,
        max_length=22,
        pattern=r"^[A-Za-z0-9]+$",
        description="歌手ID",
    )
    artist_name: str = Field(..., max_length=200, description="歌手名")
    tune_id: str = Field(
        ...,
        min_length=22,
        max_length=22,
        pattern=r"^[A-Za-z0-9]+$",
        description="楽曲ID",
    )
    tune_name: str = Field(..., max_length=200, description="楽曲名")
    model_type: str = Field(..., min_length=2, max_length=2, description="採点機種")
    score: ScoreType
    scoring_date: date = Field(..., description="採点日")
