from logging import _nameToLevel as valid_log_levels
from typing import Any

import yaml
from loguru import logger
from pydantic import BaseModel, validator


class AppConfig(BaseModel):
    """Application specific configuration."""
    crontab_path: str  # Path to the crontab file.


class LoggerConfig(BaseModel):
    """Logging specific configuration."""
    level: str
    file_path: str  # File path to output logs.

    @validator('level')
    @classmethod
    def is_valid_log_level(cls, level: str) -> str:
        """Validator to ensure log level is valid."""
        if level not in valid_log_levels:
            valid_levels = ', '.join(valid_log_levels.keys())
            raise ValueError(f'Invalid log level: {level}. Expected one of: {valid_levels}')
        return level


class Config(BaseModel):
    """Main configuration model combining all settings."""
    app: AppConfig
    logger: LoggerConfig

    @classmethod
    def load(cls, path: str) -> 'Config':
        """Loads configuration from a YAML file."""
        logger.debug(f"Trying load config from '{path}'.")

        try:
            with open(path, 'r', encoding='utf-8') as file:
                yml = yaml.safe_load(file)
        except FileNotFoundError as error:
            logger.error(f"Configuration file not found: {error}")
            raise

        logger.debug("Application config loaded successfully.")
        return cls(**yml)

    def configure_logger(self) -> None:
        """Configures the logger based on the loaded settings."""
        logger.add(self.logger.file_path, level=self.logger.level.upper())

