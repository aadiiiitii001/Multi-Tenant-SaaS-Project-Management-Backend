from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    status: str
    deadline: datetime
    project_id: int


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str

    class Config:
        orm_mode = True
