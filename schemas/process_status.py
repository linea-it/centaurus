from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import ProcessStatus as ProcessStatusModel


class ProcessStatusAttribute():
    process_status_id = Int()
    name = String()
    display_name = String()


class ProcessStatus(SQLAlchemyObjectType, ProcessStatusAttribute):
    """Process Status node"""


    class Meta:
        model = ProcessStatusModel
        interfaces = (relay.Node,)
