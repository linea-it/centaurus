from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Catalog as CatalogModel


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

    class Meta:
        model = CatalogModel
        interfaces = (relay.Node,)