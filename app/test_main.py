from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    """Test /health endpoint returns correct status and JSON."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_version():
    """Test /version endpoint returns correct version."""
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}


def test_root():
    """Test / endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.text


def test_not_found():
    """Test unknown path returns 404."""
    response = client.get("/notfound")
    assert response.status_code == 404
