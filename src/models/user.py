from sqlalchemy import Column, String, Integer, Boolean, DateTime

from .base import Base
from ._mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)

    is_admin = Column(Boolean, default=False)

    last_login_at = Column(DateTime, default=None, nullable=True)

    def __repr__(self) -> str:
        return self.username
