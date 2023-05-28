from fastapi import APIRouter

from .routers import routers
from schemas import Healthcheck

router = APIRouter(prefix="/api")

for r in routers:
    router.include_router(r)


@router.get("/healthcheck", response_model=Healthcheck)
async def healthcheck():
    return {"message": "It works"}
