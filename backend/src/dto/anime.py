from pydantic import BaseModel


class AnimeDTO(BaseModel):
    id: int
    title: str
    type_: str
    publishing_year: int
    poster_link: str

    class Config:
        orm_mode = True
