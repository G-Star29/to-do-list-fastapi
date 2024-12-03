from typing import Literal
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()
print(settings.DB_HOST)