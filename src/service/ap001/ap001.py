from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.db.session import SessionLocal
from src.utils.db_utils import load_sql
from src.schema.ap001 import ap001 as ap001_schema
from lib.api_constants import RESPONSE_CODE
from src.utils.db_utils import error_response


# ログイン照会API Service AP001
def ap001(req: ap001_schema) -> dict:
    try:
        with SessionLocal() as db:
            sql = text(load_sql("select", "user.sql"))
            result = db.execute(sql, {"user_id": req.user_id})
            row = result.mappings().first()

            # データなし
            if row is None:
                return {
                    "success_flg": True,
                    "code": RESPONSE_CODE.FILE_NOT_FOUND,
                    "message": "ユーザー情報が取得できませんでした。",
                    "user_info": None,
                }

            # 正常にユーザー情報を取得
            return {
                "success_flg": True,
                "code": RESPONSE_CODE.SUCCESS,
                "message": None,
                "user_info": dict(row),
            }

    except FileNotFoundError as e:
        return error_response(RESPONSE_CODE.FILE_IMPORT_ERROR, str(e))

    except SQLAlchemyError:
        return error_response(
            RESPONSE_CODE.DB_ERROR, "データベースエラーが発生しました。"
        )

    except Exception:
        return error_response(
            RESPONSE_CODE.UNKNOWN_ERROR, "予期しないエラーが発生しました。"
        )
