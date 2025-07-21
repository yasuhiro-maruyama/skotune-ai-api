# 楽曲特徴量マスタ定義
from sqlalchemy import Column, String, Integer, Boolean, DateTime, Numeric, Text
from datetime import datetime, timezone
from db.session import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import text
from lib.db_constants import SCHEMA_NAME


class M_Features(Base):
    # スキーマ名
    __table_args__ = {"schema": SCHEMA_NAME}
    # テーブル名
    __tablename__ = "m_features"

    # カラム定義
    tune_id = Column(
        String(22), ForeignKey(f"{SCHEMA_NAME}.m_tune.tune_id"), primary_key=True
    )
    duration_ms = Column(Integer)
    tempo = Column(Numeric(6, 2))
    key = Column(String(10))
    chord_progression = Column(Text)
    danceability = Column(Numeric(5, 4))
    energy = Column(Numeric(5, 4))
    valence = Column(Numeric(5, 4))
    speechiness = Column(Numeric(5, 4))
    acousticness = Column(Numeric(5, 4))
    instrumentalness = Column(Numeric(5, 4))
    liveness = Column(Numeric(5, 4))
    mfcc_1 = Column(Numeric(7, 5))
    mfcc_2 = Column(Numeric(7, 5))
    mfcc_3 = Column(Numeric(7, 5))
    mfcc_4 = Column(Numeric(7, 5))
    mfcc_5 = Column(Numeric(7, 5))
    mfcc_6 = Column(Numeric(7, 5))
    mfcc_7 = Column(Numeric(7, 5))
    mfcc_8 = Column(Numeric(7, 5))
    mfcc_9 = Column(Numeric(7, 5))
    mfcc_10 = Column(Numeric(7, 5))
    mfcc_11 = Column(Numeric(7, 5))
    mfcc_12 = Column(Numeric(7, 5))
    mfcc_13 = Column(Numeric(7, 5))
    chroma_1 = Column(Numeric(7, 5))
    chroma_2 = Column(Numeric(7, 5))
    chroma_3 = Column(Numeric(7, 5))
    chroma_4 = Column(Numeric(7, 5))
    chroma_5 = Column(Numeric(7, 5))
    chroma_6 = Column(Numeric(7, 5))
    chroma_7 = Column(Numeric(7, 5))
    chroma_8 = Column(Numeric(7, 5))
    chroma_9 = Column(Numeric(7, 5))
    chroma_10 = Column(Numeric(7, 5))
    chroma_11 = Column(Numeric(7, 5))
    chroma_12 = Column(Numeric(7, 5))
    rms = Column(Numeric(6, 5))
    zero_crossing_rate = Column(Numeric(6, 5))
    beat_strength = Column(Numeric(6, 5))
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
    tune = relationship("M_Tune", back_populates="features")
