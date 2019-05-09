from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models
import schemas

import utils


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
    data_loader_table = utils.DataLoaderOneToOne(models.Mask, models.Tables)
    data_loader_tag = utils.DataLoaderOneToOne(models.Mask, models.ReleaseTag)
    data_loader_field = utils.DataLoaderOneToOne(models.Mask, models.Fields)

    def resolve_table(self, info):
        return Mask.data_loader_table.load(self.mask_id)

    def resolve_tag(self, info):
        return Mask.data_loader_tag.load(self.mask_id)

    def resolve_field(self, info):
        return Mask.data_loader_field.load(self.mask_id)

    class Meta:
        model = models.Mask
        interfaces = (relay.Node,)
