from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router as api_router


def create_app() -> FastAPI:
    app_ = FastAPI()

    app_.include_router(api_router)

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app_
