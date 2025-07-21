# 共通機能 Router
from fastapi import APIRouter

from src.service.common import a000001 as a000001_service

router = APIRouter()


# A000001_ヘルスチェックAPI
@router.post("/health")
def a000001():
    return a000001_service.a000001()
