from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import PipelineStatus as PipelineStatusModel


class PipelineStatusAttribute():
    pipeline_status_id = Int()
    name = String()
    display_name = String()


class PipelineStatus(SQLAlchemyObjectType, PipelineStatusAttribute):
    """PipelineStatus node"""

    class Meta:
        model = PipelineStatusModel
        interfaces = (relay.Node,)