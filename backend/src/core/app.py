from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api import router as api_router
from exceptions.handlers import http_exception_handler


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

    app_.add_exception_handler(HTTPException, http_exception_handler)

    return app_
