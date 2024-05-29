from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


POSTGRES_URL = (f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
                f"@{settings.POSTGRES_HOSTNAME}/{settings.POSTGRES_DB}")

engine = create_engine(POSTGRES_URL)
Session = sessionmaker(autoflush=False, bind=engine)
