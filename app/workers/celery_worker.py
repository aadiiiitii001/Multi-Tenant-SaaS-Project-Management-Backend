from celery import Celery
from app.core.config import settings

# Create Celery application
celery_app = Celery(
    "saas_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

# Optional configuration
celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)


# Example background task
@celery_app.task
def send_email_notification(email: str, subject: str, message: str):
    """
    Example background task to simulate sending email
    """

    print("Sending email...")
    print(f"To: {email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")

    return {"status": "email sent"}
