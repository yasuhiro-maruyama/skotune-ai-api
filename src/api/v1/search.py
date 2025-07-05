# 検索機能 Router
from fastapi import APIRouter
from schema.search import a003001 as a003001_schema
from schema.search import a003002 as a003002_schema
from schema.search import a003003 as a003003_schema
from src.service.search import a003001 as a003001_service
from src.service.search import a003002 as a003002_service
from src.service.search import a003003 as a003003_service

router = APIRouter()


# A003001_歌手取得API
@router.post("/artist")
def artist(req: a003001_schema):
    return a003001_service.a003001(req)


# A003002_楽曲取得API
@router.post("/tune")
def tune(req: a003002_schema):
    return a003002_service.a003002(req)


# A003003_歌手楽曲一覧取得API
@router.post("/artist/tune")
def artist_tune(req: a003003_schema):
    return a003003_service.a003003(req)
