import uuid


def get_token(client):

    email = f"{uuid.uuid4()}@example.com"
    password = "password123"

    client.post(
        "/auth/register",
        json={
            "company_name": "Dashboard Company",
            "email": email,
            "password": password
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_dashboard_summary(client):

    headers = get_token(client)

    response = client.get(
        "/dashboard/summary",
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert "widgets" in data
    assert "submissions" in data


def test_dashboard_widgets(client):

    headers = get_token(client)

    response = client.get(
        "/dashboard/widgets",
        headers=headers
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_dashboard_countries(client):

    headers = get_token(client)

    response = client.get(
        "/dashboard/countries",
        headers=headers
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_dashboard_requires_auth(client):

    response = client.get("/dashboard/summary")

    assert response.status_code == 401