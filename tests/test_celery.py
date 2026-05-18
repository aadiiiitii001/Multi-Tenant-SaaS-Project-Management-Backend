from unittest.mock import patch
from app.workers.celery_worker import send_welcome_email

def test_welcome_email_task():
    # Call the task function directly (no broker needed)
    result = send_welcome_email(org_id=1, org_name="Acme Corp")
    assert result["status"] == "sent"
    assert result["org_id"] == 1
    assert result["org_name"] == "Acme Corp"

def test_welcome_email_triggered_on_org_creation(client):
    # Patch .delay so it doesn't need Redis, but verify it gets called
    with patch("app.api.routes.organizations.send_welcome_email.delay") as mock_task:
        response = client.post("/organizations/?name=TestOrg")
        assert response.status_code == 200
        mock_task.assert_called_once()
        call_args = mock_task.call_args
        assert call_args.kwargs["org_name"] == "TestOrg"