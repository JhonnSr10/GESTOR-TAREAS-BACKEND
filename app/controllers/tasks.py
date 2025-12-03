from fastapi import APIRouter, Depends, HTTPException
from typing import List
from db import get_session, init_db
from models.task import Task
from schemas.task import TaskCreate, TaskRead

router = APIRouter()

@router.on_event("startup")
def on_startup():
    init_db()

@router.get("/")
def list_tasks(session=Depends(get_session)):
    results = session.query(Task).all()
    return [TaskRead.from_orm(r) for r in results]

@router.post("/")
def create_task(task: TaskCreate, session=Depends(get_session)):
    db_task = Task(title=task.title, description=task.description, assignee_id=task.assignee_id)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return TaskRead.from_orm(db_task)

@router.get("/{task_id}")
def get_task(task_id: int, session=Depends(get_session)):
    task = session.query(Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskRead.from_orm(task)

@router.delete("/{task_id}")
def delete_task(task_id: int, session=Depends(get_session)):
    task = session.query(Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"ok": True}
