import json
import pytest


from sqlalchemy import insert, text
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from app.database import Base, engine, async_session
from app.config import settings
from app.tasks.models import Task
from app.main import app as fastapi_app

@pytest.fixture(scope='session', autouse=True)
async def prepare_database():
    """
    Фикстура для подготовки тестовой БД,
    пересоздает БД для каждой сессии, загружает тестовые данные
    :return:
    """
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(text("ALTER SEQUENCE tasks_id_seq RESTART WITH 1"))

    def open_mock_json():
        with open("app/tests/test_data_tasks.json", "r") as file:
            return json.load(file)

    tasks = open_mock_json()

    async with async_session() as session:
        add_tasks = insert(Task).values(tasks)

        await session.execute(add_tasks)
        await session.commit()

@pytest.fixture(scope='function')
async def ac():
    """
    Для каждого теста создается клиент FastAPI
    :return:
    """
    async with AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test/") as client:
        yield client