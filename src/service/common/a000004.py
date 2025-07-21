from sqlalchemy.exc import SQLAlchemyError
from db.session import SessionLocal
from schema.common import a000004 as a000004_schema
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response
from db.ddl.m_menu import M_Menu


# A000004_メニュー機能取得API Service
def a000004(req: a000004_schema) -> dict:
    try:
        with SessionLocal() as db:
            # メニューマスタからデータ取得
            query = (
                db.query(M_Menu)
                .filter(M_Menu.delete_flg == False)
                .order_by(M_Menu.sort)
            )

            # 管理者の場合、全件取得
            if req.administrator_flg:
                row = query.all()
            # 一般ユーザーの場合、管理者権限のあるメニューは取得しない
            else:
                row = query.filter(M_Menu.administrator_flg == False).all()

            # データなし
            if not row:
                return error_response(
                    RESPONSE_CODE.NOT_FOUND, "メニュー情報が取得できませんでした。"
                )

            # 取得できた場合、メニュー情報を返却
            return success_response([dict(r) for r in row])

    # ファイル取り込みエラー
    except FileNotFoundError as e:
        return error_response(RESPONSE_CODE.FILE_IMPORT_ERROR, str(e))

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
