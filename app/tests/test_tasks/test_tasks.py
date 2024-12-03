from httpx import AsyncClient
import pytest


async def test_get_tasks(ac: AsyncClient):
    """
    Тест получения всех задач
    :param ac:
    :return:
    """
    response = await ac.get("/tasks/")
    assert response.status_code == 200
    first_item = response.json()[0]
    assert first_item["title"] == "string"
    assert first_item["description"] == "string"
    assert first_item["status"] == "todo"

    last_item = response.json()[-1]
    assert last_item["title"] == "string222"
    assert last_item["description"] == "str2ing"
    assert last_item["status"] == "in_progress"

async def test_get_tasks_by_filter(ac: AsyncClient):
    """
    Тест получение всех задач по заданному фильтру
    :param ac:
    :return:
    """
    response = await ac.get("/tasks/?filter_by_status=in_progress")
    assert response.status_code == 200
    assert len(response.json()) == 3
    first_item = response.json()[0]
    assert first_item["title"] == "string222"
    assert first_item["description"] == "str2ing"
    assert first_item["status"] == "in_progress"

async def test_create_task(ac: AsyncClient):
    """
    Тест создания задачи
    :param ac:
    :return:
    """
    data = {"title": "test_creating", "description": "test_creating", "status": "todo"}
    response = await ac.post("/tasks/", json=data)
    assert response.status_code == 200

async def test_create_task_invalid(ac: AsyncClient):
    """
    Тест создания задачи с невалид данными
    :param ac:
    :return:
    """
    data = {"title": "test_creating", "description": "test_creating", "status": "iawdda"}
    response = await ac.post("/tasks/", json=data)
    assert response.status_code == 422

async def test_get_task_by_id(ac: AsyncClient):
    """
    Тест получения задачи по ID
    :param ac:
    :return:
    """
    response = await ac.get(f"/tasks/3")
    assert response.status_code == 200
    item = response.json()
    assert item["title"] == "string222"
    assert item["description"] == "str2ing"
    assert item["status"] == "in_progress"

async def test_delete_task(ac: AsyncClient):
    """
    Тест удаления задачи по ID
    :param ac:
    :return:
    """
    response = await ac.delete(f"/tasks/1")
    assert response.status_code == 200
    item = response.json()
    assert item["message"] == "OK"