from fastapi import FastAPI
from app.api.routes import auth, projects, tasks, organizations
from app.middleware.logging import LoggingMiddleware

app = FastAPI(title="Multi Tenant SaaS Backend")

# Middleware
app.add_middleware(LoggingMiddleware)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(organizations.router, prefix="/organizations", tags=["Organizations"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])


@app.get("/")
def health_check():
    return {"status": "running"}
