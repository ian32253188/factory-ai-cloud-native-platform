import pytest
from fastapi.testclient import TestClient
from app.core.config import Settings
from app.main import create_app

@pytest.fixture
def test_settings() -> Settings:
    """Provide isolated test settings."""
    return Settings(
        app_name="Factory AI Test API",
        environment="test",
    )

@pytest.fixture
def client(test_settings: Settings) -> TestClient:
    """Provide FastAPI test client fixture."""
    app = create_app()
    with TestClient(app) as test_client:
        yield test_client
