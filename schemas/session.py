from graphene import Int, String, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Session as SessionModel


class SeesionAttribute():
    session_id = String()
    data = String()
    expiration_time = DateTime()
    user_id = Int()
    tg_session = String()


class Session(SQLAlchemyObjectType, SeesionAttribute):
    """Session node"""

    class Meta:
        model = SessionModel
        interfaces = (relay.Node,)