from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine(
    os.environ.get('DATABASE_URI', 'sqlite:///:memory:'),
    convert_unicode=True,
    echo=False
)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()
# Base.metadata.reflect(engine)