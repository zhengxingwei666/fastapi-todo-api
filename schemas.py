# schemas.py
from typing import Optional
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="任务标题不能为空")
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, description="任务标题不能为空")
    completed: Optional[bool] = None