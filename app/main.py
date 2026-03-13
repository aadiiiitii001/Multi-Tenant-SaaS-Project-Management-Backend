from fastapi import FastAPI
from app.api.routes import auth, projects, tasks, organizations
from app.middleware.logging import LoggingMiddleware
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Multi Tenant SaaS Backend")

app.add_middleware(LoggingMiddleware)

app.include_router(auth.router, prefix="/auth")
app.include_router(organizations.router, prefix="/organizations")
app.include_router(projects.router, prefix="/projects")
app.include_router(tasks.router, prefix="/tasks")
