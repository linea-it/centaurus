from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models


class ProductTypeAttribute():
    type_id_seq = Int(description="Product type unique id number")
    type_id = Int(description="Product type id number")
    type_name = String(description="Name of the type")
    display_name = String(description="Name displayed of the type")


class ProductType(SQLAlchemyObjectType, ProductTypeAttribute):
    """Product Type node"""

    class Meta:
        model = models.ProductType
        interfaces = (relay.Node,)
