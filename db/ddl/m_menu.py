# メニューマスタ定義
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text
from datetime import datetime, timezone
from db.session import Base
from sqlalchemy import text
from lib.db_constants import SCHEMA_NAME


class M_Menu(Base):
    # スキーマ名
    __table_args__ = {"schema": SCHEMA_NAME}
    # テーブル名
    __tablename__ = "m_menu"

    # カラム定義
    sort = Column(Integer, primary_key=True)
    label = Column(String(10), nullable=False)
    icon = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    administrator_flg = Column(Boolean, nullable=False)
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
