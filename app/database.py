from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

# Перед подключением к ДБ, выясняем в каком режиме находимся
if settings.MODE == "TEST":
    DATABASE_URL = f"postgresql+asyncpg://{settings.TEST_DB_USER}:{settings.TEST_DB_PASS}@{settings.TEST_DB_HOST}:{settings.TEST_DB_PORT}/{settings.TEST_DB_NAME}"
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
    DATABASE_PARAMS = {}

# Создаем движок БД
engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

# Создаем сессию
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass