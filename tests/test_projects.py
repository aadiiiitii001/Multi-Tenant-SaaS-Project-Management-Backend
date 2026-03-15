from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_project():

    data = {
        "name": "Backend Platform",
        "organization_id": 1
    }

    response = client.post("/projects/", json=data)

    assert response.status_code == 200

    body = response.json()

    assert body["name"] == "Backend Platform"


def test_get_projects():

    response = client.get("/projects/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
