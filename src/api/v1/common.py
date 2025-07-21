# 共通機能 Router
from fastapi import APIRouter

from src.service.common import a000001 as a000001_service
from src.service.common import a000002 as a000002_service

router = APIRouter()


# A000001_ヘルスチェックAPI
@router.post("/health")
def a000001():
    return a000001_service.a000001()


# A000002_テーブル作成API
@router.post("/table/create")
def a000002():
    return a000002_service.a000002()
