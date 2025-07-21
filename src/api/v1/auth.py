# 認証機能 Router
from fastapi import APIRouter

from schema.auth import a001001 as a001001_schema

# from src.schema.auth import a001004 as a001004_schema
from src.service.auth import a001001 as a001001_service

# from src.service.auth import a001004 as a001004_service

router = APIRouter()


# A001001_ログイン照会API
@router.post("/login")
def a001001(req: a001001_schema):
    return a001001_service.a001001(req)


# # A001004_Spotify認証API
# @router.post("/spotify")
# def spotify(req: a001004_schema):
#     return a001004_service.a001004(req)
