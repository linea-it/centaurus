from sqlalchemy import or_
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import Schema, ObjectType, Field, List, String, Int
from sqlalchemy import func, or_
from database import db_session


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
from schemas.processes import Processes
from schemas.process_status import ProcessStatus
from schemas.session import Session
from schemas.pipelines_execution import PipelinesExecution

from models import (
   ProductClass as ProductClassModel,
   Pipelines as PipelinesModel,
   PipelineStatus as PipelineStatusModel,
   ProcessPipeline as ProcessPipelineModel,
   Modules as ModulesModel,
   Processes as ProcessesModel,
   ProcessFields as ProcessFieldsModel,
   Fields as FieldsModel
)

from views import PipelinesExecution as PipelinesExecutionModel

import os

instance = os.getenv('API_INSTANCE')


class Query(ObjectType):
   """Query objects for GraphQL API"""

   # gets all entries
   product_class_list = SQLAlchemyConnectionField(ProductClass)
   pipelines_list = SQLAlchemyConnectionField(Pipelines)
   processes_list = SQLAlchemyConnectionField(Processes)
   modules_list = SQLAlchemyConnectionField(Modules)
   group_pypelines_list = SQLAlchemyConnectionField(GroupPypelines)
   pipelines_modules_list = SQLAlchemyConnectionField(PipelinesModules)
   release_tag_list = SQLAlchemyConnectionField(ReleaseTag)
   fields_list = SQLAlchemyConnectionField(Fields)
   pipeline_stage_list = SQLAlchemyConnectionField(PipelineStage)

   # gets by field unique
   product_class_by_class_name = Field(lambda: ProductClass, name=String())
   pipelines_by_name = Field(lambda: Pipelines, name=String())
   modules_by_name = Field(lambda: Modules, name=String())

   # gets list by id 
   fields_by_tag_id = List(lambda: Fields, tag_id=Int())
   pipelines_by_field_id_and_stage_id = List(lambda: PipelinesExecution, stage_id=Int(), field_id=Int())
   processes_by_field_id_and_pipeline_id = List(lambda: Processes, field_id=Int(), pipeline_id=Int())

   def resolve_pipelines_by_field_id_and_stage_id(self, info, stage_id, field_id=None):
      query = PipelinesExecution.get_query(info)

      return query.filter_by(
         pipeline_stage_id=stage_id, instance=instance
      ).filter_by(
          field_id=field_id
      ).join(
         PipelinesModel
      ).join(
         PipelineStatusModel
      ).filter_by(
         name='enabled'
      ).join(
         PipelinesModel.processes
      ).filter_by(
         flag_removed=False
      ).order_by(
         PipelinesExecutionModel.name
      )

   def resolve_processes_by_field_id_and_pipeline_id(self, info, field_id, pipeline_id):
      query = Processes.get_query(info)
      return query.join(
         ProcessPipelineModel
      ).filter_by(
         pipeline_id=pipeline_id
      ).join(
         ProcessFieldsModel
      ).filter_by(
         field_id=field_id
      )

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
