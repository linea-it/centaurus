from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import Schema, ObjectType, Field, List, String, Int, Boolean, Enum, Argument
from sqlalchemy.inspection import inspect
from sqlalchemy import or_
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
from schemas.products import Products
from schemas.file_locator import FileLocator
from schemas.tables import Tables
from schemas.process_status import ProcessStatus
from schemas.process_component import ProcessComponent
from schemas.session import Session
from schemas.pipelines_execution import PipelinesExecution
from schemas.job_runs import JobRuns
from schemas.comments import Comments
from schemas.saved_processes import SavedProcesses
from schemas.mask import Mask

from models import (
   ProductType as ProductTypeModel,
   ProductClass as ProductClassModel,
   Pipelines as PipelinesModel,
   PipelineStatus as PipelineStatusModel,
   ProcessPipeline as ProcessPipelineModel,
   Modules as ModulesModel,
   Processes as ProcessesModel,
   ProcessFields as ProcessFieldsModel,
   Products as ProductsModel,
   ProcessComponent as ProcessComponentModel,
   Fields as FieldsModel,
   Comments as CommentsModel,
   SavedProcesses as SavedProcessesModel,
   Mask as MaskModel,
   Tables as TablesModel,
   ReleaseTag as ReleaseTagModel,
)

from views import PipelinesExecution as PipelinesExecutionModel

import os

INSTANCE = os.getenv('API_INSTANCE')


def sort_enum_for(cls):
   """Create Graphene Enum for sorting a SQLAlchemy class query"""

   name = cls.__name__+'SortEnum' 
   items = list()

   for attr in inspect(cls).attrs:
      try:
         asc = attr.expression
         desc = asc.desc()
      except AttributeError as error:
         pass
      else:
         key = attr.key.lower()
         items.extend([(key + '_asc', asc), (key + '_desc', desc)])

   return Enum(name, items)


class Query(ObjectType):
   """Query objects for GraphQL API"""

   # gets all entries
   product_class_list = SQLAlchemyConnectionField(ProductClass)
   pipelines_list = SQLAlchemyConnectionField(Pipelines)
   modules_list = SQLAlchemyConnectionField(Modules)
   group_pypelines_list = SQLAlchemyConnectionField(GroupPypelines)
   pipelines_modules_list = SQLAlchemyConnectionField(PipelinesModules)
   release_tag_list = SQLAlchemyConnectionField(ReleaseTag)
   fields_list = SQLAlchemyConnectionField(Fields)
   pipeline_stage_list = SQLAlchemyConnectionField(PipelineStage)
   product_type_list = SQLAlchemyConnectionField(ProductType)
   mask_list = SQLAlchemyConnectionField(Mask)

   # gets list by filters
   processes_list = SQLAlchemyConnectionField(
      Processes,
      all_instances=Boolean(),
      running=Boolean(),
      published=Boolean(),
      saved=Boolean(),
      sort=Argument(List(sort_enum_for(ProcessesModel))),
      before=String(),
      after=String(),
      first=Int(),
      last=Int()
   )

   products_list = SQLAlchemyConnectionField(
      Products,
      release_name=String(),
      field_name=String(),
      type_name=String(),
      class_name=String(),
      band=String(),
      filter=String(),
      before=String(),
      after=String(),
      first=Int(),
      last=Int()
   )

   # gets by field unique
   product_class_by_class_name = Field(lambda: ProductClass, name=String())
   pipelines_by_name = Field(lambda: Pipelines, name=String())
   modules_by_name = Field(lambda: Modules, name=String())
   process_by_process_id = Field(lambda: Processes, process_id=Int())

   # gets list by id 
   fields_by_tag_id = List(lambda: Fields, tag_id=Int())
   pipelines_by_field_id_and_stage_id = List(lambda: PipelinesExecution, stage_id=Int(), field_id=Int())
   processes_by_field_id_and_pipeline_id = List(lambda: Processes, field_id=Int(), pipeline_id=Int())
   products_by_process_id = List(lambda: Products, process_id=Int())
   process_components_by_process_id = List(lambda: ProcessComponent, process_id=Int())
   comments_by_process_id = List(lambda: Comments, process_id=Int())

   def resolve_pipelines_by_field_id_and_stage_id(self, info, stage_id, field_id=None):
      query = PipelinesExecution.get_query(info)

      return query.filter_by(
         pipeline_stage_id=stage_id, instance=INSTANCE
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

   def resolve_processes_by_field_id_and_pipeline_id(self, info, pipeline_id, field_id=None):
      query = Processes.get_query(info)
      return query.filter_by(
         instance=INSTANCE, flag_removed=False
      ).join(
         ProcessPipelineModel
      ).filter_by(
         pipeline_id=pipeline_id
      ).outerjoin(
         ProcessFieldsModel
      ).filter_by(
         field_id=field_id
      ).order_by(
         ProcessesModel.process_id.desc()
      )

   def resolve_products_by_process_id(self, info, process_id):
      query = Products.get_query(info)
      return query.filter_by(
         process_id=process_id
      ).order_by(
         ProductsModel.product_id
      )

   def resolve_process_components_by_process_id(self, info, process_id):
      query = ProcessComponent.get_query(info)
      return query.filter_by(
         process_id=process_id
      ).order_by(
         ProcessComponentModel.module_id
      )

   def resolve_comments_by_process_id(self, info, process_id):
      query = Comments.get_query(info)
      return query.filter_by(
         process_id=process_id
      ).order_by(
         CommentsModel.date
      )

   def resolve_process_by_process_id(self, info, process_id):
      query = Processes.get_query(info)
      return query.filter_by(
         process_id=process_id
      ).order_by(
         ProcessesModel.process_id
      ).one_or_none()

   def resolve_processes_list(self, info, all_instances=None, running=None,
      published=None, saved=None, sort=list(), **args):
      query = Processes.get_query(info)
      query = query.filter_by(flag_removed=False)

      if not all_instances:
         query = query.filter_by(instance=INSTANCE)

      if running is True:
         query = query.filter(ProcessesModel.end_time.is_(None))
      elif running is False:
         query = query.filter(ProcessesModel.end_time.isnot(None))

      if published is True:
         query = query.filter(ProcessesModel.published_date.isnot(None))
      elif published is False:
         query = query.filter(ProcessesModel.published_date.is_(None))

      if saved is True:
         query = query.join(SavedProcessesModel)
      elif saved is False:
         query = query.outerjoin(
            SavedProcessesModel
         ).filter(SavedProcessesModel.process_id.is_(None))

      return query.order_by(*sort)

   def resolve_products_list(self, info, release_name=None, field_name=None,
      type_name=None, class_name=None, band=None, filter=None, sort=list(),
      **args):
      query = Products.get_query(info)
      query = query.join(TablesModel)
      query = query.join(MaskModel)
      query = query.join(
         ReleaseTagModel, MaskModel.tag_id == ReleaseTagModel.tag_id)
      query = query.join(
         FieldsModel, MaskModel.field_id == FieldsModel.field_id)
      query = query.join(ProductClassModel)
      query = query.join(ProductTypeModel)

      if release_name:
         query = query.filter(ReleaseTagModel.name == release_name)
      if field_name:
         query = query.filter(FieldsModel.field_name == field_name)
      if band:
         query = query.filter(MaskModel.filter == band)
      if class_name:
         query = query.filter(ProductClassModel.class_name == class_name)
      if type_name:
         query = query.filter(ProductTypeModel.type_name == type_name)

      if filter:
         _columns = [
            ReleaseTagModel.name, FieldsModel.field_name, MaskModel.filter,
            ProductClassModel.class_name, ProductTypeModel.type_name
         ]

         _filters = [column.like("%{0}%".format(filter)) for column in _columns]
         query = query.filter(or_(*_filters))

      return query.order_by(*sort)

   def resolve_fields_by_tag_id(self, info, tag_id):
       query = Fields.get_query(info)
       return query.filter(FieldsModel.release_tag_id == tag_id)

   def resolve_product_class_by_class_name(self, info, name):
       query = ProductClass.get_query(info)
       return query.filter(ProductClassModel.class_name == name).one_or_none()

   def resolve_pipelines_by_name(self, info, name):
        query = Pipelines.get_query(info)
        return query.filter(PipelinesModel.name == name).one_or_none()

   def resolve_modules_by_name(self, info, name):
        query = Modules.get_query(info)
        return query.filter(ModulesModel.name == name).one_or_none()

schema = Schema(query=Query)
