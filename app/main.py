from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.api.health import router as health_router
from app.api.market import router as market_router
from app.api.billing import router as billing_router
from app.api.reports import router as reports_router
from app.api.keywords import router as keywords_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
    )

    # Register API Routers
    app.include_router(health_router)
    app.include_router(market_router)
    app.include_router(billing_router)
    app.include_router(reports_router)
    app.include_router(keywords_router)

    # Mount Static Files for Web SaaS Dashboard
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    if os.path.exists(static_dir):
        app.mount("/static", StaticFiles(directory=static_dir), name="static")

    @app.get("/", include_in_schema=False)
    def root():
        index_file = os.path.join(static_dir, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"message": "Market Intelligence Cloud-Native SaaS API Online"}

    return app


app = create_app()
