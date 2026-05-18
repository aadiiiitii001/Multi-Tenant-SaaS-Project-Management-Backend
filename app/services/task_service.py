from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.project import Project

class TaskService:

    def create_task(self, db: Session, data, organization_id: int):
        # Verify project belongs to this org before creating task
        project = db.query(Project).filter(
            Project.id == data.project_id,
            Project.organization_id == organization_id
        ).first()
        if not project:
            return None
        task = Task(
            title=data.title,
            status=data.status,
            deadline=data.deadline,
            project_id=data.project_id
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def get_tasks(self, db: Session, organization_id: int):
        # Get tasks only for projects belonging to this org
        return db.query(Task).join(Project).filter(
            Project.organization_id == organization_id
        ).all()

    def update_task(self, db: Session, task_id: int, organization_id: int, update_data: dict):
        task = db.query(Task).join(Project).filter(
            Task.id == task_id,
            Project.organization_id == organization_id
        ).first()
        if not task:
            return None
        for key, value in update_data.items():
            if value is not None:
                setattr(task, key, value)
        db.commit()
        db.refresh(task)
        return task

    def delete_task(self, db: Session, task_id: int, organization_id: int):
        task = db.query(Task).join(Project).filter(
            Task.id == task_id,
            Project.organization_id == organization_id
        ).first()
        if not task:
            return None
        db.delete(task)
        db.commit()
        return {"deleted": task_id}