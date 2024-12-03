from pydantic import BaseModel
from app.tasks.models import StatusCode


class STask(BaseModel):
    title: str
    description: str
    status: StatusCode

    class Config:
        from_attributes = True

class STaskWithID(BaseModel):
    id: int
    title: str
    description: str
    status: StatusCode

    class Config:
        from_attributes = True