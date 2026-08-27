from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field


class SubscriptionTier(str, Enum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class SentimentCategory(str, Enum):
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"


class SentimentBreakdown(BaseModel):
    positive_pct: float
    neutral_pct: float
    negative_pct: float
    score: float  # Composite Sentiment Index (-1.0 to 1.0)


class MarketKeyword(BaseModel):
    id: str
    keyword: str
    category: str
    mentions_count: int
    sentiment_score: float
    status: str = "tracking"
    last_updated: datetime = Field(default_factory=datetime.utcnow)


class Tenant(BaseModel):
    id: str
    name: str
    plan: SubscriptionTier = SubscriptionTier.FREE
    api_key: str
    usage_count: int = 0
    quota_limit: int = 100
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SubscriptionPlanInfo(BaseModel):
    tier: SubscriptionTier
    name: str
    price_usd_monthly: float
    quota_limit: int
    features: List[str]
