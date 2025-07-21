# マイリスト機能 Router
from fastapi import APIRouter
from schema.mylist import a006001 as a006001_schema
from src.service.mylist import a006001 as a006001_service

router = APIRouter()


# A006001_Spotifyプレイリスト取得API
@router.post("/spotify")
def artist(req: a006001_schema):
    return a006001_service.a006001(req)
