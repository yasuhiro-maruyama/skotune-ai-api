# 共通機能 Router
from fastapi import APIRouter

from schema.common import a000004 as a000004_schema

from src.service.common import a000001 as a000001_service
from src.service.common import a000002 as a000002_service
from src.service.common import a000004 as a000004_service

router = APIRouter()


# A000001_ヘルスチェックAPI
@router.get("/health")
def a000001():
    return a000001_service.a000001()


# A000002_テーブル作成API
@router.post("/table/create")
def a000002():
    return a000002_service.a000002()


# A000004_メニュー機能取得API
@router.post("/menu")
def a000004(req: a000004_schema):
    return a000004_service.a000004(req)
