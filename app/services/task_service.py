from sqlalchemy.orm import Session
from app.models.task import Task


class TaskService:

    def create_task(self, db: Session, data):

        task = Task(**data.dict())

        db.add(task)
        db.commit()
        db.refresh(task)

        return task
