from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Map as MapModel


class MapAttribute():

    map_id = Int()
    nside = Int()
    ordering = String()
    image = String()
    snr = Int()
    type = String()
    magnitude = String()
    filter = String()
    date = DateTime()
    flag_removed = Boolean()
    tag_id = Int()
    field_id = Int()
    table_id = Int()


class Map(SQLAlchemyObjectType, MapAttribute):
    """Map node"""

    class Meta:
        model = MapModel
        interfaces = (relay.Node,)