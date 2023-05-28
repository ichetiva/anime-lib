from pydantic import BaseModel


class ReqCreateSession(BaseModel):
    username: str
    password: str
