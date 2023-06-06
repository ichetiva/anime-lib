from typing import Literal, Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: Literal["success", "error"]
    data: Any

    class Config:
        orm_mode = True


class Healthcheck(BaseModel):
    message: Literal["It works"]

