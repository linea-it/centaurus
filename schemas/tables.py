from graphene import String, Int, Field, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from schemas.catalog import Catalog
from schemas.map import Map
from schemas.mask import Mask

from models import (
    Tables as TablesModel
)
import os

DACHS_URL = os.getenv('DACHS_URL')


class TablesAttribute():
    table_id = Int()
    schema_name = String()
    table_name = String()
    dachs_url = String()
    catalog = Field(lambda: Catalog)
    mask = Field(lambda: Mask)
    map = Field(lambda: Map)

class Tables(SQLAlchemyObjectType, TablesAttribute):
    """Tables node"""

    class Meta:
        model = TablesModel
        interfaces = (relay.Node,)


    def resolve_dachs_url(self, info):
        """ Mount link to DACHS service """

        return os.path.join(
            DACHS_URL,
            "%(schema)s/%(table)s/q/form" % {
                "schema": self.schema_name,
                "table": self.table_name
            }
        )