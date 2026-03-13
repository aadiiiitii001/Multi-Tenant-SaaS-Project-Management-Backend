from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.task import Task

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks")
def get_tasks(page:int=1, db:Session=Depends(get_db)):

    limit = 20
    offset = (page-1) * limit

    tasks = db.query(Task)\
        .order_by(Task.deadline)\
        .limit(limit)\
        .offset(offset)\
        .all()

    return tasks
