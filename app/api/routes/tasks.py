from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.task_service import TaskService
from app.schemas.task_schema import TaskCreate
from app.models.task import Task

router = APIRouter(tags=["Tasks"])

task_service = TaskService()


@router.post("/")
def create_task(data: TaskCreate, db: Session = Depends(get_db)):

    task = task_service.create_task(db, data)

    return task


@router.get("/")
def get_tasks(page: int = 1, db: Session = Depends(get_db)):

    limit = 20
    offset = (page - 1) * limit

    tasks = db.query(Task)\
        .limit(limit)\
        .offset(offset)\
        .all()

    return tasks
