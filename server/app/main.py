from fastapi import FastAPI

from .api import router


def main():
    app = FastAPI(
        title="AI Spoof Guard API",
        description="API for AI Spoof Guard plugin service",
        version="0.0.0",
    )
    app.include_router(router)

    return app
