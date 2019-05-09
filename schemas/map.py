from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models
import schemas

import utils


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
    data_loader_table = utils.DataLoaderOneToOne(models.Map, models.Tables)
    data_loader_tag = utils.DataLoaderOneToOne(models.Map, models.ReleaseTag)

    def resolve_table(self, info):
        return Map.data_loader_table.load(self.map_id)

    def resolve_tag(self, info):
        return Map.data_loader_tag.load(self.map_id)

    class Meta:
        model = models.Map
        interfaces = (relay.Node,)
