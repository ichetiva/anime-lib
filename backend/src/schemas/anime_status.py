from pydantic import BaseModel

from .base import BaseResponse
from dto import AnimeStatusDTO


class ReqSetAnimeStatus(BaseModel):
    anime_id: int
    status: str


class ResAnimeStatus(BaseResponse):
    data: AnimeStatusDTO | None = None


class ResAnimeStatuses(BaseResponse):
    data: list[AnimeStatusDTO] = []
