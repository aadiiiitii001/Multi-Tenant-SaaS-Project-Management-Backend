from sqlalchemy.orm import Session
from app.models.project import Project


class ProjectService:

    def create_project(self, db: Session, data):

        project = Project(**data.dict())

        db.add(project)
        db.commit()
        db.refresh(project)

        return project
