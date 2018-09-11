from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

port = os.environ.get('DB_PORT')
host = os.environ.get('DB_HOST')

if port:
    host = '{host}:{port}'.format({'host': host, 'port': port})

database_uri = 'postgresql://{user}:{pwd}@{host}/{db}'.format(**{
    'user': os.environ.get('POSTGRES_USER'),
    'pwd': os.environ.get('POSTGRES_PASSWORD'),
    'host': host,
    'db': os.environ.get('POSTGRES_DB')
})

engine = create_engine(database_uri, convert_unicode=True, echo=False)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()
