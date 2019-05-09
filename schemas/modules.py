from graphene import Int, Float, String, Boolean, DateTime, relay, Field
from graphene_sqlalchemy import SQLAlchemyObjectType

import models
from schemas.tg_user import TgUser

import utils


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
    data_loader = utils.DataLoaderOneToOne(models.Modules, models.TgUser)

    def resolve_user(self, info):
        return Modules.data_loader.load(self.module_id)

    class Meta:
        model = models.Modules
        interfaces = (relay.Node,)