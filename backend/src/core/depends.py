from typing import Annotated, AsyncGenerator

from fastapi import Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession

from .db import async_session
from dao import DAOFactory
from dto import UserDTO
from services import ServicesFactory
from exceptions import session as session_excs


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except:
            await session.rollback()


async def get_services(session: AsyncSession = Depends(get_session)) -> ServicesFactory:
    daos = DAOFactory(session)
    services = ServicesFactory(daos)
    return services


async def get_current_user(
    authorization: Annotated[str, Header()],
    services: ServicesFactory = Depends(get_services),
) -> UserDTO | None:
    if authorization.startswith("Bearer "):
        token = authorization.replace("Bearer ", "")
        user = await services.session_service.get_user(token)
        return user
    raise session_excs.UnauthorizedError()
