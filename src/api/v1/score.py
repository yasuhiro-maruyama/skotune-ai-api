# 採点履歴登録機能 Router
from fastapi import APIRouter

from schema.score import a004001 as a004001_schema
from src.service.score import a004001 as a004001_service

router = APIRouter()


# A004001_採点履歴登録API
@router.post("/register")
def a004001(req: a004001_schema):
    return a004001_service.a004001(req)
