from dao import DAOFactory
from .user import UserService


class ServicesFactory:
    def __init__(self, daos: DAOFactory) -> None:
        self.daos = daos

    @property
    def user_service(self) -> UserService:
        return UserService(self.daos)
