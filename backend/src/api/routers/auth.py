from typing import Annotated

from fastapi import APIRouter, Depends

from schemas import ReqCreateSession, ResSession
from services import ServicesFactory
from core import get_services

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/", response_model=ResSession)
async def create_session(
    data: ReqCreateSession,
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    user = await services.user_service.authorize(data)
    session = await services.session_service.create(user)
    return {
        "status": "success",
        "data": session,
    }
