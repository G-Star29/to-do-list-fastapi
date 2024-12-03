from fastapi import FastAPI

from app.tasks.routers import router as tasks_router
app = FastAPI()

app.include_router(tasks_router)