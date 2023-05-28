from dao import DAOFactory
from dto import AnimeDTO
from models import Anime


class AnimeService:
    def __init__(self, daos: DAOFactory):
        self.daos = daos

    def convert(self, anime: Anime) -> AnimeDTO:
        return AnimeDTO(
            id=anime.id,
            title=anime.title,
            type_=anime.type_,
            publishing_year=anime.publishing_year,
            poster_link=anime.poster_link,
        )

    async def get(self, id: int) -> AnimeDTO:
        anime = await self.daos.anime_dao.get(id=id)
        return self.convert(anime)
