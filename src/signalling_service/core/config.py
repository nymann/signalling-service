from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from signalling_service.version import __version__


class Config(BaseSettings):
    title: str = "Signalling Service"
    version: str = __version__
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )
