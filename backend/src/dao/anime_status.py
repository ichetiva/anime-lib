from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from models import AnimeStatus


class AnimeStatusDAO(BaseDAO[AnimeStatus]):
    def __init__(self, session: AsyncSession):
        super().__init__(AnimeStatus, session)
