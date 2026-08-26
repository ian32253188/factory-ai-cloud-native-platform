from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Factory AI Cloud-Native Platform"
    app_version: str = "0.1.0"
    environment: str = "development"

    model_config = SettingsConfigDict(
        env_prefix="FACTORY_",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
