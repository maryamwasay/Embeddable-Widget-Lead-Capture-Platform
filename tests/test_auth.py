import uuid


def test_register(client):

    email = f"{uuid.uuid4()}@example.com"

    response = client.post(
        "/auth/register",
        json={
            "company_name": "FlyRank",
            "email": email,
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User registered successfully"
    assert "user_id" in data
    assert "tenant_id" in data


def test_duplicate_registration(client):

    email = f"{uuid.uuid4()}@example.com"

    payload = {
        "company_name": "FlyRank",
        "email": email,
        "password": "password123"
    }

    response1 = client.post(
        "/auth/register",
        json=payload
    )

    assert response1.status_code == 200

    response2 = client.post(
        "/auth/register",
        json=payload
    )

    assert response2.status_code == 400
    assert response2.json()["detail"] == "Email already registered"


def test_login_success(client):

    email = f"{uuid.uuid4()}@example.com"

    password = "password123"

    client.post(
        "/auth/register",
        json={
            "company_name": "FlyRank",
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

    assert response.status_code == 200

    token = response.json()

    assert "access_token" in token
    assert token["token_type"] == "bearer"


def test_login_invalid_password(client):

    email = f"{uuid.uuid4()}@example.com"

    client.post(
        "/auth/register",
        json={
            "company_name": "FlyRank",
            "email": email,
            "password": "correctpassword"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"


def test_login_unknown_user(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "nouser@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"