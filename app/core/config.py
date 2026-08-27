from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Market Intelligence Cloud-Native SaaS Platform"
    app_version: str = "0.2.0"
    environment: str = "development"

    # Stripe & Billing Configuration
    stripe_public_key: str = "pk_test_market_intel_mock_key"
    stripe_secret_key: str = "sk_test_market_intel_mock_key"

    # Default Tenant Quotas (API Requests per month)
    free_tier_quota: int = 100
    pro_tier_quota: int = 10000
    enterprise_tier_quota: int = 1000000

    model_config = SettingsConfigDict(
        env_prefix="MARKET_",
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
