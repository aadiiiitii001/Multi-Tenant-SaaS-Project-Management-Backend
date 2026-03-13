from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.models.organization import Organization

router = APIRouter(tags=["Organizations"])


@router.post("/")
def create_organization(name: str, db: Session = Depends(get_db)):

    organization = Organization(name=name)

    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization


@router.get("/")
def get_organizations(db: Session = Depends(get_db)):

    organizations = db.query(Organization).all()

    return organizations
