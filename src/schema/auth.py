# 認証機能 Schema
from pydantic import BaseModel, Field


# A001001_ログイン照会API
class a001001(BaseModel):
    user_id: str = Field(..., description="ユーザーIDは必須です")
    password: str = Field(..., description="パスワードは8文字以上")


# A001002_メニュー機能取得API
class a001002(BaseModel):
    administrator_flg: bool = Field(..., description="管理者フラグは必須です。")
