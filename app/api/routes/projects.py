from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.services.project_service import ProjectService
from app.schemas.project_schema import ProjectCreate

router = APIRouter(tags=["Projects"])

project_service = ProjectService()


@router.post("/")
def create_project(data: ProjectCreate, db: Session = Depends(get_db)):

    project = project_service.create_project(db, data)

    return project


@router.get("/")
def get_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()

    return projects
