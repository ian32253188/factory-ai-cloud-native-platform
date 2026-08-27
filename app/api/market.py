from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.core.auth import check_and_increment_quota, get_current_tenant
from app.models.market import MarketKeyword, Tenant
from app.services.ai_sentiment import ai_sentiment
from app.services.market_scraper import market_scraper

router = APIRouter(prefix="/api/v1/market", tags=["Market Intelligence APIs"])

# Default Keywords Store
keywords_db: List[MarketKeyword] = [
    MarketKeyword(id="K-001", keyword="電動車 AI 輔助駕駛 (Autonomous Driving)", category="汽車科技", mentions_count=6420, sentiment_score=0.58),
    MarketKeyword(id="K-002", keyword="折疊螢幕旗艦手機 (Foldable Smartphone)", category="消費電子", mentions_count=4180, sentiment_score=0.32),
    MarketKeyword(id="K-003", keyword="生成式 AI 辦公助理 (Generative AI Copilot)", category="企業軟體", mentions_count=8950, sentiment_score=0.67),
    MarketKeyword(id="K-004", keyword="無添加燕麥奶咖啡 (Oat Milk Coffee)", category="餐飲保健", mentions_count=2150, sentiment_score=0.12)
]


@router.get("/keywords", response_model=List[MarketKeyword])
def list_market_keywords(tenant: Tenant = Depends(get_current_tenant)):
    """
    取得目前正在追蹤的商業熱門關鍵字與市場聲量概況。
    """
    return keywords_db


@router.get("/sentiment/{keyword_id}")
def analyze_keyword_sentiment(keyword_id: str, tenant: Tenant = Depends(get_current_tenant)):
    """
    【付費計費 API 端點】調用 AI 進行網路公開數據抓取與市場聲量/情感分析。
    """
    kw = next((k for k in keywords_db if k.id == keyword_id), None)
    if not kw:
        raise HTTPException(status_code=404, detail="找不到指定的市場關鍵字。")

    # Check quota
    check_and_increment_quota(tenant)

    # Scrape data & run AI analytics
    data = market_scraper.fetch_keyword_mentions(kw.keyword)
    status, sentiment_index, health_label, advice = ai_sentiment.analyze_market_trend(data)

    # Update keyword model
    kw.mentions_count = data["total_mentions"]
    kw.sentiment_score = sentiment_index

    return {
        "tenant_id": tenant.id,
        "keyword": kw.keyword,
        "category": kw.category,
        "status": status,
        "health_label": health_label,
        "sentiment_index": sentiment_index,
        "mentions_count": data["total_mentions"],
        "sentiment_breakdown": data["sentiment_breakdown"],
        "trending_topics": data["trending_topics"],
        "ai_advice": advice,
        "data_sources": data["sources"]
    }
