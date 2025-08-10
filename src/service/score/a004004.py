from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response
from db.ddl.m_user import M_User
from db.ddl.t_score import T_Score
from db.session import SessionLocal
from schema.score import a004004 as a004004_schema


# A004004_採点履歴削除API Service
def a004004(req: a004004_schema) -> dict:
    try:
        with SessionLocal() as db:
            # ユーザーが存在しない場合、異常終了
            row = (
                db.query(M_User)
                .filter(M_User.user_id == req.user_id, M_User.delete_flg == False)
                .first()
            )
            if not row:
                return error_response(
                    RESPONSE_CODE.AUTH_ERROR, "ユーザーが存在しません。"
                )

            # 採点情報を削除
            db.query(T_Score).filter(
                T_Score.user_id == req.user_id,
                T_Score.tune_id == req.tune_id,
                T_Score.model_type == req.model_type,
                T_Score.scoring_date == req.scoring_date,
            ).delete()

            # コミット
            db.commit()

            # 正常終了
            return success_response({"status": "ok"})

    # DB接続エラー
    except SQLAlchemyError:
        db.rollback()
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        db.rollback()
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
