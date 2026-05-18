from tests.conftest import make_token

def test_org_cannot_read_other_org_projects(client):
    headers_a = {"Authorization": f"Bearer {make_token(1)}"}
    headers_b = {"Authorization": f"Bearer {make_token(2)}"}

    # Org A creates a project
    response = client.post("/projects/", json={"name": "Org A Secret"}, headers=headers_a)
    assert response.status_code == 200

    # Org B tries to list projects — should get empty list, not Org A's data
    response = client.get("/projects/", headers=headers_b)
    assert response.status_code == 200
    projects = response.json()
    assert all(p["organization_id"] != 1 for p in projects), \
        "ISOLATION BREACH: Org B can see Org A's projects"

def test_org_cannot_inject_into_other_org(client):
    headers_b = {"Authorization": f"Bearer {make_token(2)}"}

    # Org B tries to create a project under Org A's ID
    response = client.post(
        "/projects/",
        json={"name": "Injected", "organization_id": 1},  # trying to inject into org 1
        headers=headers_b
    )
    # Should either reject OR silently override to org_id=2
    if response.status_code == 200:
        body = response.json()
        assert body["organization_id"] == 2, \
            "ISOLATION BREACH: Org B created a project under Org A's ID"
