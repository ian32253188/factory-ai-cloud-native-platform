from fastapi import APIRouter
from factory_api.api.v1 import health

api_router = APIRouter()

# Root-level probes for Kubernetes compatibility (/healthz, /readyz)
api_router.include_router(health.router)

# Versioned API routes (/api/v1/...)
v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(health.router, prefix="/health")

# Future domain routers (Day 3+):
# v1_router.include_router(sensors.router, prefix="/sensors", tags=["Sensors"])
# v1_router.include_router(readings.router, prefix="/readings", tags=["Readings"])
# v1_router.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])

api_router.include_router(v1_router)
