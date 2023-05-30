from sqlalchemy import Column, Integer, ForeignKey, Enum

from .base import Base
from dto import Status


class AnimeStatus(Base):
    __tablename__ = "anime_statuses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    anime_id = Column(Integer, ForeignKey("anime.id", ondelete="CASCADE"))
    status = Column(Enum(Status))

    def __repr__(self) -> str:
        return self.id
