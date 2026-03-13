from pydantic import BaseSettings


class Settings(BaseSettings):

    # Application
    PROJECT_NAME: str = "Multi Tenant SaaS Backend"
    API_VERSION: str = "v1"

    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/saas_db"

    # JWT Security
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100

    class Config:
        env_file = ".env"


settings = Settings()
