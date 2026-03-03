from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ADMIN_ID: int = Field()
    TELEGRAM_BOT_TOKEN: str = Field()

    class Config:
        env_file = ".env"

settings = Settings()