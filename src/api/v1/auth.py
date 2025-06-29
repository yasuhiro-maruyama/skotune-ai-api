# 認証機能 Router
from fastapi import APIRouter
from schema.auth import a001001 as a001001_schema
from schema.auth import a001002 as a001002_schema
from src.service.auth import a001001 as a001001_service
from src.service.auth import a001002 as a001002_service

router = APIRouter()


# A001001_ログイン照会API
@router.post("/login")
def login(req: a001001_schema):
    return a001001_service.a001001(req)


# A001002_メニュー機能取得API
@router.post("/menu")
def menu(req: a001002_schema):
    return a001002_service.a001002(req)
