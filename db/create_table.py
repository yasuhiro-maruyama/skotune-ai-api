# テーブル作成
from db.session import engine, Base
from db.ddl import m_user
from db.ddl import m_menu
from db.ddl import m_artist
from db.ddl import m_tune
from db.ddl import m_features

Base.metadata.create_all(bind=engine)
