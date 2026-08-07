def test_root(client):

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"



def test_health(client):

    response = client.get("/health/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"



def test_ready(client):

    response = client.get("/health/ready")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ready"