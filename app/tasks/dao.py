from typing import List

from app.database import async_session

from sqlalchemy import select

from app.dao.base import BaseDAO
from app.tasks.models import Task, StatusCode
from app.tasks.schemas import STask

class TaskDAO(BaseDAO):

    model = Task

    @classmethod
    async def get_tasks_by_status(cls, status: StatusCode) -> List[STask]:
        async with async_session() as session:
            query = select(cls.model).filter_by(status=status)
            result = await session.execute(query)
            return result.scalars().all()
