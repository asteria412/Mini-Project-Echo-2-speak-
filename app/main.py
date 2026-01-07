#app/main.py

from fastapi import FastAPI
from app.core.config import settings
from app.api import health

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(health.router)
