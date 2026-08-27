from fastapi.testclient import TestClient


def test_healthz_endpoint(client: TestClient):
    """Test process liveness endpoint /health."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "Market Intelligence" in data["service"]


def test_health_detail_endpoint(client: TestClient):
    """Test detailed health check endpoint /health/detail."""
    response = client.get("/health/detail?verbose=true")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "timestamp" in data
    assert data["mode"] == "verbose_diagnostic"
