# coding: utf-8

from database import Base, engine
from sqlalchemy import PrimaryKeyConstraint, ForeignKeyConstraint


class PipelinesExecution(Base):
    __tablename__ = "vw_pipelines_execution"
    __table_args__ = (
        PrimaryKeyConstraint('pipeline_id', name='vw_pipelines_execution_pk'),
        ForeignKeyConstraint(['pipeline_id'], ['pipelines.pipeline_id']),
        {'autoload':True, 'autoload_with': engine, 'extend_existing': True}
    )
