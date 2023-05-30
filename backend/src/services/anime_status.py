from dao import DAOFactory


class AnimeStatusService:
    def __init__(self, daos: DAOFactory):
        self.daos = daos
