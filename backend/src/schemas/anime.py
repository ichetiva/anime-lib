from .base import BaseResponse

from dto import AnimeDTO


class ResAnime(BaseResponse):
    data: AnimeDTO | None = None


class ResAnimeList(BaseResponse):
    data: list[AnimeDTO] = []
