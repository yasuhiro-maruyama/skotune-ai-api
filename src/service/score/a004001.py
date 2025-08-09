from sqlalchemy.exc import SQLAlchemyError
from lib.api_constants import RESPONSE_CODE
from lib.message import DB_MSG
from utils.utils import success_response, error_response
from db.ddl.m_artist import M_Artist
from db.ddl.m_tune import M_Tune
from db.ddl.t_score import T_Score
from db.session import SessionLocal
from schema.score import a004001 as a004001_schema


# A004001_採点履歴登録API Service
def a004001(req: a004001_schema) -> dict:
    try:
        with SessionLocal() as db:
            # アーティストが存在しない場合、アーティスト情報を登録
            row = db.query(M_Artist).filter(M_Artist.artist_id == req.artist_id).first()
            if not row:
                artist = M_Artist(
                    artist_id=req.artist_id,
                    artist_name=req.artist_name,
                )
                db.add(artist)

            # 楽曲が存在しない場合、楽曲情報を登録
            row = db.query(M_Tune).filter(M_Tune.tune_id == req.tune_id).first()
            if not row:
                tune = M_Tune(
                    tune_id=req.tune_id,
                    artist_id=req.artist_id,
                    tune_name=req.tune_name,
                )
                db.add(tune)

            # 採点結果を登録
            score = T_Score(
                user_id=req.user_id,
                tune_id=req.tune_id,
                model_type=req.model_type,
                score=req.score,
                scoring_date=req.scoring_date,
            )
            db.add(score)

            # コミット
            db.commit()

            # 正常終了
            return success_response(None)

    # DB接続エラー
    except SQLAlchemyError:
        db.rollback()
        return error_response(RESPONSE_CODE.DB_ERROR, DB_MSG.DB_ERROR)

    # 予期せぬエラー
    except Exception:
        db.rollback()
        return error_response(RESPONSE_CODE.UNKNOWN_ERROR, DB_MSG.UNKNOWN_ERROR)
