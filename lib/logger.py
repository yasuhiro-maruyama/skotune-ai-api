import logging
import time
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("api_logger")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class Logging(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        log_message = f"Request: {request.method} {request.url} "

        if request.method == "GET":
            log_message += f"request={dict(request.query_params)}"
        else:
            body = await request.body()
            log_message += f"request={body.decode('utf-8', errors='replace')}"
            request = Request(
                request.scope, receive=lambda: {"type": "http.request", "body": body}
            )

        # リクエストログ出力
        logger.info(log_message)

        try:
            response = await call_next(request)
            resp_body = b""
            async for chunk in response.body_iterator:
                resp_body += chunk
            # レスポンス再構築（読み取り後の再利用のため）
            response = Response(
                content=resp_body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type,
            )
        except Exception as e:
            # 例外発生時のログ
            logger.error(f"Exception: {e}", exc_info=True)
            raise

        process_time = (time.time() - start_time) * 1000

        # レスポンスログ出力
        logger.info(
            f"Response: status_code={response.status_code} response={resp_body.decode('utf-8', errors='replace')} duration={process_time:.2f}ms"
        )

        return response
