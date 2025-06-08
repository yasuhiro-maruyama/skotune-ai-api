# 共通関数(DB用)
from pathlib import Path
from lib.api_constants import RESPONSE_CODE


# SQLファイル読み込み
def load_sql(query_type: str, filename: str) -> str:
    base_dir = Path(__file__).resolve().parents[2]
    sql_path = base_dir / "src" / "sql" / query_type / filename
    if not sql_path.exists():
        raise FileNotFoundError(f"SQLファイルが見つかりません: {sql_path}")
    return sql_path.read_text(encoding="utf-8")


# 異常系レスポンス
def error_response(code: str, message: str):
    return {
        "success_flg": False,
        "code": code,
        "message": message,
    }
