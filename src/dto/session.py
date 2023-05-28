from datetime import datetime

from pydantic import BaseModel


class SessionDTO(BaseModel):
    id: int
    user_id: int
    access_token: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
