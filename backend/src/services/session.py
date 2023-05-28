from datetime import datetime

import jwt

from dao import DAOFactory
from models import Session
from dto import UserDTO, SessionDTO
from core import settings
from services import ServicesFactory


class SessionService:
    def __init__(self, daos: DAOFactory, services: ServicesFactory) -> None:
        self.daos = daos
        self.services = services

    def convert(self, session: Session) -> SessionDTO:
        return SessionDTO(
            access_token=session.access_token,
        )

    async def create(self, user: UserDTO) -> SessionDTO:
        created, session = await self.daos.session_dao.get_or_create(
            defaults={"access_token": self._generate_access_token(user.id)},
            user_id=user.id,
        )
        if created:
            await self.daos.session.commit()

        return self.convert(session)

    async def get_user(self, token: str) -> UserDTO:
        session = await self.daos.session_dao.get(access_token=token)
        user = await self.daos.user_dao.get(id=session.user_id)
        return self.services.user_service.convert(user)

    def _generate_access_token(self, user_id: int) -> str:
        access_token = jwt.encode(
            {
                "user_id": user_id,
                "created_at": str(datetime.now()),
            },
            settings.SECRET_KEY,
            algorithm="HS512",
        )
        return access_token
