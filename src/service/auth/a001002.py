from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from db.session import SessionLocal
from utils.utils import load_sql
from schema.auth import a001002 as a001002_schema
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import error_response


# A001002_メニュー機能取得API Service
def a001002(req: a001002_schema) -> dict:
    try:
        with SessionLocal() as db:
            sql = text(load_sql("auth", "select_menu.sql"))
            result = db.execute(sql, {"admin": req.administrator_flg})
            row = result.mappings().all()

            # データなし
            if row is None:
                return {
                    "success_flg": False,
                    "code": RESPONSE_CODE.NOT_FOUND,
                    "message": "メニュー情報が取得できませんでした。",
                    "response_info": None,
                }

            # 取得できた場合、メニュー情報を返却
            return {
                "success_flg": True,
                "code": RESPONSE_CODE.SUCCESS,
                "message": None,
                "response_info": [dict(r) for r in row],
            }

    # ファイル取り込みエラー
    except FileNotFoundError as e:
        return error_response(RESPONSE_CODE.FILE_IMPORT_ERROR, str(e))

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
