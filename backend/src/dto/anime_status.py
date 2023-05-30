from enum import Enum

from pydantic import BaseModel


class Status(Enum):
    scheduled = "scheduled"
    viewed = "viewed"
    watching = "watching"
    abandoned = "abandoned"
    postponed = "postponed"


class AnimeStatusDTO(BaseModel):
    id: int
    user_id: int
    anime_id: int
    status: Status

    class Config:
        orm_mode = True
