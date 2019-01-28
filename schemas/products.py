from graphene import Int, String, Boolean, Field, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import (
    Products as ProductsModel
)


class ProductsAttribute():
    product_id = Int()
    file_id = Int()
    job_id = Int()
    table_id = Int()
    class_id = Int()
    flag_removed = Boolean()
    display_name = String()
    version = Int()
    selected_name = String()


class Products(SQLAlchemyObjectType, ProductsAttribute):
    """Products node"""

    class Meta:
        model = ProductsModel
        interfaces = (relay.Node,)