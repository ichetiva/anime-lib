from typing import Literal

from pydantic import BaseModel


class Healthcheck(BaseModel):
    message: Literal["It works"]
