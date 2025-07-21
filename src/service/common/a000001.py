from utils.utils import success_response


# A000001_ヘルスチェックAPI Service
def a000001() -> dict:
    return success_response({"status": "ok"})
