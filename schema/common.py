# 共通機能 Schema
from pydantic import BaseModel, Field


# A000004_メニュー機能取得API
class a000004(BaseModel):
    administrator_flg: bool = Field(..., description="管理者フラグ")


# A000005_コード値取得API
class a000005(BaseModel):
    code_id: str = Field(max_length=4, description="コードID")
