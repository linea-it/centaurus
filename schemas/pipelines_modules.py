from graphene import Int, String, relay, Field
from graphene_sqlalchemy import SQLAlchemyObjectType

import models
from schemas.modules import Modules
from schemas.pipelines import Pipelines

import utils


class PipelinesModulesAttribute():
    pipeline_id = Int(description="Pipeline unique ID number")
    module_id = Int(description="Module unique ID number")
    xml_config = String()


class PipelinesModules(SQLAlchemyObjectType, PipelinesModulesAttribute):
    """Pipelines modules node"""
    data_loader_module = utils.DataLoaderOneToOne(
        models.PipelinesModules,
        models.Modules,
        pk_inner_model=models.PipelinesModules.module_id)
    data_loader_pipeline = utils.DataLoaderOneToOne(
        models.PipelinesModules,
        models.Pipelines,
        pk_inner_model=models.PipelinesModules.pipeline_id)

    def resolve_module(self, info):
        return PipelinesModules.data_loader_module.load(self.module_id)

    def resolve_pipeline(self, info):
        return PipelinesModules.data_loader_pipeline.load(self.pipeline_id)

    class Meta:
        model = models.PipelinesModules
        interfaces = (relay.Node,)