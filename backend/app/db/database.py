from sqlalchemy import create_engine

from backend.app.core.config import settings


engine = create_engine(settings.database_url)