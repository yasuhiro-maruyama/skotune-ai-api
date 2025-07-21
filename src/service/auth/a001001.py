from passlib.hash import bcrypt
from sqlalchemy.exc import SQLAlchemyError
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response
from db.ddl.m_user import M_User
from db.session import SessionLocal
from schema.auth import a001001 as a001001_schema

AUTH_ERROR_MSG = "ユーザー情報が取得できませんでした。"


# A001001_ログイン照会API Service
def a001001(req: a001001_schema) -> dict:
    try:
        with SessionLocal() as db:
            row = db.query(M_User).filter(M_User.user_id == req.user_id).first()

            # データなし
            if row is None:
                return error_response(RESPONSE_CODE.NOT_FOUND, AUTH_ERROR_MSG)

            # パスワード不一致
            if not bcrypt.verify(req.password, row.password):
                return error_response(RESPONSE_CODE.AUTH_ERROR, AUTH_ERROR_MSG)

            # 取得した情報からパスワードを除外してユーザー情報を設定
            keys_to_extract = ["user_id", "user_name", "administrator_flg"]
            user_info = {key: getattr(row, key) for key in keys_to_extract}

            # ユーザー情報が取得できた場合、ユーザー情報を返却
            return success_response(user_info)

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
