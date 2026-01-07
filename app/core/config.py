#app/core/config.py

from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Echo 2 Speak"
    # 나중에 FIREBASE 설정 등 추가

settings = Settings()
