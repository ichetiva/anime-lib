from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from models import Anime


class AnimeDAO(BaseDAO[Anime]):
    def __init__(self, session: AsyncSession):
        super().__init__(Anime, session)
