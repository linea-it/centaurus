from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

from sqlalchemy.engine import Engine
import time
import logging

logging.basicConfig()
logger = logging.getLogger("centarus")
logger.setLevel(logging.DEBUG)

@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    logger.debug("-" * 40)
    logger.debug("START query: %s", statement)
    logger.debug("parameters: %s", parameters)

@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    logger.debug("END query ~ runtime: %f", total)

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
