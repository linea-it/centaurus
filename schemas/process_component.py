from graphene import Int, String, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import ProcessComponent as ProcessComponentModel


class ProcessComponentAttribute():
    process_id = Int()
    module_id = Int()
    version = String()
    version_date = DateTime()


class ProcessComponent(SQLAlchemyObjectType, ProcessComponentAttribute):
    """Process Component node"""


    class Meta:
        model = ProcessComponentModel
        interfaces = (relay.Node,)
