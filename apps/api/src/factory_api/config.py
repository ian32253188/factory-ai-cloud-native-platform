from functools import lru_cache
from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Environment & Info
    ENV: str = Field(default="development", description="Runtime environment: development | test | production")
    APP_NAME: str = Field(default="Factory AI Platform API", description="Application name")
    APP_VERSION: str = Field(default="0.1.0", description="Application release version")
    DEBUG: bool = Field(default=False, description="Debug mode")

    # Server configuration
    HOST: str = Field(default="0.0.0.0", description="Bind host")
    PORT: int = Field(default=8000, description="Bind port")
    API_V1_PREFIX: str = Field(default="/api/v1", description="Prefix for V1 API routes")

    # Logging
    LOG_LEVEL: str = Field(default="INFO", description="Logging level: DEBUG | INFO | WARNING | ERROR")

    # Security & CORS
    CORS_ORIGINS: List[str] = Field(
        default=["*"],
        description="Allowed CORS origin URLs",
    )

    # Database (prepared for Days 4+)
    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./factory_dev.db",
        description="SQL Database connection URL",
    )


@lru_cache()
def get_settings() -> Settings:
    """Return cached application settings singleton."""
    return Settings()
