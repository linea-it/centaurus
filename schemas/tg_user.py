from graphene import Int, String, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import TgUser as TgUserModel


class TgUserAttribute():
    user_id = Int()
    user_name = String()
    email_address = String()
    display_name = String()
    created = DateTime()
    affiliation = String()
    status = String()
    url_photo = String()
    about = String()


class TgUser(SQLAlchemyObjectType, TgUserAttribute):
    """TgUser node"""

    class Meta:
        model = TgUserModel
        interfaces = (relay.Node,)