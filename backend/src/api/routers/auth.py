from fastapi import APIRouter, Depends

from dto import SessionDTO
from schemas import ReqCreateSession
from services import ServicesFactory
from core import get_services

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/", response_model=SessionDTO)
async def create_session(
    data: ReqCreateSession,
    services: ServicesFactory = Depends(get_services),
):
    user = await services.user_service.authorize(data)
    session = await services.session_service.create(user)
    return session
