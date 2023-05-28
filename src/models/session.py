from sqlalchemy import Column, Integer, String, ForeignKey

from .base import Base
from ._mixins import TimestampMixin


class Session(Base, TimestampMixin):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    access_token = Column(String(512))

    def __repr__(self) -> str:
        return self.user_id
