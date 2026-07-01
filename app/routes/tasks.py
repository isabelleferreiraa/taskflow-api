from fastapi import APIRouter
from app.schemas.task import Task

router = APIRouter()

tasks = []


@router.post("/tasks")
def create_task(task: Task):
    tasks.append(task)

    return {
        "message": "Task created successfully!",
        "task": task
    }