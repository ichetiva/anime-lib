import hashlib

from dao import DAOFactory
from schemas import (
    ReqCreateUser,
    ReqUpdateUser,
    ReqChangeUserPassword,
    ReqCreateSession,
)
from models import User
from dto import UserDTO
from exceptions import user as user_excs


class UserService:
    def __init__(self, daos: DAOFactory) -> None:
        self.daos = daos

    def convert(self, user: User) -> UserDTO:
        return UserDTO(
            id=user.id,
            username=user.username,
            is_admin=user.is_admin,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def create(self, data: ReqCreateUser) -> UserDTO:
        created, user = await self.daos.user_dao.get_or_create(
            defaults={"password": self._hash_password(data.password)},
            username=data.username,
        )
        if not created:
            raise user_excs.AlreadyExistsError()

        await self.daos.session.commit()

        return self.convert(user)

    async def get(self, username: str) -> UserDTO:
        user = await self.daos.user_dao.get(username=username)
        if not user:
            raise user_excs.DoesNotExistError()
        return self.convert(user)

    async def update(self, username: str, data: ReqUpdateUser) -> UserDTO:
        user = await self.daos.user_dao.get(for_update=True, username=username)
        if not user:
            raise user_excs.DoesNotExistError()

        user.username = data.new_username
        await self.daos.session.commit()

        return self.convert(user)

    async def change_password(
        self, username: str, data: ReqChangeUserPassword
    ) -> UserDTO:
        user = await self.daos.user_dao.get(for_update=True, username=username)
        if not user:
            raise user_excs.DoesNotExistError()
        elif not self._match_passwords(user.password, data.password):
            raise user_excs.WrongPasswordError()
        elif data.new_password != data.repeat_new_password:
            raise user_excs.PasswordsMismatchError()

        user.password = self._hash_password(data.new_password)
        await self.daos.session.commit()

        return user

    async def delete(self, username: str) -> bool:
        try:
            await self.daos.user_dao.delete_by_username(username)
            await self.daos.session.commit()
        except:
            return False
        return True

    async def authorize(self, data: ReqCreateSession) -> UserDTO:
        user = await self.daos.user_dao.get(username=data.username)

        if not user:
            raise user_excs.DoesNotExistError()
        elif not self._match_passwords(user.password, data.password):
            raise user_excs.WrongPasswordError()

        return self.convert(user)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha512(password.encode()).hexdigest()

    def _match_passwords(self, hashed_password: str, password: str) -> bool:
        return hashed_password == self._hash_password(password)
