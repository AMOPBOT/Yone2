from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from Yone import DB_URI, LOGGER as log

if DB_URI and DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    try:
        engine.connect()
    except Exception as e:
        log.error(f"Error connecting to the database: {e}")
        return None
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False,))


BASE = declarative_base()
SESSION = start()
