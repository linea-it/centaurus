from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import relay, Schema, ObjectType, Field, String, Int
from schemas.product_class import ProductClass
from schemas.product_type import ProductType
from models import ProductClass as ProductClassModel

class Query(ObjectType):
    """Query objects for GraphQL API"""

    node = relay.Node.Field()
    product_type = relay.Node.Field(ProductType)
    product_type_list = SQLAlchemyConnectionField(ProductType)
    product_class = relay.Node.Field(ProductClass)
    product_class_list = SQLAlchemyConnectionField(ProductClass)

    product_class_by_display_name = Field(lambda: ProductClass, displayName=String())

    def resolve_product_class_by_display_name(self, info, displayName):
       query = ProductClass.get_query(info)
       return query.filter(ProductClassModel.display_name == displayName).first()

schema = Schema(query=Query)
