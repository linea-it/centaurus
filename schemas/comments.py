from graphene import Int, String, DateTime, Float, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Comments as CommentsModel


class CommentsAttribute():
    comment_id = Int()
    comments = String()
    process_id = Int()
    date = DateTime()
    user_id = Int()
    hid = Float()
    hid_title = String()


class Comments(SQLAlchemyObjectType, CommentsAttribute):
    """Comments node"""

    class Meta:
        model = CommentsModel
        interfaces = (relay.Node,)