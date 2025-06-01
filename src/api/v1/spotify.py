from fastapi import APIRouter
from src.service.spotify import public_auth

router = APIRouter()


@router.get("/get")
def get():
    name = public_auth.get()
    return {"name": name}
