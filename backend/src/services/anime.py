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

    def convert_multiple(self, anime_list: list[Anime]) -> list[AnimeDTO]:
        anime_list_dto = []
        for anime in anime_list:
            anime_list_dto.append(self.convert(anime))
        return anime_list_dto

    async def get(self, id: int) -> AnimeDTO:
        anime = await self.daos.anime_dao.get(id=id)
        return self.convert(anime)

    async def get_all(self) -> list[AnimeDTO]:
        anime_list = await self.daos.anime_dao.get_multiple()
        return self.convert_multiple(anime_list)
