from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_keywords_list():
    response = client.get("/api/v1/market/keywords")
    assert response.status_code == 200
    keywords = response.json()
    assert len(keywords) >= 3
    assert keywords[0]["id"] == "K-001"


def test_sentiment_analysis_endpoint():
    response = client.get("/api/v1/market/sentiment/K-001")
    assert response.status_code == 200
    data = response.json()
    assert "sentiment_index" in data
    assert "health_label" in data
    assert "ai_advice" in data


def test_billing_plans():
    response = client.get("/api/v1/billing/plans")
    assert response.status_code == 200
    plans = response.json()
    assert len(plans) == 3
    tiers = [p["tier"] for p in plans]
    assert "free" in tiers
    assert "pro" in tiers
    assert "enterprise" in tiers


def test_subscribe_plan():
    response = client.post("/api/v1/billing/subscribe", json={"target_tier": "pro"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["new_plan"] == "pro"


def test_report_html_generation():
    response = client.get("/api/v1/reports/html/K-001")
    assert response.status_code == 200
    assert "Market AI 商業市場調查研報" in response.text
