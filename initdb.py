# coding: utf-8
from sqlalchemy import DDL, event
from database import engine, db_session, Base
from sqlalchemy import Table
from sqlalchemy.sql import text
from sqlalchemy_views import CreateView

import json

from models import (
    ProductType, ProductClass, FileMimetype, GroupPypelines,
    PipelineStage, PipelineStatus, ProcessStatus, ProcessingSite,
    Tables, TgUser, FileLocator, Modules, Pipelines, Session,
    PipelinesConfig, Processes, ProcessPipeline, JobRuns,
    Products, ProcessProducts, ReleaseTag, Fields, ProcessFields,
    PipelinesModules, ProcessComponent
)

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
    Products, ProcessProducts, ReleaseTag, Fields, ProcessFields,
    PipelinesModules, ProcessComponent
]

for item in classes:
    if not has_table(item.__tablename__, item.__table__.schema):
        item.metadata.create_all(bind=engine, tables=[item.__table__])
        ingest_json(item)


# view created to show information about general pipelines execution
view = Table('vw_pipelines_execution', Base.metadata)

definition = text(str(
    "SELECT DISTINCT pipelines.pipeline_id, "
    "pipelines.display_name, "
    "pipelines.name, "
    "pipelines.pipeline_stage_id, "
    "coadd.process_fields.field_id, "
    "processes.instance "
    "FROM pipelines "
    "INNER JOIN process_pipeline ON pipelines.pipeline_id = process_pipeline.pipeline_id "
    "INNER JOIN processes ON processes.process_id = process_pipeline.process_id "
    "LEFT JOIN coadd.process_fields ON coadd.process_fields.process_id = processes.process_id"
))

vw_pipelines_execution = CreateView(view, definition, or_replace=True)
vw_pipelines_execution.compile()
engine.execute(vw_pipelines_execution)