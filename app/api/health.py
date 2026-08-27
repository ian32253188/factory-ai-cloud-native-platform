from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.environment,
    }
from datetime import datetime
from typing import Optional

@router.get("/health/detail")
def detailed_health_check(verbose: bool = False) -> dict:
    """
    延伸端點：詳細健康檢查。
    支援 Query Parameter: ?verbose=true 或 ?verbose=false
    """
    response_data = {
        "status": "ok",
        "service": settings.app_name,
    }
    
    # 若使用者帶入 ?verbose=true，則補充詳細時間資訊
    if verbose:
        response_data["timestamp"] = datetime.utcnow().isoformat()
        response_data["environment"] = settings.environment
        response_data["mode"] = "verbose_diagnostic"

    return response_data
