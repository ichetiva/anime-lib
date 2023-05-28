from pydantic import BaseModel


class SessionDTO(BaseModel):
    access_token: str

    class Config:
        orm_mode = True
