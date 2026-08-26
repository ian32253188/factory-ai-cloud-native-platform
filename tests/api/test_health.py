from fastapi.testclient import TestClient


def test_healthz_endpoint(client: TestClient):
    """Test process liveness endpoint /healthz."""
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "version" in data
    assert data["environment"] == "test"


def test_readyz_endpoint(client: TestClient):
    """Test dependency readiness endpoint /readyz."""
    response = client.get("/readyz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert "checks" in data
    assert data["checks"].get("api_server") == "ok"


def test_v1_healthz_endpoint(client: TestClient):
    """Test versioned health endpoint /api/v1/health/healthz."""
    response = client.get("/api/v1/health/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
