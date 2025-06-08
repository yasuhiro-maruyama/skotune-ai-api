# テーブル作成
from src.db.session import engine, Base
from src.model import user

Base.metadata.create_all(bind=engine)
