import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Test as TestModel


class Test(SQLAlchemyObjectType):
    class Meta:
        model = TestModel
        interfaces = (relay.Node, )


class TestConnection(relay.Connection):
    class Meta:
        node = Test

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_tests = SQLAlchemyConnectionField(TestConnection)

schema = graphene.Schema(query=Query, types=[Test])
