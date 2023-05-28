from typing import Type, TypeVar, Generic, Any, Tuple

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base

Model = TypeVar("Model", Base, Base)


class BaseDAO(Generic[Model]):
    def __init__(self, model: Type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get(
        self, *, for_update: bool = False, **kwargs: dict[str, Any]
    ) -> Model | None:
        stmt = select(self.model).filter_by(**kwargs)
        if for_update:
            stmt = stmt.with_for_update()
        instance = await self.session.scalar(stmt)
        return instance

    async def get_or_create(
        self, *, for_update: bool = False, defaults: dict = {}, **kwargs: dict[str, Any]
    ) -> Tuple[bool, Model]:
        instance = await self.get(for_update=for_update, **kwargs)
        if instance:
            return False, instance
        kwargs.update(defaults)
        instance = self.model(**kwargs)
        self.session.add(instance)
        return True, instance

    async def update(self, *, id: int, **kwargs: dict[str, Any]) -> None:
        stmt = update(self.model).where(self.model.id == id).values(**kwargs)
        await self.session.execute(stmt)

    async def delete(self, *, id: int) -> None:
        stmt = delete(self.model).where(self.model.id == id)
        await self.session.execute(stmt)
