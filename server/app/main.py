from fastapi import FastAPI
import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .api import router


def main():
    app = FastAPI(
        title="AI Spoof Guard API",
        description="API for AI Spoof Guard plugin service",
        version="0.0.0",
    )
    app.include_router(router)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
        logging.error(f"{request}: {exc_str}")
        content = {'status_code': 10422, 'message': exc_str, 'data': None}
        return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    return app
