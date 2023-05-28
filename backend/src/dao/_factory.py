from sqlalchemy.ext.asyncio import AsyncSession

from .user import UserDAO
from .session import SessionDAO


class DAOFactory:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @property
    def user_dao(self) -> UserDAO:
        return UserDAO(self.session)

    @property
    def session_dao(self) -> SessionDAO:
        return SessionDAO(self.session)
