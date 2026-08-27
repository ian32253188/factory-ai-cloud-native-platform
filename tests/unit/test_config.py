import os
from app.core.config import Settings


def test_default_settings():
    """Test default settings initialization."""
    settings = Settings()
    assert settings.app_name == "Market Intelligence Cloud-Native SaaS Platform"
    assert settings.app_version == "0.2.0"
    assert settings.environment == "development"
    assert settings.free_tier_quota == 100


def test_settings_environment_override(monkeypatch):
    """Test environment variable overrides on settings using MARKET_ prefix."""
    monkeypatch.setenv("MARKET_ENVIRONMENT", "production")
    monkeypatch.setenv("MARKET_APP_NAME", "Production Market API")
    monkeypatch.setenv("MARKET_FREE_TIER_QUOTA", "50")

    settings = Settings()
    assert settings.environment == "production"
    assert settings.app_name == "Production Market API"
    assert settings.free_tier_quota == 50
