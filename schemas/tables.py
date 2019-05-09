from graphene import String, Int, Field, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import schemas
import models

import os

DACHS_URL = os.getenv('DACHS_URL')


class TablesAttribute():
    table_id = Int()
    schema_name = String()
    table_name = String()
    dachs_url = String()
    catalog = Field(lambda: schemas.catalog.Catalog)
    mask = Field(lambda: schemas.mask.Mask)
    map = Field(lambda: schemas.map.Map)

class Tables(SQLAlchemyObjectType, TablesAttribute):
    """Tables node"""

    class Meta:
        model = models.Tables
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