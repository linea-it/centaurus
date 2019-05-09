from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models


class PipelineStageAttribute():
    pipeline_stage_id = Int()
    name = String()
    display_name = String()
    level = Int()


class PipelineStage(SQLAlchemyObjectType, PipelineStageAttribute):
    """PipelineStage node"""

    class Meta:
        model = models.PipelineStage
        interfaces = (relay.Node,)