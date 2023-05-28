from fastapi import FastAPI

from api import router as api_router


def create_app() -> FastAPI:
    app_ = FastAPI()

    app_.include_router(api_router)

    return app_
