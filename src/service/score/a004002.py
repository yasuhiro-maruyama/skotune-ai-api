from sqlalchemy.exc import SQLAlchemyError
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response
from db.ddl.m_user import M_User
from db.ddl.m_artist import M_Artist
from db.ddl.m_tune import M_Tune
from db.ddl.t_score import T_Score
from db.session import SessionLocal
from schema.score import a004002 as a004002_schema

# 採点機種マッピング
MODEL_TYPE_MAP = {"00": "joysound", "01": "joysound_ai", "10": "dam", "11": "dam_ai"}


# A004002_採点履歴検索API Service
def a004002(req: a004002_schema) -> dict:
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

            # ユーザーの期間内の採点情報を取得
            query = (
                db.query(
                    T_Score.user_id,
                    M_Tune.artist_id,
                    M_Artist.artist_name,
                    M_Tune.tune_id,
                    M_Tune.tune_name,
                    T_Score.model_type,
                    T_Score.score,
                    T_Score.scoring_date,
                )
                .join(M_Tune, T_Score.tune_id == M_Tune.tune_id)
                .join(M_Artist, M_Tune.artist_id == M_Artist.artist_id)
                .filter(T_Score.user_id == req.user_id, T_Score.delete_flg == False)
            )

            # 開始日が設定されている場合
            if req.from_date is not None:
                query = query.filter(T_Score.scoring_date >= req.from_date)

            # 終了日が指定されている場合
            if req.to_date is not None:
                query = query.filter(T_Score.scoring_date <= req.to_date)

            # ソート実行
            result = query.order_by(
                T_Score.scoring_date, T_Score.score, T_Score.model_type
            ).all()

            # マッピング情報をもとに、各採点機種の配列を作成する
            grouped = {v: [] for v in MODEL_TYPE_MAP.values()}
            for row in result:
                grouped[MODEL_TYPE_MAP.get(row.model_type)].append(
                    {
                        "user_id": row.user_id,
                        "artist_id": row.artist_id,
                        "artist_name": row.artist_name,
                        "tune_id": row.tune_id,
                        "tune_name": row.tune_name,
                        "score": row.score,
                        "scoring_date": row.scoring_date,
                    }
                )

            # 正常終了
            return success_response(grouped)

    # DB接続エラー
    except SQLAlchemyError:
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
