from fastapi import FastAPI
from src.api.v1 import spotify

# FestAPI起動
app = FastAPI()

app.include_router(spotify.router, prefix="/api/v1/spotify")
