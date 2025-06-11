# 認証機能 Router
from fastapi import APIRouter
from src.service.ap001 import ap001 as ap001_service
from src.schema.ap001 import ap001 as ap001_schema

router = APIRouter()


# ログイン照会
@router.post("/login")
def login(req: ap001_schema):
    return ap001_service.ap001(req)
