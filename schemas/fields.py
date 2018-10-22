from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Fields as FieldsModel


class FieldsAttribute():

    field_id = Int()
    field_name = String()
    display_name = String()
    install_date = DateTime()
    release_date = DateTime()
    status = Boolean()
    start_date = DateTime()
    discovery_date = DateTime()
    release_tag_id = Int()


class Fields(SQLAlchemyObjectType, FieldsAttribute):
    """Release Tag node"""

    class Meta:
        model = FieldsModel
        interfaces = (relay.Node,)