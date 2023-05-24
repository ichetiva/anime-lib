from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .db import async_session
from dao import DAOFactory
from services import ServicesFactory


async def get_session():
    async with async_session() as session:
        try:
            yield session
        except:
            await session.rollback()


async def get_services(session: AsyncSession = Depends(get_session)):
    daos = DAOFactory(session)
    services = ServicesFactory(daos)
    return services
