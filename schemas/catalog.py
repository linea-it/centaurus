from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models
import schemas

import utils


class CatalogAttribute():

    catalog_id = Int()
    num_tiles = Int()
    num_objects = Int()
    num_columns = Int()
    visibility = Int()
    catalog_name = String()
    version = String()
    ingestion_date = DateTime()
    user_id = Int()
    description = String()
    status_id = Int()
    flag_removed = Boolean()
    table_id = Int()


class Catalog(SQLAlchemyObjectType, CatalogAttribute):
    """Catalog node"""
    data_loader_table = utils.DataLoaderOneToOne(models.Catalog, models.Tables)

    def resolve_table(self, info):
        return Catalog.data_loader_table.load(self.catalog_id)

    class Meta:
        model = models.Catalog
        interfaces = (relay.Node,)
