from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Fields as FieldsModel


class FieldsAttribute():

    field_id = Int(description='Field ID')
    field_name = String(description='Field name')
    display_name = String(description='Field ID')
    install_date = DateTime(description='Instalation date')
    release_date = DateTime(description='Release date')
    status = Boolean(description='Field status: true = available / false = unavailable')
    start_date = DateTime(description='Start date')
    discovery_date = DateTime(description='Discovery date')
    release_tag_id = Int(description='Release ID')


class Fields(SQLAlchemyObjectType, FieldsAttribute):
    """Fields node"""

    class Meta:
        model = FieldsModel
        interfaces = (relay.Node,)