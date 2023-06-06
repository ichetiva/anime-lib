from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from models import Anime


class AnimeDAO(BaseDAO[Anime]):
    def __init__(self, session: AsyncSession):
        super().__init__(Anime, session)

    async def get_by_pattern_in_title(self, pattern: str) -> list[Anime]:
        stmt = select(Anime).where(Anime.title.ilike(f"%{pattern}%"))
        anime_list = await self.session.scalars(stmt)
        return anime_list.all()
