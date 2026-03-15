from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    organization_id: int


class ProjectResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
