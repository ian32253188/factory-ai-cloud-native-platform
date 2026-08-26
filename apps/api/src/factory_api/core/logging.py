import logging
import sys
from factory_api.config import Settings


def setup_logging(settings: Settings) -> None:
    """Configure structured console logging for the application."""
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    log_format = "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
    if settings.DEBUG:
        log_format = "%(asctime)s [%(levelname)s] [%(name)s:%(lineno)d] %(message)s"

    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )

    # Silence overly verbose loggers in external packages if needed
    logging.getLogger("uvicorn.access").setLevel(log_level)
