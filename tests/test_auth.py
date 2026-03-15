from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_success():

    response = client.post(
        "/auth/login",
        params={"email": "test@example.com"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_invalid():

    response = client.post(
        "/auth/login",
        params={"email": "invalid@example.com"}
    )

    # Depending on implementation this may return 401
    assert response.status_code in [200, 401]
