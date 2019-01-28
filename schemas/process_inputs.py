from graphene import Int, String, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import ProcessInputs as ProcessInputsModel


class ProcessInputsAttribute():
    process_id = Int()
    product_id = Int()


class ProcessInputs(SQLAlchemyObjectType, ProcessInputsAttribute):
    """Process Inputs node"""


    class Meta:
        model = ProcessInputsModel
        interfaces = (relay.Node,)
