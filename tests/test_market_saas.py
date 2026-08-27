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
from app.services.ai_sentiment import ai_sentiment

def test_ai_sentiment_engine_critical_threshold():
    # 模擬高負面聲量數據
    mock_data = {
        "keyword": "測試產品",
        "sentiment_breakdown": {
            "sentiment_index": 0.05,
            "negative_pct": 30.0
        }
    }
    status, score, label, advice = ai_sentiment.analyze_market_trend(mock_data)
    
    # 驗證 AI 引擎是否能精準觸發公關危機警告
    assert status == "critical"
    assert "公關危機警告" in label
