from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router


def main():
    app = FastAPI(
        title="AI Spoof Guard API",
        description="API for AI Spoof Guard plugin service",
        version="0.0.0",
    )
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
