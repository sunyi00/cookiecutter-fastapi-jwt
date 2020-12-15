from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# Get an OAuth2 token
def test_login():
    response = client.post("/token", data={"username": "johndoe", "password": "secret"})
    assert response.status_code == 200

    global oauth2_token  # this is global so the rest of the tests can use it
    oauth2_token = response.json()["access_token"]


def test_users_me():
    auth_response = client.get(
        "/users/me", headers={"Authorization": "Bearer " + oauth2_token}
    )
    assert auth_response.status_code == 200
    assert auth_response.json()["username"] == "johndoe"


def test_users_me_items():
    auth_response = client.get(
        "/users/me/items", headers={"Authorization": "Bearer " + oauth2_token}
    )
    assert auth_response.status_code == 200
    assert auth_response.json()[0]["owner"] == "johndoe"
