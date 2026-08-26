from typing import Dict
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field
from factory_api.config import Settings, get_settings

router = APIRouter(tags=["Health & Probes"])


class HealthResponse(BaseModel):
    """Schema for process liveness check."""

    status: str = Field(default="ok", examples=["ok"], description="Process health status")
    version: str = Field(..., examples=["0.1.0"], description="API version")
    environment: str = Field(..., examples=["development"], description="Runtime environment")


class ReadinessResponse(BaseModel):
    """Schema for dependency readiness check."""

    status: str = Field(default="ready", examples=["ready"], description="Overall readiness status")
    checks: Dict[str, str] = Field(
        default_factory=dict,
        examples=[{"database": "ok", "storage": "ok"}],
        description="Individual dependency check results",
    )


@router.get(
    "/healthz",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Liveness Probe",
    description="Kubernetes liveness probe endpoint to check if the process is responsive.",
)
async def get_healthz(settings: Settings = Depends(get_settings)) -> HealthResponse:
    """Return process health status."""
    return HealthResponse(
        status="ok",
        version=settings.APP_VERSION,
        environment=settings.ENV,
    )


@router.get(
    "/readyz",
    response_model=ReadinessResponse,
    status_code=status.HTTP_200_OK,
    summary="Readiness Probe",
    description="Kubernetes readiness probe endpoint to check if all dependencies are ready to serve traffic.",
)
async def get_readyz() -> ReadinessResponse:
    """Return dependency readiness status."""
    # Future days will incorporate real DB/Redis connectivity tests
    return ReadinessResponse(
        status="ready",
        checks={
            "api_server": "ok",
        },
    )
