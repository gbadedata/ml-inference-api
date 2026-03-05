from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "ML Inference API"
    app_version: str = "0.0.0"
    log_level: str = "INFO"
    model_path: str = "model/artifact/model.json"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()