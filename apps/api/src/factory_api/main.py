import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from factory_api import __version__
from factory_api.api.router import api_router
from factory_api.config import Settings, get_settings
from factory_api.core.logging import setup_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifecycle management for startup and shutdown events."""
    settings = get_settings()
    setup_logging(settings)
    logger.info(
        "Starting %s v%s in %s mode",
        settings.APP_NAME,
        settings.APP_VERSION,
        settings.ENV,
    )
    yield
    logger.info("Shutting down %s", settings.APP_NAME)


def create_app(settings: Settings | None = None) -> FastAPI:
    """FastAPI application factory."""
    if settings is None:
        settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=__version__,
        description=(
            "Cloud-native Factory AI Monitoring Platform API. "
            "Provides sensor ingestion, telemetry analytics, alert pipelines, and ML inference."
        ),
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # CORS configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routes
    app.include_router(api_router)

    return app


# Default application instance for Uvicorn
app = create_app()
