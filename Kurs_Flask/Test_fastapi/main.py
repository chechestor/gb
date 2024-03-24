'''
uvicorn app2:app --reload

Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.
'''

from fastapi import FastAPI
import logging

from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    title: Optional[str] = ""
    description: Optional[str] = ""
    status: Optional[bool] = False

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tasks_counter=0
tasks={}

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/tasks/")
async def read_root():
    global tasks
    return tasks


@app.get("/tasks/{task_id}")
async def read_item(task_id: int, q: str = None):
    global tasks
    if task_id in tasks:
        return tasks[task_id]
    else:
        return None


@app.post("/tasks/")
async def create_item(task: Task):
    global tasks_counter
    global tasks
    id = tasks_counter
    tasks_counter += 1
    tasks[id] = Task()
    return id


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    global tasks
    if task_id in tasks:
        for field in task:
            tasks[task_id] = task[f]
    return tasks[task_id]


@app.delete("/tasks/{task_id}")
async def delete_item(item_id: int):
    global tasks
    if item_id in tasks:
        del tasks[item_id]
        return True
    else:
        return False
