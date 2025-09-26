from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

class TelegramConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="TG_")

    token: SecretStr



config = TelegramConfig()
