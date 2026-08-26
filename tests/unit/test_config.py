import os
from factory_api.config import Settings


def test_default_settings():
    """Test default settings initialization."""
    settings = Settings()
    assert settings.APP_NAME == "Factory AI Platform API"
    assert settings.APP_VERSION == "0.1.0"
    assert settings.API_V1_PREFIX == "/api/v1"
    assert settings.PORT == 8000
    assert settings.DEBUG is False


def test_settings_environment_override(monkeypatch):
    """Test environment variable overrides on settings."""
    monkeypatch.setenv("ENV", "production")
    monkeypatch.setenv("PORT", "9000")
    monkeypatch.setenv("LOG_LEVEL", "WARNING")

    settings = Settings()
    assert settings.ENV == "production"
    assert settings.PORT == 9000
    assert settings.LOG_LEVEL == "WARNING"
