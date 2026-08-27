from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "Market Intelligence" in payload["service"]
    assert payload["environment"] == "development"


def test_health_detail_basic() -> None:
    # 測試預設值 ?verbose=false 情況
    response = client.get("/health/detail")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "timestamp" not in payload  # 預設不應該包含 timestamp


def test_health_detail_verbose() -> None:
    # 測試帶入 ?verbose=true 情況
    response = client.get("/health/detail?verbose=true")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "timestamp" in payload     # 應該包含 timestamp
    assert payload["mode"] == "verbose_diagnostic"

