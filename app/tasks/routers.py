from typing import Dict, List

from fastapi import APIRouter

from app.tasks.models import StatusCode
from app.tasks.schemas import STask, STaskWithID
from app.tasks.dao import TaskDAO

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)

@router.post("/")
async def create_task(task: STask) -> Dict[str, str]:
    """Создать задачу"""
    await TaskDAO.add(title=task.title, description=task.description, status=task.status)
    return {'message': "OK"}

@router.get("/")
async def get_tasks(filter_by_status: StatusCode = None) -> List[STaskWithID]:
    """Получить все задачи по фильтру/без фильтра"""
    if filter_by_status is None:
        result = await TaskDAO.get_all()
        return result

    result = await TaskDAO.get_tasks_by_status(filter_by_status)
    return result

@router.get("/{task_id}")
async def get_task(task_id: int) -> STaskWithID | Dict[str, str]:
    """Получить задачу по ID"""
    task = await TaskDAO.get_one_or_none(id=task_id)
    if task is None:
        return {"message": "Не найдено"}
    return task

@router.put("/{task_id}")
async def update_task(task_id: int, task_data: STask) -> Dict[str, str]:
    """Апдейт задачи по ID"""
    task = await TaskDAO.get_one_or_none(id=task_id)
    if task is None:
        return {"message": "Не найдено"}
    await TaskDAO.update(id=task_id, title=task_data.title, description=task_data.description, status=task_data.status)
    return {'message': "OK"}

@router.delete("/{task_id}")
async def delete_task(task_id: int) -> Dict[str, str]:
    """Удаление задачи по ID"""
    task = await TaskDAO.get_one_or_none(id=task_id)
    if task is None:
        return {"message": "Не найдено"}
    await TaskDAO.delete(id=task_id)
    return {'message': "OK"}
