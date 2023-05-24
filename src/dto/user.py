from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    password: str
    is_admin: bool
    last_login_at: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
