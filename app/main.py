from fastapi import FastAPI

from app.tasks.routers import router as tasks_router
app = FastAPI()

app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "see /docs"}