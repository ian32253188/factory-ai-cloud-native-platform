from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_keywords_search_with_query():
    # 測試有帶 q 參數
    response = client.get("/api/v1/keywords/search?q=AI")
    assert response.status_code == 200
    payload = response.json()
    assert "total" in payload
    assert payload["total"] == 3
    assert "results" in payload
    assert "AI Chip" in payload["results"]
    assert "AI Server" in payload["results"]
    assert "Edge AI" in payload["results"]

def test_keywords_search_without_query():
    # 測試沒有帶 q 參數，回傳全部
    response = client.get("/api/v1/keywords/search")
    assert response.status_code == 200
    payload = response.json()
    assert "total" in payload
    assert payload["total"] == 10
    assert len(payload["results"]) == 10
