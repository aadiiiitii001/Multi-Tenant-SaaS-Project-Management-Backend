from unittest.mock import patch
from tests.conftest import make_token

@patch("app.api.routes.organizations.send_welcome_email.delay")
def test_create_project(mock_email, client):
    headers = {"Authorization": f"Bearer {make_token(1)}"}

    client.post("/organizations/?name=TestOrg")
    response = client.post("/projects/", json={"name": "Backend Platform"}, headers=headers)

    assert response.status_code == 200
    assert response.json()["name"] == "Backend Platform"

@patch("app.api.routes.organizations.send_welcome_email.delay")
def test_get_projects(mock_email, client):
    headers = {"Authorization": f"Bearer {make_token(1)}"}

    client.post("/organizations/?name=TestOrg")
    client.post("/projects/", json={"name": "Backend Platform"}, headers=headers)

    response = client.get("/projects/", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1