import os
import pytest
from fastapi.testclient import TestClient
from factory_api.config import Settings, get_settings
from factory_api.main import create_app


@pytest.fixture
def test_settings() -> Settings:
    """Provide isolated test settings."""
    return Settings(
        ENV="test",
        DEBUG=True,
        APP_NAME="Factory AI Test API",
        LOG_LEVEL="DEBUG",
        DATABASE_URL="sqlite+aiosqlite:///:memory:",
    )


@pytest.fixture
def client(test_settings: Settings) -> TestClient:
    """Provide FastAPI test client fixture."""
    app = create_app(settings=test_settings)
    app.dependency_overrides[get_settings] = lambda: test_settings
    with TestClient(app) as test_client:
        yield test_client
