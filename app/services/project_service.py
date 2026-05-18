from sqlalchemy.orm import Session
from app.repositories.project_repo import ProjectRepository

project_repo = ProjectRepository()

class ProjectService:
    def create_project(self, db: Session, name: str, organization_id: int):
        return project_repo.create_project(db, name, organization_id)

    def get_projects(self, db: Session, organization_id: int):
        return project_repo.get_projects_by_organization(db, organization_id)
