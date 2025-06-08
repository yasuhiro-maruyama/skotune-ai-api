# ユーザー定義
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from src.db.session import Base


class User(Base):
    __table_args__ = {"schema": "skotune_ai"}
    __tablename__ = "user"

    user_id = Column(String(50), primary_key=True)
    user_name = Column(String(100), nullable=False)
    mail_address = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    administrator_flg = Column(Boolean, nullable=False)
    insert_date = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    update_date = Column(
        DateTime(timezone=True),
        default=None,
        onupdate=lambda: datetime.now(timezone.utc),
    )
    delete_flg = Column(Boolean, nullable=False)
