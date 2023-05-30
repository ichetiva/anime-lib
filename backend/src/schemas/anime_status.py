from pydantic import BaseModel


class ReqSetAnimeStatus(BaseModel):
    anime_id: int
    status: str
