#app/core/config.py

# ❌ 기존에는 이렇게 되어 있었을 거야:
# from pydantic import BaseSettings

# ✅ Pydantic v2에서는 BaseSettings가 pydantic-settings 패키지로 분리됨
from pydantic_settings import BaseSettings  # <-- 여기만 핵심 수정

class Settings(BaseSettings):
    PROJECT_NAME: str = "Echo 2 Speak"
    # 나중에 FIREBASE 설정 등 추가 예정
    # 예: FIREBASE_PROJECT_ID: str | None = None

# settings 인스턴스를 한 번 만들어서 다른 곳에서 import 해서 쓰도록 함
settings = Settings()
