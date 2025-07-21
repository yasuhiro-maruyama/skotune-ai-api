# 楽曲レコメンド機能 Router
from fastapi import APIRouter
from schema.model import a005001 as a005001_schema
from src.service.model import a005001 as a005001_service

router = APIRouter()


# A005001_点数推測モデル生成API
@router.post("/score/create")
def a005001(req: a005001_schema):
    return a005001_service.a005001(req)
