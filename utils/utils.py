# 共通関数
from pathlib import Path
from lib.api_constants import RESPONSE_CODE


# SQLファイル読み込み
def load_sql(function_type: str, filename: str) -> str:
    base_dir = Path(__file__).resolve().parents[2]
    sql_path = base_dir / "src" / "db" / "sql" / function_type / filename
    if not sql_path.exists():
        raise FileNotFoundError(f"SQLファイルが見つかりません: {sql_path}")
    return sql_path.read_text(encoding="utf-8")


# 正常系レスポンス
def success_response(result):
    return {
        "success_flg": False,
        "code": RESPONSE_CODE.SUCCESS,
        "message": None,
        "response_info": result,
    }


# 異常系レスポンス
def error_response(code: str, message: str):
    return {
        "success_flg": False,
        "code": code,
        "message": message,
    }
