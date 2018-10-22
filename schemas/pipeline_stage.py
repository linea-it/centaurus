from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import PipelineStage as PipelineStageModel


class PipelineStageAttribute():
    pipeline_stage_id = Int()
    name = String()
    display_name = String()
    level = Int()


class PipelineStage(SQLAlchemyObjectType, PipelineStageAttribute):
    """PipelineStage node"""

    class Meta:
        model = PipelineStageModel
        interfaces = (relay.Node,)