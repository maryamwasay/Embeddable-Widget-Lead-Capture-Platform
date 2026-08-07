import uuid


def create_widget(client):

    email = f"{uuid.uuid4()}@example.com"
    password = "password123"

    client.post(
        "/auth/register",
        json={
            "company_name": "Public Test",
            "email": email,
            "password": password
        }
    )

    login = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    token = login.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    widget = client.post(
        "/widgets/",
        headers=headers,
        json={
            "title": "Contact Form",
            "description": "Testing",
            "widget_type": "popup",
            "button_text": "Submit",
            "fields": [
                {
                    "name": "name",
                    "type": "text",
                    "required": True
                },
                {
                    "name": "email",
                    "type": "email",
                    "required": True
                }
            ]
        }
    )

    return widget.json()["id"]


def test_get_public_widget(client):

    widget_id = create_widget(client)

    response = client.get(
        f"/public/widget/{widget_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == widget_id
    assert "fields" in data


def test_widget_not_found(client):

    response = client.get(
        "/public/widget/999999"
    )

    assert response.status_code == 404


def test_submit_widget(client):

    widget_id = create_widget(client)

    response = client.post(
        f"/public/submit/{widget_id}",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123456789",
            "message": "Hello"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "submission_id" in data


def test_submit_invalid_widget(client):

    response = client.post(
        "/public/submit/999999",
        json={
            "name": "John",
            "email": "john@test.com"
        }
    )

    assert response.status_code == 404