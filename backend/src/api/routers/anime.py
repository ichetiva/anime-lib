from typing import Annotated

from fastapi import APIRouter, Path, Depends, Query

from core import get_services
from services import ServicesFactory
from schemas import ResAnime, ResAnimeList

router = APIRouter(
    prefix="/anime",
    tags=["anime"],
)


@router.get("/{id}", response_model=ResAnime)
async def get_single_anime(
    id: Annotated[int, Path(title="The ID of the anime to get")],
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    anime = await services.anime_service.get(id)
    return {
        "status": "success",
        "data": anime,
    }


@router.get("/", response_model=ResAnimeList)
async def get_all_anime(
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    anime_list = await services.anime_service.get_all()
    return {
        "status": "success",
        "data": anime_list,
    }


@router.get("/search", response_model=ResAnimeList)
async def search_anime(
    pattern: Annotated[str, Query(title="The part of anime name to get")],
    services: Annotated[ServicesFactory, Depends(get_services)],
    search_in: Annotated[str | None, Query(title="The column where to search")] = None,
):
    if not search_in:
        search_in = "title"
    anime_list = await services.anime_service.search(
        pattern=pattern, search_in=search_in
    )
    return {
        "status": "success",
        "data": anime_list,
    }
