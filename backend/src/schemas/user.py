from pydantic import BaseModel

from .base import BaseResponse
from dto import UserDTO


class ReqCreateUser(BaseModel):
    username: str
    password: str


class ReqUpdateUser(BaseModel):
    new_username: str


class ReqChangeUserPassword(BaseModel):
    password: str
    new_password: str
    repeat_new_password: str


class ResUser(BaseResponse):
    data: UserDTO | None = None
