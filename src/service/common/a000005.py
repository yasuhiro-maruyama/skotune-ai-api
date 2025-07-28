from sqlalchemy.exc import SQLAlchemyError
from db.session import SessionLocal
from schema.common import a000005 as a000005_schema
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response
from db.ddl.m_code import M_Code


# A000005_コード値取得API Service
def a000005(req: a000005_schema) -> dict:
    try:
        with SessionLocal() as db:
            # コードマスタからデータ取得
            query = (
                db.query(
                    M_Code.code_id,
                    M_Code.code_value,
                    M_Code.code_name,
                )
                .filter(M_Code.delete_flg == False)
                .order_by(M_Code.code_value)
            )

            # コードIDが存在する場合、一致する情報のみ返却
            if req.code_id:
                row = query.filter(M_Code.code_id == req.code_id).all()
            # リクエストがない場合、全件取得
            else:
                row = query.all()

            # データなし
            if not row:
                return error_response(
                    RESPONSE_CODE.NOT_FOUND, "コード情報が取得できませんでした。"
                )

            # 取得した情報から不要な項目を除外してコード情報を設定
            code_info = [
                {
                    "code_value": r.code_value,
                    "code_name": r.code_name,
                }
                for r in row
            ]

            # 取得できた場合、コード情報を返却
            return success_response(code_info)

    # ファイル取り込みエラー
    except FileNotFoundError as e:
        return error_response(RESPONSE_CODE.FILE_IMPORT_ERROR, str(e))

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
