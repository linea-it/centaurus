from graphene import String, Float, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Filters as FiltersModel


class FiltersAttribute():
    filter = String()
    lambda_min = Float()
    lambda_max = Float()
    lambda_mean = Float()


class Filters(SQLAlchemyObjectType, FiltersAttribute):
    """Filters node"""

    class Meta:
        model = FiltersModel
        interfaces = (relay.Node,)