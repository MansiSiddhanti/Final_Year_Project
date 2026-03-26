from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./farmbuddy.db"

# DATABASE ENGINE
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SESSION
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# BASE MODEL
Base = declarative_base()


# ✅ DATABASE DEPENDENCY (THIS WAS MISSING)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()