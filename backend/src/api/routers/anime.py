from typing import Annotated

from fastapi import APIRouter, Path, Depends

from dto import AnimeDTO
from core import get_services
from services import ServicesFactory

router = APIRouter(
    prefix="/anime",
    tags=["anime"],
)


@router.get("/{id}", response_model=AnimeDTO)
async def get_single_anime(
    id: Annotated[int, Path(title="The ID of the anime to get")],
    services: ServicesFactory = Depends(get_services()),
):
    anime = await services.anime_service.get(id)
    return anime
