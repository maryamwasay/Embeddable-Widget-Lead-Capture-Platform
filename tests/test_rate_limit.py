import uuid


def create_widget(client):

    email = f"{uuid.uuid4()}@example.com"
    password = "password123"

    client.post(
        "/auth/register",
        json={
            "company_name": "Rate Limit Test",
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
            "title": "Rate Test",
            "description": "Testing",
            "widget_type": "popup",
            "button_text": "Submit",
            "fields": [
                {
                    "name": "name",
                    "type": "text",
                    "required": True
                }
            ]
        }
    )

    return widget.json()["id"]


def test_rate_limit(client):

    widget_id = create_widget(client)

    status_codes = []

    for _ in range(6):

        response = client.post(
            f"/public/submit/{widget_id}",
            json={
                "name": "John",
                "email": "john@test.com"
            }
        )

        status_codes.append(response.status_code)

    assert 429 in status_codes