# アーティストマスタ定義
from sqlalchemy import Column, String, Boolean, DateTime
from datetime import datetime, timezone
from db.session import Base
from sqlalchemy.orm import relationship
from sqlalchemy import text
from lib.db_constants import SCHEMA_NAME


class M_Artist(Base):
    # スキーマ名
    __table_args__ = {"schema": SCHEMA_NAME}
    # テーブル名
    __tablename__ = "m_artist"

    # カラム定義
    artist_id = Column(String(22), primary_key=True)
    artist_name = Column(String(200), nullable=False)
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

    # リレーション設定
    tune = relationship("M_Tune", back_populates="artist")
