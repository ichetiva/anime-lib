from sqlalchemy import Column, Integer, String

from ._mixins import TimestampMixin
from .base import Base


class Anime(Base, TimestampMixin):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True)
    title = Column(String(512))
    type_ = Column(String(32))
    publishing_year = Column(Integer)
    poster_link = Column(String(512))

    def __repr__(self) -> str:
        return self.title
