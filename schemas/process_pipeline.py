from graphene import Int, String, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import ProcessPipeline as ProcessPipelineModel


class ProcessPipelineAttribute():
    process_id = Int()
    pipeline_id = Int()
    version = String()
    version_date = DateTime()


class ProcessPipeline(SQLAlchemyObjectType, ProcessPipelineAttribute):
    """Process Pipeline node"""


    class Meta:
        model = ProcessPipelineModel
        interfaces = (relay.Node,)
