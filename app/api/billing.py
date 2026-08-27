from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from app.core.auth import generate_new_api_key, get_current_tenant
from app.core.config import settings
from app.models.market import SubscriptionPlanInfo, SubscriptionTier, Tenant

router = APIRouter(prefix="/api/v1/billing", tags=["SaaS Billing & Subscriptions"])


PLANS = [
    SubscriptionPlanInfo(
        tier=SubscriptionTier.FREE,
        name="Free Tier (免費試用版)",
        price_usd_monthly=0.0,
        quota_limit=settings.free_tier_quota,
        features=[
            "每月 100 次 API 查詢",
            "追蹤最多 3 個市場關鍵字",
            "基礎網路公開聲量統計"
        ]
    ),
    SubscriptionPlanInfo(
        tier=SubscriptionTier.PRO,
        name="Pro Tier (專業分析師版)",
        price_usd_monthly=49.0,
        quota_limit=settings.pro_tier_quota,
        features=[
            "每月 10,000 次 API 查詢",
            "追蹤最多 50 個品牌/競品關鍵字",
            "即時負面輿情危機告警 (Slack/Email)",
            "專屬 B2B API Key 授權",
            "全方位社群與電商聲量大數據"
        ]
    ),
    SubscriptionPlanInfo(
        tier=SubscriptionTier.ENTERPRISE,
        name="Enterprise Tier (企業旗艦版)",
        price_usd_monthly=299.0,
        quota_limit=settings.enterprise_tier_quota,
        features=[
            "無限量 API 數據查詢 (1,000,000+)",
            "無限關鍵字追蹤與客製化網路爬蟲 Pipeline",
            "一鍵導出 PDF 高管商業市場研報",
            "專屬 Docker / Kubernetes 獨立私有雲部署",
            "7x24 SRE 專人營運與 99.9% SLO 服務保證"
        ]
    )
]


class SubscriptionRequest(BaseModel):
    target_tier: SubscriptionTier


@router.get("/plans", response_model=List[SubscriptionPlanInfo])
def get_plans():
    return PLANS


@router.get("/usage")
def get_tenant_usage(tenant: Tenant = Depends(get_current_tenant)):
    return {
        "tenant_id": tenant.id,
        "tenant_name": tenant.name,
        "plan": tenant.plan,
        "api_key": tenant.api_key,
        "usage_count": tenant.usage_count,
        "quota_limit": tenant.quota_limit,
        "usage_percentage": round((tenant.usage_count / tenant.quota_limit) * 100, 1),
        "stripe_customer_id": f"cus_market_{tenant.id}"
    }


@router.post("/subscribe")
def subscribe_plan(req: SubscriptionRequest, tenant: Tenant = Depends(get_current_tenant)):
    target = next((p for p in PLANS if p.tier == req.target_tier), None)
    if not target:
        raise HTTPException(status_code=400, detail="無效的訂閱方案。")

    tenant.plan = target.tier
    tenant.quota_limit = target.quota_limit
    new_api_key = generate_new_api_key(tenant)

    return {
        "success": True,
        "message": f"🎉 成功訂閱/升級至 {target.name}！您的每月 API 查詢配額已提升至 {target.quota_limit:,} 次。",
        "new_plan": tenant.plan,
        "new_quota_limit": tenant.quota_limit,
        "new_api_key": new_api_key,
        "stripe_checkout_url": f"https://checkout.stripe.com/pay/mock_market_session_{tenant.id}"
    }
