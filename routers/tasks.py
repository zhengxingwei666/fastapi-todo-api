# routers/tasks.py
from fastapi import APIRouter, HTTPException
from typing import Optional
# 导入之前建好的两个文件
import database
import schemas

# 创建路由实例，设置路径前缀和标签
router = APIRouter(prefix="/tasks", tags=["任务管理"])

@router.get("")
def get_tasks(completed: Optional[bool] = None):
    if completed is None:
        return database.mock_tasks
    return [task for task in database.mock_tasks if task["completed"] == completed]

@router.get("/{task_id}")
def get_task(task_id: int):
    for task in database.mock_tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("", status_code=201)
def create_task(task: schemas.TaskCreate):
    database.current_id += 1
    new_task_dict = task.model_dump()
    new_task_dict["id"] = database.current_id
    database.mock_tasks.append(new_task_dict)
    return new_task_dict

@router.patch("/{task_id}")
def update_task(task_id: int, task_update: schemas.TaskUpdate):
    for task in database.mock_tasks:
        if task["id"] == task_id:
            update_data = task_update.model_dump(exclude_unset=True)
            task.update(update_data)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    for task in database.mock_tasks:
        if task["id"] == task_id:
            database.mock_tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail="Task not found")