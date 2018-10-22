from graphene import Int, Float, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Modules as ModulesModel
# from schemas.tg_user import TgUser
# from schemas.pipelines_modules import PipelinesModules


class ModulesAttribute():
    module_id = Int()
    name = String()
    version = String()
    display_name = String()
    xml_config = String()
    description = String()
    version_date = DateTime()
    grade = Float()
    user_id = Int()


class Modules(SQLAlchemyObjectType, ModulesAttribute):
    """Modules node"""

    class Meta:
        model = ModulesModel
        interfaces = (relay.Node,)