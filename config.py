from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ADMIN_ID: int
    TELEGRAM_BOT_TOKEN: str

    class Config:
        env_prefix = ""

settings = Settings()