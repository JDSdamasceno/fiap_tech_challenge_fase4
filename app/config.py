import os
from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = "Tech Challenge - Stock Forecast API"
    VERSION: str = os.getenv("API_VERSION", "v1")
    MODEL_VERSION: str = os.getenv("MODEL_VERSION", "v1")


settings = Settings()
