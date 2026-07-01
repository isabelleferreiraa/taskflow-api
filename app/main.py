from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.tasks import router as tasks_router

app = FastAPI(
    title="TaskFlow API",
    version="1.0.0",
    description="API para gerenciamento de tarefas e projetos."
)


@app.get("/")
def home():
    return {
        "application": "TaskFlow API",
        "version": "1.0.0",
        "status": "online",
        "documentation": "/docs"
    }


app.include_router(health_router)
app.include_router(tasks_router)