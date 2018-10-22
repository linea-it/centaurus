from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import PipelinesModules as PipelinesModulesModel


class PipelinesModulesAttribute():
    pipeline_id = Int(description="Pipeline unique ID number")
    module_id = Int(description="Module unique ID number")
    xml_config = String()

class PipelinesModules(SQLAlchemyObjectType, PipelinesModulesAttribute):
    """Pipelines modules node"""

    class Meta:
        model = PipelinesModulesModel
        interfaces = (relay.Node,)