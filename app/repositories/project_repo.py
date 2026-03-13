from sqlalchemy.orm import Session
from app.models.project import Project


class ProjectRepository:

    def create_project(self, db: Session, project_data: dict):
        project = Project(**project_data)

        db.add(project)
        db.commit()
        db.refresh(project)

        return project


    def get_project_by_id(self, db: Session, project_id: int):
        return db.query(Project)\
            .filter(Project.id == project_id)\
            .first()


    def get_projects_by_organization(self, db: Session, organization_id: int):
        return db.query(Project)\
            .filter(Project.organization_id == organization_id)\
            .all()


    def update_project(self, db: Session, project_id: int, update_data: dict):

        project = db.query(Project)\
            .filter(Project.id == project_id)\
            .first()

        if not project:
            return None

        for key, value in update_data.items():
            setattr(project, key, value)

        db.commit()
        db.refresh(project)

        return project


    def delete_project(self, db: Session, project_id: int):

        project = db.query(Project)\
            .filter(Project.id == project_id)\
            .first()

        if not project:
            return None

        db.delete(project)
        db.commit()

        return project
