# 採点テーブル定義
from sqlalchemy import Column, String, Numeric, Boolean, Date, DateTime
from datetime import datetime, timezone
from db.session import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import text
from lib.db_constants import SCHEMA_NAME


class T_Score(Base):
    # スキーマ名
    __table_args__ = {"schema": SCHEMA_NAME}
    # テーブル名
    __tablename__ = "t_score"

    # カラム定義
    user_id = Column(
        String(200), ForeignKey(f"{SCHEMA_NAME}.m_user.user_id"), primary_key=True
    )
    tune_id = Column(
        String(22), ForeignKey(f"{SCHEMA_NAME}.m_tune.tune_id"), primary_key=True
    )
    model_type = Column(String(2), primary_key=True)
    score = Column(Numeric(7, 3), nullable=False)
    scoring_date = Column(
        Date,
        server_default=text("CURRENT_DATE"),
        primary_key=True,
    )
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
    user = relationship("M_User", back_populates="score")
    tune = relationship("M_Tune", back_populates="score")
