from sqlalchemy.ext.asyncio import AsyncSession

from models import Session
from .base import BaseDAO


class SessionDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Session, session)
