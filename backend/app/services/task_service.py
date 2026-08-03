from pydantic import BaseModel
from typing import List
import datetime

class Task(BaseModel):
    id: int
    title: str
    description: str
    due_date: str
    status: str = "pending"

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str, description: str, due_date: str):
        task_id = len(self.tasks) + 1
        task = Task(id=task_id, title=title, description=description, due_date=due_date)
        self.tasks.append(task)
        return task

    def get_tasks(self):
        return self.tasks

task_service = TaskService()
