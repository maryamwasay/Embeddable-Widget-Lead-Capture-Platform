def test_cors_preflight(client):

    response = client.options(
        "/public/submit/1",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST"
        }
    )

    assert response.status_code == 200


def test_cors_headers_exist(client):

    response = client.options(
        "/public/submit/1",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST"
        }
    )

    assert (
        "access-control-allow-origin"
        in response.headers
    )


def test_root_has_cors(client):

    response = client.get(
        "/",
        headers={
            "Origin": "http://localhost:3000"
        }
    )

    assert response.status_code == 200