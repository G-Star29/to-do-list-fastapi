from typing import Any

from sqlalchemy import insert, select, update, delete

from app.database import async_session

class BaseDAO:
    """
    Содержит базовые функции для взаимодействия с БД.
    """

    model = None

    @classmethod
    async def add(cls, **data: Any) -> None:
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_all(cls) -> Any:
        async with async_session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_one_or_none(cls, **filter_by: Any) -> Any:
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def update(cls, id: int, **data: Any) -> None:
        async with async_session() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, id: int) -> None:
        async with async_session() as session:
            query = delete(cls.model).where(cls.model.id == id)
            await session.execute(query)
            await session.commit()