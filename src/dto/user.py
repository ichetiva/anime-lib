from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    is_admin: bool
    last_login_at: datetime | None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
