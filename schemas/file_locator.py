from graphene import Int, String, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import (
    FileLocator as FileLocatorModel
)


class FileLocatorAttribute():
    file_id = Int()
    uri = String()
    provenance_id = Int()
    survey_id = Int()
    category_id = Int()
    file_name = String()
    file_type_id = Int()
    namespace = String()


class FileLocator(SQLAlchemyObjectType, FileLocatorAttribute):
    """FileLocator node"""

    class Meta:
        model = FileLocatorModel
        interfaces = (relay.Node,)