from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .config import settings

class Base(DeclarativeBase):
    ...

engine = create_engine(f'postgresql://{settings.postgres_user}:{settings.postgres_password}@localhost/{settings.postgres_db}')
local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
