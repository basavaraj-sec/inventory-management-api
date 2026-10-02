from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import (
    DATABASE_TYPE,
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_DRIVER,
)


def build_database_url() -> str:
    if DATABASE_TYPE == "sqlite":
        if DATABASE_NAME == ":memory:":
            return "sqlite:///:memory:"

        return f"sqlite:///{DATABASE_NAME}"

    if DATABASE_TYPE in {"mysql", "postgresql"}:
        driver = f"+{DATABASE_DRIVER}" if DATABASE_DRIVER else ""

        return (
            f"{DATABASE_TYPE}{driver}://"
            f"{DATABASE_USER}:{DATABASE_PASSWORD}"
            f"@{DATABASE_HOST}:{DATABASE_PORT}"
            f"/{DATABASE_NAME}"
        )

    raise ValueError(
        f"Unsupported database type: {DATABASE_TYPE}"
    )


DATABASE_URL = build_database_url()


if DATABASE_TYPE == "sqlite" and DATABASE_NAME == ":memory:":
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
elif DATABASE_TYPE == "sqlite":
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()