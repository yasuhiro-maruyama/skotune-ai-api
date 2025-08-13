# 採点履歴登録機能 Router
from fastapi import APIRouter

from schema.score import a004001 as a004001_schema
from schema.score import a004002 as a004002_schema
from schema.score import a004003 as a004003_schema
from schema.score import a004004 as a004004_schema
from src.service.score import a004001 as a004001_service
from src.service.score import a004002 as a004002_service
from src.service.score import a004003 as a004003_service
from src.service.score import a004004 as a004004_service

router = APIRouter()


# A004001_採点履歴登録API
@router.post("/register")
def a004001(req: a004001_schema):
    return a004001_service.a004001(req)


# A004002_採点履歴検索API
@router.post("/search")
def a004002(req: a004002_schema):
    return a004002_service.a004002(req)


# A004003_採点履歴更新API
@router.post("/update")
def a004003(req: a004003_schema):
    return a004003_service.a004003(req)


# A004004_採点履歴削除API
@router.post("/delete")
def a004004(req: a004004_schema):
    return a004004_service.a004004(req)
