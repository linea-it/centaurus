# coding: utf-8
from sqlalchemy import DDL, event
from database import engine, db_session, Base

from models import (
    ProductType, ProductClass, FileMimetype, GroupPypelines,
    PipelineStage, PipelineStatus, ProcessStatus, ProcessingSite,
    Tables, TgUser, FileLocator, Modules, Pipelines, Session,
    PipelinesConfig, Processes, ProcessPipeline, JobRuns,
    Products, ReleaseTag, Fields, PipelinesModules
)
import json

event.listen(
    Base.metadata, 'before_create',
    DDL("CREATE SCHEMA IF NOT EXISTS coadd")
)


def has_table(tablename, schema=None):
    """ Check if the table exists in the database
    
    Arguments:
        tablename {str} -- table name
        schema {str} -- schema name
    
    Returns:
        boolean -- True has table, False not has table
    """
            
    return engine.dialect.has_table(engine, tablename, schema)


def ingest_json(class_table):
    """ Ingest tests json in database
    
    Arguments:
        class_table {class} -- sqlalchemy model (DeclarativeMeta)
    """


    with open('{}/{}.json'.format(
       'tests/data', class_table.__tablename__
    )) as json_file:
        data = json.load(json_file)

    db_session.bulk_insert_mappings(
        class_table, [dict(i) for i in data]
    )
    db_session.commit()


classes = [
    ProductType, ProductClass, FileMimetype, GroupPypelines,
    PipelineStage, PipelineStatus, ProcessStatus, ProcessingSite,
    Tables, TgUser, FileLocator, Modules, Pipelines, Session,
    PipelinesConfig, Processes, ProcessPipeline, JobRuns,
    Products, ReleaseTag, Fields, PipelinesModules
]

for item in classes:
    if not has_table(item.__tablename__, item.__table__.schema):
        item.metadata.create_all(bind=engine, tables=[item.__table__])
        ingest_json(item)
