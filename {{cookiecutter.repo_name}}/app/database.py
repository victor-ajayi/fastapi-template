from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import settings

{% if cookiecutter.database == "SQLite" %}

SQLALCHEMY_DATABASE_URL = f"sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

{% else %}

{% if cookiecutter.database == "PostgreSQL" %}
SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL
{% else %}
SQLALCHEMY_DATABASE_URL = settings.DB_URL
{% endif %}

engine = create_engine(SQLALCHEMY_DATABASE_URL)

{% endif %}

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
