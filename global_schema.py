from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import Schema, ObjectType, Field, List, String, Int

from schemas.product_class import ProductClass
from schemas.product_type import ProductType
from schemas.tg_user import TgUser
from schemas.pipelines import Pipelines
from schemas.modules import Modules
from schemas.pipelines_modules import PipelinesModules
from schemas.pipeline_stage import PipelineStage
from schemas.group_pypelines import GroupPypelines
from schemas.release_tag import ReleaseTag
from schemas.fields import Fields
from schemas.pipeline_status import PipelineStatus

from models import ProductClass as ProductClassModel
from models import Pipelines as PipelinesModel
from models import Modules as ModulesModel
from models import Fields as FieldsModel


class Query(ObjectType):
    """Query objects for GraphQL API"""

    # gets all entries
    product_class_list = SQLAlchemyConnectionField(ProductClass)
    pipelines_list = SQLAlchemyConnectionField(Pipelines)
    modules_list = SQLAlchemyConnectionField(Modules)
    group_pypelines_list = SQLAlchemyConnectionField(GroupPypelines)
    pipelines_modules_list = SQLAlchemyConnectionField(PipelinesModules)
    release_tag_list = SQLAlchemyConnectionField(ReleaseTag)
    pipeline_stage_list = SQLAlchemyConnectionField(PipelineStage)

    # gets by field unique
    product_class_by_class_name = Field(lambda: ProductClass, name=String())
    pipelines_by_name = Field(lambda: Pipelines, name=String())
    modules_by_name = Field(lambda: Modules, name=String())

    # gets list by id 
    fields_by_tag_id = List(lambda: Fields, tag_id=Int())
    pipelines_by_stage_id = List(lambda: Pipelines, stage_id=Int())

    def resolve_pipelines_by_stage_id(self, info, stage_id):
       query = Pipelines.get_query(info)
       return query.filter(PipelinesModel.pipeline_stage_id == stage_id)

    def resolve_fields_by_tag_id(self, info, tag_id):
       query = Fields.get_query(info)
       return query.filter(FieldsModel.release_tag_id == tag_id)

    def resolve_product_class_by_class_name(self, info, name):
       query = ProductClass.get_query(info)
       return query.filter(ProductClassModel.class_name == name).first()

    def resolve_pipelines_by_name(self, info, name):
        query = Pipelines.get_query(info)
        return query.filter(PipelinesModel.name == name).first()

    def resolve_modules_by_name(self, info, name):
        query = Modules.get_query(info)
        return query.filter(ModulesModel.name == name).first()

schema = Schema(query=Query)
