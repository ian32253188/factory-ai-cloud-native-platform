from typing import Dict, Optional
import uuid
from fastapi import Header, HTTPException, status
from app.core.config import settings
from app.models.market import SubscriptionTier, Tenant

# In-memory demo tenant
DEFAULT_TENANT = Tenant(
    id="tenant_market_01",
    name="Vanguard Market Research Inc.",
    plan=SubscriptionTier.FREE,
    api_key="mk_live_demo_key_8899",
    usage_count=18,
    quota_limit=settings.free_tier_quota
)

tenants_db: Dict[str, Tenant] = {
    DEFAULT_TENANT.api_key: DEFAULT_TENANT
}


def get_current_tenant(x_api_key: Optional[str] = Header(None, alias="X-API-Key")) -> Tenant:
    if not x_api_key:
        return DEFAULT_TENANT

    tenant = tenants_db.get(x_api_key)
    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="無效的 API Key，請檢查授權標頭 X-API-Key。"
        )

    return tenant


def check_and_increment_quota(tenant: Tenant) -> None:
    if tenant.usage_count >= tenant.quota_limit:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=f"【用量配額已滿】您當前方案 ({tenant.plan.value.upper()}) 月配額上限為 {tenant.quota_limit} 次 API 呼叫，已全部用盡！請升級至 Pro 或 Enterprise 訂閱方案。"
        )
    tenant.usage_count += 1


def generate_new_api_key(tenant: Tenant) -> str:
    new_key = f"mk_{tenant.plan.value}_{uuid.uuid4().hex[:12]}"
    if tenant.api_key in tenants_db:
        del tenants_db[tenant.api_key]
    tenant.api_key = new_key
    tenants_db[new_key] = tenant
    return new_key
