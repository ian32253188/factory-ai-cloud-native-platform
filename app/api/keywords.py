from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/api/v1/keywords", tags=["keywords"])

# 記憶體內的關鍵字列表（模擬資料庫）
KEYWORDS_DB = [
    "AI Chip",
    "Cloud Native",
    "AI Server",
    "SaaS Platform",
    "Edge AI",
    "Kubernetes",
    "Machine Learning",
    "DevOps",
    "MLOps",
    "Microservices"
]

@router.get("/search")
def search_keywords(q: Optional[str] = None) -> dict:
    """
    搜尋市場關鍵字。
    支援 Query Parameter: ?q=關鍵字
    """
    # 如果有傳入 q，則進行不區分大小寫的模糊搜尋
    if q:
        matched_keywords = [
            kw for kw in KEYWORDS_DB if q.lower() in kw.lower()
        ]
    else:
        # 如果未傳入 q，則回傳全部
        matched_keywords = KEYWORDS_DB

    return {
        "total": len(matched_keywords),
        "results": matched_keywords
    }
