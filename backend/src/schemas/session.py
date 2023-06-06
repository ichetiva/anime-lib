from pydantic import BaseModel

from .base import BaseResponse
from dto import SessionDTO


class ReqCreateSession(BaseModel):
    username: str
    password: str


class ResSession(BaseResponse):
    data: SessionDTO | None = None
