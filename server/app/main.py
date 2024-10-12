from fastapi import FastAPI

from .api.main import router


def main():
    app = FastAPI()
    app.include_router(router)

    return app
