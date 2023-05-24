from typing import Annotated

from fastapi import APIRouter, Depends, Path

from schemas import ReqCreateUser, ReqUpdateUser, ReqChangeUserPassword
from dto import UserDTO
from services import ServicesFactory
from core import get_services

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserDTO)
async def create_user(
    data: ReqCreateUser,
    services: ServicesFactory = Depends(get_services),
):
    user = await services.user_service.create(data)
    return user


@router.get("/{username}", response_model=UserDTO)
async def get_single_user(
    username: Annotated[str, Path(title="The username of the user to get")],
    services: ServicesFactory = Depends(get_services),
):
    user = await services.user_service.get(username)
    return user


@router.put("/{username}", response_model=UserDTO)
async def update_user(
    username: Annotated[str, Path(title="The username of the user to get")],
    data: ReqUpdateUser,
    services: ServicesFactory = Depends(get_services),
):
    user = await services.user_service.update(username, data)
    return user


@router.put("/{username}/change_password", response_model=UserDTO)
async def change_user_password(
    username: Annotated[str, Path(title="The username of the user to get")],
    data: ReqChangeUserPassword,
    services: ServicesFactory = Depends(get_services),
):
    user = await services.user_service.change_password(username, data)
    return user


@router.delete("/{username}", response_model=UserDTO)
async def delete_user(
    username: Annotated[str, Path(title="The username of the user to get")],
    services: ServicesFactory = Depends(get_services),
):
    ok = await services.user_service.delete(username)
    return {"ok": ok}
