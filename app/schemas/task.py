from datetime import date

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    completed: bool = False
    urgent: bool = False
    due_date: date