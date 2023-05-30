from typing import List, Annotated

from fastapi import APIRouter, Depends, Path

from dto import AnimeStatusDTO, UserDTO
from core import get_current_user, get_services
from services import ServicesFactory
from schemas import ReqSetAnimeStatus
from exceptions import session as session_excs

router = APIRouter(
    prefix="/anime/status",
    tags=["status"],
)


@router.post("/", response_model=AnimeStatusDTO)
async def set_anime_status(
    data: ReqSetAnimeStatus,
    current_user: UserDTO = Depends(get_current_user),
    services: ServicesFactory = Depends(get_services),
):
    anime_status = await services.anime_status_service.set(current_user.id, data)
    return anime_status


@router.get("/{username}/{anime_id}", response_model=AnimeStatusDTO)
async def get_anime_status(
    username: Annotated[
        str, Path(title="The username of the user to get his tracked anime")
    ],
    anime_id: Annotated[int, Path(title="The ID of the anime")],
    current_user: UserDTO = Depends(get_current_user),
    services: ServicesFactory = Depends(get_services),
):
    if current_user.username != username:
        raise session_excs.NoPermissionsError()

    anime_status = await services.anime_status_service.get(current_user.id, anime_id)
    return anime_status


@router.get("/{username}", response_model=List[AnimeStatusDTO])
async def get_anime_statuses_by_username(
    username: Annotated[
        str, Path(title="The username of the user to get his tracked anime")
    ],
    current_user: UserDTO = Depends(get_current_user),
    services: ServicesFactory = Depends(get_services),
):
    if current_user.username != username:
        raise session_excs.NoPermissionsError()

    anime_statuses = await services.anime_status_service.get_by_user(current_user.id)
    return anime_statuses
