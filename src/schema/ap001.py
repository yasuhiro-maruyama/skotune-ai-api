# ログイン照会API Schema AP001
from pydantic import BaseModel, Field


class ap001(BaseModel):
    user_id: str = Field(..., description="ユーザーIDは必須です")
    password: str = Field(..., description="パスワードは8文字以上")
