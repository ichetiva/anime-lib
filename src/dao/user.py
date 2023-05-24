from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from .base import BaseDAO
from models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def delete_by_username(self, username: str):
        stmt = delete(self.model).where(self.model.username == username)
        await self.session.execute(stmt)
        await self.session.delete()
