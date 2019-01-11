from graphene import Int, String, Field, DateTime, ObjectType, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import func, or_
from database import db_session

from models import (
    Pipelines as PipelinesModel,
    ProcessPipeline as ProcessPipelineModel,
    Processes as ProcessesModel,
    ProcessFields as ProcessFieldsModel,
    Fields as FieldsModel,
    ProcessStatus as ProcessStatusModel
)

from views import PipelinesExecution as PipelinesExecutionModel

import os

instance = os.getenv('API_INSTANCE')


class ProcessExecutionNode(ObjectType):
    """Process execution node"""
    process_count = Int()
    last_process_id = Int()
    start_time = DateTime()
    end_time = DateTime()
    status = String()


class PipelinesExecutionAttribute():
    pipeline_id = Int(description="Pipeline unique ID number")
    display_name = String()
    name = String()
    pipeline_stage_id = Int()
    field_id = Int()
    process = Field(ProcessExecutionNode)


class PipelinesExecution(SQLAlchemyObjectType, PipelinesExecutionAttribute):
    """Pipelines execution node"""

    class Meta:
        model = PipelinesExecutionModel
        interfaces = (relay.Node,)

    def resolve_process(self, info):

        subproc = db_session.query(
            PipelinesModel.pipeline_id,
            func.count(func.distinct(ProcessesModel.process_id)).label('process_count'),
            func.max(ProcessesModel.process_id).label('last_process_id')
        ).filter_by(
            pipeline_stage_id=self.pipeline_stage_id
        ).filter_by(
            pipeline_id=self.pipeline_id
        ).join(
            PipelinesModel.processes
        ).filter_by(
            flag_removed=False, instance=instance
        ).outerjoin(
            ProcessesModel.fields
        ).filter_by(
            field_id=self.field_id
        ).group_by(
            PipelinesModel.pipeline_id
        ).subquery()

        proc = db_session.query(
            ProcessesModel.start_time,
            ProcessesModel.end_time,
            ProcessStatusModel.name.label('status'),
            subproc.c.process_count,
            subproc.c.last_process_id
        ).join(
            subproc, ProcessesModel.process_id == subproc.c.last_process_id
        ).join(
            ProcessStatusModel
        ).one_or_none()

        procexec = proc._asdict() if proc else {}

        return ProcessExecutionNode(**procexec)
