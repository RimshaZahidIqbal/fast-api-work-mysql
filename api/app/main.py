from fastapi import FastAPI
from app.api.routes import router
from app.tasks.scheduler import schedule_tasks

app = FastAPI()

app.include_router(router)

schedule_tasks()
