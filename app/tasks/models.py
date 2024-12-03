import enum

from sqlalchemy import Column, Integer, String, Text, Enum

from app.database import Base

class StatusCode(enum.Enum):
    """
    Статус код содержит все допустимые значения для поля 'status'
    """
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(StatusCode), default=StatusCode.done, nullable=False)