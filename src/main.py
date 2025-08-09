from fastapi import FastAPI
from src.api.v1 import common
from src.api.v1 import auth
from src.api.v1 import search
from src.api.v1 import score
from src.api.v1 import model
from src.api.v1 import mylist
from lib.logger import Logging

# FestAPI起動
app = FastAPI()
app.add_middleware(Logging)

app.include_router(common.router, prefix="/api/v1/common")
app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(search.router, prefix="/api/v1/search")
app.include_router(score.router, prefix="/api/v1/score")
app.include_router(model.router, prefix="/api/v1/model")
app.include_router(mylist.router, prefix="/api/v1/mylist")
