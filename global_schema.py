from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import Schema, ObjectType, Field, List, String, Int, Boolean, Argument, InputObjectType
from sqlalchemy import or_

from schemas.product_class import ProductClass
from schemas.product_type import ProductType
from schemas.pipelines import Pipelines
from schemas.modules import Modules
from schemas.pipelines_modules import PipelinesModules
from schemas.pipeline_stage import PipelineStage
from schemas.group_pypelines import GroupPypelines
from schemas.release_tag import ReleaseTag
from schemas.fields import Fields
from schemas.processes import Processes
from schemas.products import Products
from schemas.process_component import ProcessComponent
from schemas.pipelines_execution import PipelinesExecution
from schemas.comments import Comments
from schemas.mask import Mask
from schemas.map import Map
from schemas.catalog import Catalog
from schemas.filters import Filters

# Unused imports but necessary to show their objects from other objects.
from schemas.tg_user import TgUser
from schemas.pipeline_status import PipelineStatus
from schemas.file_locator import FileLocator
from schemas.tables import Tables
from schemas.process_status import ProcessStatus
from schemas.session import Session
from schemas.job_runs import JobRuns
from schemas.saved_processes import SavedProcesses

import models
import views
import utils
import os

INSTANCE = os.getenv('API_INSTANCE')


class SearchProductClass(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.ProductClass, models.ProductType])


class SearchPipelinesList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.Pipelines, models.Processes])


class SearchModulesList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.Modules, models.TgUser])


class SearchProductType(InputObjectType):
    text = String()
    columns = utils.column_from_classes(models.ProductType)


class Query(ObjectType):
    """Query objects for GraphQL API"""

    # gets all entries
    product_class_list = SQLAlchemyConnectionField(
        ProductClass,
        sort=Argument(utils.sort_enum_for([models.ProductClass, models.ProductType])),
        search=SearchProductClass(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    pipelines_list = SQLAlchemyConnectionField(
        Pipelines,
        sort=Argument(utils.sort_enum_for([models.Pipelines, models.Processes])),
        search=SearchPipelinesList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    modules_list = SQLAlchemyConnectionField(
        Modules,
        sort=Argument(utils.sort_enum_for([models.Modules, models.TgUser])),
        search=SearchModulesList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    group_pypelines_list = SQLAlchemyConnectionField(GroupPypelines)
    pipelines_modules_list = SQLAlchemyConnectionField(PipelinesModules)
    pipeline_stage_list = SQLAlchemyConnectionField(PipelineStage)
    product_type_list = SQLAlchemyConnectionField(
        ProductType,
        sort=Argument(utils.sort_enum_for(models.ProductType)),
        search=SearchProductType(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    mask_list = SQLAlchemyConnectionField(Mask)
    map_list = SQLAlchemyConnectionField(Map)
    catalog_list = SQLAlchemyConnectionField(Catalog)
    filters_list = SQLAlchemyConnectionField(Filters)

    # gets list by filters
    release_tag_list = SQLAlchemyConnectionField(
        ReleaseTag,
        only_available=Boolean(),
        sort=Argument(List(utils.sort_enum_for(models.ReleaseTag))),
        search=String(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    fields_list = SQLAlchemyConnectionField(
        Fields, only_available=Boolean(),
        sort=Argument(List(utils.sort_enum_for(models.Fields))),
        search=String(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    processes_list = SQLAlchemyConnectionField(
        Processes,
        all_instances=Boolean(),
        running=Boolean(),
        published=Boolean(),
        saved=Boolean(),
        sort=Argument(List(utils.sort_enum_for(models.Processes))),
        search=String(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    products_list = SQLAlchemyConnectionField(
        Products,
        tag_id=Int(),
        field_id=Int(),
        type_id=Int(),
        class_id=Int(),
        band=String(),
        sort=Argument(List(utils.sort_enum_for(models.Products))),
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

    # gets list by unique field
    fields_by_tag_id = List(
        lambda: Fields,
        tag_id=Int(),
        only_available=Boolean())
    pipelines_by_field_id_and_stage_id = List(
        lambda: PipelinesExecution, stage_id=Int(), field_id=Int())
    processes_by_field_id_and_pipeline_id = List(
        lambda: Processes, field_id=Int(), pipeline_id=Int())
    products_by_process_id = List(lambda: Products, process_id=Int())
    process_components_by_process_id = List(
        lambda: ProcessComponent, process_id=Int())
    comments_by_process_id = List(lambda: Comments, process_id=Int())
    fields_by_tagname = List(lambda: Fields, tagname=String())
    product_class_by_type_id = List(lambda: ProductClass, type_id=Int())

    def resolve_product_class_list(
            self,
            info,
            sort=list(),
            search=None,
            **args):
        query = ProductClass.get_query(info)
        tables = utils.selected_tables_from_arguments(sort)
        if utils.is_valid_search(search):
            tables = tables.union(
                utils.selected_tables_from_arguments(
                    search['columns']))

        if 'product_type' in tables:
            query = query.join(models.ProductType)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_pipelines_list(self, info, sort=list(), search=None, **args):
        query = Pipelines.get_query(info)
        tables = utils.selected_tables_from_arguments(sort)
        if utils.is_valid_search(search):
            tables = tables.union(
                utils.selected_tables_from_arguments(
                    search['columns']))

        if 'processes' in tables:
            query = query.join(models.ProcessPipeline)
            query = query.join(models.Processes)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_modules_list(self, info, sort=list(), search=None, **args):
        query = Modules.get_query(info)
        tables = utils.selected_tables_from_arguments(sort)
        if utils.is_valid_search(search):
            tables = tables.union(
                utils.selected_tables_from_arguments(
                    search['columns']))

        if 'tg_user' in tables:
            query = query.join(models.TgUser)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_product_type_list(
            self,
            info,
            sort=list(),
            search=None,
            **args):
        query = ProductType.get_query(info)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_pipelines_by_field_id_and_stage_id(
            self, info, stage_id, field_id=None):
        query = PipelinesExecution.get_query(info)

        return query.filter_by(
            pipeline_stage_id=stage_id, instance=INSTANCE
        ).filter_by(
            field_id=field_id
        ).join(
            models.Pipelines
        ).join(
            models.PipelineStatus
        ).filter_by(
            name='enabled'
        ).join(
            models.Pipelines.processes
        ).filter_by(
            flag_removed=False
        ).order_by(
            views.PipelinesExecution.name
        )

    def resolve_processes_by_field_id_and_pipeline_id(
            self, info, pipeline_id, field_id=None):
        query = Processes.get_query(info)
        return query.filter_by(
            instance=INSTANCE, flag_removed=False
        ).join(
            models.ProcessPipeline
        ).filter_by(
            pipeline_id=pipeline_id
        ).outerjoin(
            models.ProcessFields
        ).filter_by(
            field_id=field_id
        ).order_by(
            models.Processes.process_id.desc()
        )

    def resolve_products_by_process_id(self, info, process_id):
        query = Products.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.Products.product_id
        )

    def resolve_process_components_by_process_id(self, info, process_id):
        query = ProcessComponent.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.ProcessComponent.module_id
        )

    def resolve_comments_by_process_id(self, info, process_id):
        query = Comments.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.Comments.date
        )

    def resolve_process_by_process_id(self, info, process_id):
        query = Processes.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.Processes.process_id
        ).one_or_none()

    def resolve_release_tag_list(self, info, only_available=True, sort=list(),
                                 search=None, **args):
        """ Returns available release list(default behavior)
        Arguments:
           info -- is the resolver info.
        Keyword Arguments:
           only_available {bool} -- if False returns all entries regardless
              of status. (default: {True})
           sort {list} -- columns list to sorting. e.g.: ["name_asc"]

        """

        query = ReleaseTag.get_query(info)
        _columns = [
            models.ReleaseTag.release_display_name,
            models.ReleaseTag.name
        ]
        if only_available:
            query = query.join(models.Fields).filter_by(status=True)
            _columns += [
                models.Fields.display_name,
                models.Fields.field_name
            ]
        if search:
            _filters = [column.like("%{}%".format(search))
                        for column in _columns]
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_fields_list(self, info, only_available=True, sort=list(),
                            search=None, **args):
        """ Returns available field list (default behavior)
        Arguments:
           info -- is the resolver info.
        Keyword Arguments:
           only_available {bool} -- if False returns all entries regardless
              of status. (default: {True})
           sort {list} -- columns list to sorting. e.g.: ["field_name_asc"]
        """

        query = Fields.get_query(info)
        if only_available:
            query = query.filter_by(status=True)
        query = query.join(models.ReleaseTag)
        if search:
            _columns = [
                models.Fields.display_name,
                models.Fields.field_name,
                models.ReleaseTag.release_display_name,
                models.ReleaseTag.name
            ]
            _filters = [column.like("%{}%".format(search))
                        for column in _columns]
            query = query.filter(or_(*_filters))
        return query.order_by(*sort)

    def resolve_processes_list(
            self,
            info,
            all_instances=None,
            running=None,
            published=None,
            saved=None,
            sort=list(),
            search=None,
            **args):

        query = Processes.get_query(info).filter_by(flag_removed=False)

        if not all_instances:
            query = query.filter_by(instance=INSTANCE)

        if running is True:
            query = query.filter(models.Processes.end_time.is_(None))
        elif running is False:
            query = query.filter(models.Processes.end_time.isnot(None))

        if published is True:
            query = query.filter(models.Processes.published_date.isnot(None))
        elif published is False:
            query = query.filter(models.Processes.published_date.is_(None))

        if saved is True:
            query = query.join(models.SavedProcesses)
        elif saved is False:
            query = query.outerjoin(
                models.SavedProcesses
            ).filter(models.SavedProcesses.process_id.is_(None))

        query = query.join(models.ProcessStatus)
        query = query.outerjoin(models.ProcessFields).outerjoin(models.Fields)
        query = query.outerjoin(models.ReleaseTag)
        query = query.join(models.Session).join(models.TgUser)

        if search:
            _columns = [
                models.Processes.name,
                models.ProcessStatus.display_name,
                models.Fields.display_name,
                models.ReleaseTag.release_display_name,
                models.TgUser.display_name
            ]

            _filters = [column.like("%{}%".format(search))
                        for column in _columns]
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_products_list(
            self,
            info,
            tag_id=None,
            field_id=None,
            type_id=None,
            class_id=None,
            band=None,
            filter=None,
            sort=list(),
            **args):
        query = Products.get_query(info)
        query = query.join(models.ProductField)
        query = query.outerjoin(models.Tables)
        query = query.join(models.Processes)
        query = query.filter(models.Processes.flag_removed == False)
        query = query.outerjoin(
            models.Mask, models.Mask.table_id == models.Tables.table_id)
        query = query.outerjoin(
            models.Map, models.Map.table_id == models.Tables.table_id)
        query = query.outerjoin(
            models.Fields,
            models.ProductField.field_id == models.Fields.field_id)
        query = query.outerjoin(
            models.ReleaseTag,
            models.Fields.release_tag_id == models.ReleaseTag.tag_id)
        query = query.join(models.ProductClass)
        query = query.join(models.ProductType)

        if tag_id:
            query = query.filter(models.ReleaseTag.tag_id == tag_id)
        if field_id:
            query = query.filter(models.Fields.field_id == field_id)
        if band:
            query = query.filter(
                or_(models.Mask.filter == band, models.Map.filter == band))
        if class_id:
            query = query.filter(models.ProductClass.class_id == class_id)
        if type_id:
            query = query.filter(models.ProductType.type_id == type_id)

        if filter:
            _columns = [
                models.ReleaseTag.name, models.Fields.field_name,
                models.Products.display_name,
                models.ProductClass.class_name, models.ProductType.type_name,
                models.Map.filter, models.Mask.filter
            ]

            _filters = [column.like("%{0}%".format(filter))
                        for column in _columns]
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_fields_by_tag_id(self, info, tag_id, only_available=True):
        query = Fields.get_query(info)

        if only_available:
            query = query.filter_by(status=True)

        return query.filter(models.Fields.release_tag_id == tag_id)

    def resolve_fields_by_tagname(self, info, tagname):
        query = Fields.get_query(info)
        query = query.join(models.ReleaseTag)
        return query.filter(models.ReleaseTag.name == tagname)

    def resolve_product_class_by_class_name(self, info, name):
        query = ProductClass.get_query(info)
        return query.filter(
            models.ProductClass.class_name == name).one_or_none()

    def resolve_product_class_by_type_id(self, info, type_id):
        query = ProductClass.get_query(info)
        query = query.join(models.ProductType)
        return query.filter(models.ProductType.type_id == type_id)

    def resolve_pipelines_by_name(self, info, name):
        query = Pipelines.get_query(info)
        return query.filter(models.Pipelines.name == name).one_or_none()

    def resolve_modules_by_name(self, info, name):
        query = Modules.get_query(info)
        return query.filter(models.Modules.name == name).one_or_none()


schema = Schema(query=Query)
