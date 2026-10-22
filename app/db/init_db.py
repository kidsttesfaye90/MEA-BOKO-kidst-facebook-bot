from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.base import Base
from app.db.session import engine
from app.db.models import User  # noqa: F401


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def db_healthcheck(db: Session) -> bool:
    try:
        db.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
