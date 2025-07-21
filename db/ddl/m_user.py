# ユーザーマスタ定義
from sqlalchemy import Column, String, Boolean, DateTime, text
from datetime import datetime, timezone
from db.session import Base
from lib.db_constants import SCHEMA_NAME


class M_User(Base):
    # スキーマ名
    __table_args__ = {"schema": SCHEMA_NAME}
    # テーブル名
    __tablename__ = "m_user"

    # カラム定義
    user_id = Column(String(200), primary_key=True)
    user_name = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    administrator_flg = Column(Boolean, nullable=False)
    spotify_token = Column(String(200))
    insert_date = Column(
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )
    update_date = Column(
        DateTime(timezone=True),
        default=None,
        onupdate=lambda: datetime.now(timezone.utc),
    )
    delete_flg = Column(Boolean, nullable=False, server_default=text("false"))
