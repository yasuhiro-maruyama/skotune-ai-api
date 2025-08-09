# テーブル作成
from db.session import engine, Base
from db.ddl import m_code
from db.ddl import m_user
from db.ddl import m_menu
from db.ddl import m_artist
from db.ddl import m_tune
from db.ddl import m_features
from db.ddl import t_score
from sqlalchemy.exc import SQLAlchemyError
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response


# A000002_テーブル作成API Service
def a000002() -> dict:
    try:
        Base.metadata.create_all(bind=engine)
        return success_response({"status": "ok"})

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
