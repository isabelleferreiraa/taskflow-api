from fastapi import APIRouter, HTTPException

from app.schemas.task import Task
from app.schemas.task_create import TaskCreate

router = APIRouter()

tasks = []


@router.post("/tasks")
def create_task(task: TaskCreate):
    next_id = len(tasks) + 1

    new_task = Task(
        id=next_id,
        title=task.title,
        description=task.description,
        completed=task.completed,
        urgent=task.urgent,
        due_date=task.due_date
    )

    tasks.append(new_task)

    return {
        "message": "Tarefa criada com sucesso!",
        "task": new_task
    }


@router.get("/tasks")
def list_tasks():
    return tasks


@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada."
    )


@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            task_updated = Task(
                id=task_id,
                title=updated_task.title,
                description=updated_task.description,
                completed=updated_task.completed,
                urgent=updated_task.urgent,
                due_date=updated_task.due_date
            )

            tasks[index] = task_updated

            return {
                "message": "Tarefa atualizada com sucesso!",
                "task": task_updated
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada."
    )


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)

            return {
                "message": "Tarefa removida com sucesso!"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada."
    )