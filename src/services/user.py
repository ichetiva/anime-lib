from dao import DAOFactory


class UserService:
    def __init__(self, daos: DAOFactory) -> None:
        self.daos = daos
