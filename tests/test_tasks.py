from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():

    data = {
        "title": "Build API",
        "status": "todo",
        "deadline": "2026-04-01T10:00:00",
        "project_id": 1
    }

    response = client.post("/tasks/", json=data)

    assert response.status_code == 200

    body = response.json()

    assert body["title"] == "Build API"
    assert body["status"] == "todo"


def test_get_tasks():

    response = client.get("/tasks/?page=1")

    assert response.status_code == 200
