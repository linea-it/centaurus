from graphene import String, Int, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import (
    Tables as TablesModel
)


class TablesAttribute():
    user_id = Int()
    user_name = String()
    email_address = String()
    display_name = String()
    created = DateTime()
    affiliation = String()
    status = String()
    url_photo = String()
    about = String()


class Tables(SQLAlchemyObjectType):
    """Tables node"""

    class Meta:
        model = TablesModel
        interfaces = (relay.Node,)