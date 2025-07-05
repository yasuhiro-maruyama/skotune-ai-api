from fastapi import FastAPI
from src.api.v1 import auth
from src.api.v1 import search
from lib.logger import Logging

# FestAPI起動
app = FastAPI()
app.add_middleware(Logging)

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(search.router, prefix="/api/v1/search")
