import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logging(
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> None:
    """
    Setup logging configuration for the project.

    Args:
        log_file: Optional path to log file. If None, logs only to console
        level: Logging level (default: logging.INFO)
        log_format: Format string for log messages
    """
    # Create logs directory if logging to file
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

    # Basic configuration
    handlers = []

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)

    # File handler if log_file specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(file_handler)

    # Configure root logger
    logging.basicConfig(level=level, handlers=handlers, format=log_format)
