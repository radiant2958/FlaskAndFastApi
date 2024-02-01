from fastapi import FastAPI, HTTPException
from typing import List, Dict
from uuid import uuid4, UUID
from bd import Task

app = FastAPI()
tasks: Dict[UUID, Task] = {}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    task_id = uuid4()
    tasks[task_id] = task
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}
