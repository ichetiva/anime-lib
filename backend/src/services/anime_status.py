from typing import List

from dao import DAOFactory
from dto import AnimeStatusDTO
from schemas import ReqSetAnimeStatus
from models import AnimeStatus


class AnimeStatusService:
    def __init__(self, daos: DAOFactory):
        self.daos = daos

    def convert(self, anime_status: AnimeStatus) -> AnimeStatusDTO:
        return AnimeStatusDTO(
            id=anime_status.id,
            user_id=anime_status.user_id,
            anime_id=anime_status.user_id,
            status=anime_status.status,
        )

    def convert_multiple(
        self, anime_statuses: list[AnimeStatus]
    ) -> list[AnimeStatusDTO]:
        anime_statuses_dto = []
        for anime_status in anime_statuses:
            anime_statuses_dto.append(self.convert(anime_status))
        return anime_statuses_dto

    async def set(self, user_id: int, data: ReqSetAnimeStatus) -> AnimeStatusDTO:
        created, anime_status = await self.daos.anime_status_dao.get_or_create(
            defaults={"status": data.status},
            for_update=True,
            user_id=user_id,
            anime_id=data.anime_id,
        )
        if not created:
            anime_status.status = data.status
        await self.daos.session.commit()
        return self.convert(anime_status)

    async def get(self, user_id: int, anime_id: int) -> AnimeStatusDTO | None:
        anime_status = await self.daos.anime_status_dto.get(
            user_id=user_id, anime_id=anime_id
        )
        return self.convert(anime_status) if anime_status else None

    async def get_by_user(self, user_id) -> list[AnimeStatusDTO]:
        anime_statuses = await self.daos.anime_status_dao.get_multiple(user_id=user_id)
        return self.convert_multiple(anime_statuses)
