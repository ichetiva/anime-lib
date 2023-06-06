from typing import Annotated, List

from fastapi import APIRouter, Path, Depends, Query

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
    services: ServicesFactory = Depends(get_services),
):
    anime = await services.anime_service.get(id)
    return anime


@router.get("/", response_model=List[AnimeDTO])
async def get_all_anime(services: ServicesFactory = Depends(get_services)):
    anime_list = await services.anime_service.get_all()
    return anime_list


@router.get("/search", response_model=List[AnimeDTO])
async def search_anime(
    pattern: Annotated[str, Query(title="The part of anime name to get")],
    search_in: Annotated[str | None, Query(title="The column where to search")] = None,
    services: ServicesFactory = Depends(get_services),
):
    if not search_in:
        search_in = "title"
    anime_list = await services.anime_service.search(
        pattern=pattern, search_in=search_in
    )
    return anime_list
