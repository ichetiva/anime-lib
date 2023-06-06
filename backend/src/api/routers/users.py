from typing import Annotated

from fastapi import APIRouter, Depends, Path

from schemas import (
    ReqCreateUser,
    ReqUpdateUser,
    ReqChangeUserPassword,
    ResUser,
)
from dto import UserDTO
from services import ServicesFactory
from core import get_services, get_current_user
from exceptions import session as session_excs

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=ResUser)
async def create_user(
    data: ReqCreateUser,
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    user = await services.user_service.create(data)
    return {
        "status": "success",
        "data": user,
    }


@router.get("/{username}", response_model=UserDTO)
async def get_single_user(
    username: Annotated[str, Path(title="The username of the user to get")],
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    user = await services.user_service.get(username)
    return {
        "status": "success",
        "data": user,
    }


@router.put("/{username}", response_model=UserDTO)
async def update_user(
    data: ReqUpdateUser,
    username: Annotated[str, Path(title="The username of the user to get")],
    services: Annotated[ServicesFactory, Depends(get_services)],
    current_user: Annotated[UserDTO, Depends(get_current_user)],
):
    if current_user.username != username:
        raise session_excs.NoPermissionsError()

    user = await services.user_service.update(username, data)
    return {
        "status": "success",
        "data": user,
    }


@router.put("/{username}/change_password", response_model=UserDTO)
async def change_user_password(
    data: ReqChangeUserPassword,
    username: Annotated[str, Path(title="The username of the user to get")],
    services: Annotated[ServicesFactory, Depends(get_services)],
    current_user: Annotated[UserDTO, Depends(get_current_user)],
):
    if current_user.username != username:
        raise session_excs.NoPermissionsError()

    user = await services.user_service.change_password(username, data)
    return {
        "status": "success",
        "data": user,
    }


@router.delete("/{username}", response_model=UserDTO)
async def delete_user(
    username: Annotated[str, Path(title="The username of the user to get")],
    services: Annotated[ServicesFactory, Depends(get_services)],
    current_user: Annotated[UserDTO, Depends(get_current_user)],
):
    if current_user.username != username:
        raise session_excs.NoPermissionsError()

    ok = await services.user_service.delete(username)
    return {
        "status": "success",
        "data": None,
    }
