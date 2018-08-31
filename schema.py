import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import ProductClass


class Test(SQLAlchemyObjectType):
    class Meta:
        model = ProductClass
        interfaces = (relay.Node, )


class TestConnection(relay.Connection):
    class Meta:
        node = Test

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_tests = SQLAlchemyConnectionField(TestConnection)

schema = graphene.Schema(query=Query, types=[Test])
