from dao import DAOFactory
from .user import UserService
from .session import SessionService


class ServicesFactory:
    def __init__(self, daos: DAOFactory) -> None:
        self.daos = daos

    @property
    def user_service(self) -> UserService:
        return UserService(self.daos)

    @property
    def session_service(self) -> SessionService:
        return SessionService(self.daos, self)
