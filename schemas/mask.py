from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Mask as MaskModel


class MaskAttribute():

    mask_id = Int()
    filter = String()
    date = DateTime()
    flag_removed = Boolean()
    tag_id = Int()
    field_id = Int()
    table_id = Int()


class Mask(SQLAlchemyObjectType, MaskAttribute):
    """Mask node"""

    class Meta:
        model = MaskModel
        interfaces = (relay.Node,)