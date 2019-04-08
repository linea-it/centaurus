from graphene import Int, String, Boolean, Field, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from utils import Connection

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
    data_type = String()


class Products(SQLAlchemyObjectType, ProductsAttribute):
    """Products node"""

    class Meta:
        model = ProductsModel
        interfaces = (relay.Node,)
        connection_class = Connection


    def resolve_data_type(self, info):
        """ Returns data type of the product """

        data_type = 'Table'

        if self.file_id:
            data_type = 'File'

        return data_type
