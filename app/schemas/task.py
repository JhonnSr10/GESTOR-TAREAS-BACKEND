from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    assignee_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    status: str = "todo"
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
