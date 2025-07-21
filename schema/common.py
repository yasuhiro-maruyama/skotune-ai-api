# 共通機能 Schema
from pydantic import BaseModel, Field


# A000004_メニュー機能取得API
class a000004(BaseModel):
    administrator_flg: bool = Field(..., description="管理者フラグ")
