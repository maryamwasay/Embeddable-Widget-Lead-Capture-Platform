import uuid


def get_token(client):

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

    token = response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_create_widget(client):

    headers = get_token(client)

    response = client.post(
        "/widgets/",
        headers=headers,
        json={
            "title": "Contact Form",
            "description": "Lead Capture",
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

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Contact Form"


def test_get_widgets(client):

    headers = get_token(client)

    response = client.get(
        "/widgets/",
        headers=headers
    )

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_get_widget_not_found(client):

    headers = get_token(client)

    response = client.get(
        "/widgets/999999",
        headers=headers
    )

    assert response.status_code == 404


def test_update_widget_not_found(client):

    headers = get_token(client)

    response = client.put(
        "/widgets/999999",
        headers=headers,
        json={
            "title": "Updated"
        }
    )

    assert response.status_code == 404


def test_delete_widget_not_found(client):

    headers = get_token(client)

    response = client.delete(
        "/widgets/999999",
        headers=headers
    )

    assert response.status_code == 404