from unittest.mock import patch
from tests.conftest import make_token
from datetime import datetime

@patch("app.api.routes.organizations.send_welcome_email.delay")
def test_task_status_transition(mock_email, client):
    headers = {"Authorization": f"Bearer {make_token(1)}"}

    client.post("/organizations/?name=OrgA")
    client.post("/projects/", json={"name": "Project A"}, headers=headers)

    response = client.post("/tasks/", json={
        "title": "My Task",
        "status": "todo",
        "deadline": "2026-12-31T00:00:00",
        "project_id": 1
    }, headers=headers)
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.patch(f"/tasks/{task_id}",
        json={"status": "in_progress"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"

    response = client.patch(f"/tasks/{task_id}",
        json={"status": "done"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["status"] == "done"

@patch("app.api.routes.organizations.send_welcome_email.delay")
def test_cannot_update_other_org_task(mock_email, client):
    headers_a = {"Authorization": f"Bearer {make_token(1)}"}
    headers_b = {"Authorization": f"Bearer {make_token(2)}"}

    client.post("/organizations/?name=OrgA")
    client.post("/projects/", json={"name": "Project A"}, headers=headers_a)
    client.post("/tasks/", json={
        "title": "Org A Task",
        "status": "todo",
        "deadline": "2026-12-31T00:00:00",
        "project_id": 1
    }, headers=headers_a)

    response = client.patch("/tasks/1",
        json={"status": "done"},
        headers=headers_b
    )
    assert response.status_code == 404