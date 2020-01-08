from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import (
    Schema, ObjectType, Field, List, String, Int, Boolean,
    Argument, InputObjectType, relay
)
from sqlalchemy import or_, and_, func
import subprocess

import models
import schemas
import utils
import os

from database import db_session

INSTANCE = os.getenv('API_INSTANCE')


class SearchProductClass(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.ProductClass, models.ProductType])


class SearchPipelinesList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [
            models.Pipelines,
            models.Processes,
            models.PipelineStage,
            models.GroupPypelines,
            models.TgUser])


class SearchModulesList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.Modules, models.TgUser, models.Pipelines])


class SearchProductType(InputObjectType):
    text = String()
    columns = utils.column_from_classes(models.ProductType)


class SearchFieldList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.Fields, models.ReleaseTag])


class SearchProcessList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [models.Processes, models.ProcessStatus, models.Fields, models.ReleaseTag, models.TgUser])


class SearchProductsList(InputObjectType):
    text = String()
    columns = utils.column_from_classes(
        [
            models.Products,
            models.ReleaseTag,
            models.Fields,
            models.ProductClass,
            models.ProductType,
            models.Mask,
            models.Map])


class SearchReleaseTag(InputObjectType):
    text = String()
    columns = utils.column_from_classes([models.ReleaseTag, models.Fields])


class SearchPipelinesModulesList(InputObjectType):
    text = String()
    columns = utils.column_from_classes([models.ReleaseTag, models.Fields])


class Query(ObjectType):
    """Query objects for GraphQL API"""
    node = relay.Node.Field()

    # gets all entries
    product_class_list = SQLAlchemyConnectionField(
        schemas.ProductClass,
        sort=Argument(utils.sort_enum_for([
            models.ProductClass, models.ProductType
        ])),
        search=SearchProductClass(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    pipelines_list = SQLAlchemyConnectionField(
        schemas.Pipelines,
        sort=Argument(utils.sort_enum_for([
            models.Pipelines, models.PipelineStage,
            models.GroupPypelines, models.TgUser
        ])),
        search=SearchPipelinesList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int())
    modules_list = SQLAlchemyConnectionField(
        schemas.Modules,
        sort=Argument(utils.sort_enum_for([
            models.Modules, models.TgUser, models.Pipelines
        ])),
        search=SearchModulesList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    group_pypelines_list = SQLAlchemyConnectionField(schemas.GroupPypelines)
    pipelines_modules_list = SQLAlchemyConnectionField(
        schemas.PipelinesModules)
    pipeline_stage_list = SQLAlchemyConnectionField(schemas.PipelineStage)
    product_type_list = SQLAlchemyConnectionField(
        schemas.ProductType,
        sort=Argument(utils.sort_enum_for(models.ProductType)),
        search=SearchProductType(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )
    mask_list = SQLAlchemyConnectionField(schemas.Mask)
    map_list = SQLAlchemyConnectionField(schemas.Map)
    catalog_list = SQLAlchemyConnectionField(schemas.Catalog)
    filters_list = SQLAlchemyConnectionField(schemas.Filters)
    session_list = SQLAlchemyConnectionField(schemas.Session)

    # gets list by filters
    release_tag_list = SQLAlchemyConnectionField(
        schemas.ReleaseTag,
        only_available=Boolean(),
        sort=Argument(utils.sort_enum_for([models.ReleaseTag, models.Fields])),
        search=SearchReleaseTag(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    fields_list = SQLAlchemyConnectionField(
        schemas.Fields, only_available=Boolean(),
        sort=Argument(utils.sort_enum_for([
            models.Fields, models.ReleaseTag
        ])),
        search=SearchFieldList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    processes_list = SQLAlchemyConnectionField(
        schemas.Processes,
        all_instances=Boolean(),
        running=Boolean(),
        failure=Boolean(),
        success=Boolean(),
        published=Boolean(),
        removed=Boolean(),
        saved=Boolean(),
        sort=Argument(utils.sort_enum_for([
            models.Processes,
            models.TgUser,
            models.Fields,
            models.ReleaseTag,
            models.ProcessStatus
        ])),
        search=SearchProcessList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    products_list = SQLAlchemyConnectionField(
        schemas.Products,
        tag_id=Int(),
        field_id=Int(),
        type_id=Int(),
        class_id=Int(),
        band=String(),
        sort=Argument(utils.sort_enum_for([
            models.Products,
            models.ReleaseTag,
            models.Fields,
            models.ProductClass,
            models.ProductType
        ])),
        search=SearchProductsList(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int()
    )

    # gets by field unique
    product_class_by_class_name = Field(
        lambda: schemas.ProductClass, name=String())
    pipelines_by_name = Field(lambda: schemas.Pipelines, name=String())
    modules_by_name = Field(lambda: schemas.Modules, name=String())
    process_by_process_id = Field(lambda: schemas.Processes, process_id=Int())

    # gets list by unique field
    fields_by_tag_id = List(
        lambda: schemas.Fields,
        tag_id=Int(),
        only_available=Boolean()
    )
    pipelines_by_stage_id_and_tag_id_and_field_id = relay.ConnectionField(
        schemas.PipelinesExecutionConnection,
        stage_id=Int(),
        tag_id=Int(),
        field_id=Int(),
        before=String(),
        after=String(),
        first=Int(),
        last=Int())

    processes_by_tag_id_and_field_id_and_pipeline_id = List(
        lambda: schemas.Processes,
        pipeline_id=Int(),
        tag_id=Int(),
        field_id=Int(),
    )
    products_by_process_id = List(lambda: schemas.Products, process_id=Int())
    process_components_by_process_id = List(
        lambda: schemas.ProcessComponent, process_id=Int()
    )
    comments_by_process_id = List(lambda: schemas.Comments, process_id=Int())
    fields_by_tagname = List(lambda: schemas.Fields, tagname=String())
    product_class_by_type_id = List(
        lambda: schemas.ProductClass, type_id=Int())
    git_info = relay.ConnectionField(schemas.GitInfoConnection)
    time_profile = relay.ConnectionField(
        schemas.TimeProfileConnection,
        process_id=Int())

    output_products_by_pipeline = relay.ConnectionField(
        schemas.ProductsByPipelineConnection,
        pipeline_id=Int())
    input_products_by_pipeline = relay.ConnectionField(
        schemas.ProductsByPipelineConnection,
        pipeline_id=Int())

    def resolve_product_class_list(self, info, sort=list(),
                                   search=None, **args):
        query = schemas.ProductClass.get_query(info)
        tables = utils.selected_tables_from_arguments(sort)

        if utils.is_valid_search(search):
            tables = tables.union(utils.selected_tables_from_arguments(
                search['columns']
            ))

        if 'product_type' in tables:
            query = query.join(models.ProductType)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_pipelines_list(self, info, sort=list(), search=None,
                               **args):
        query = schemas.Pipelines.get_query(info)
        tables = utils.selected_tables_from_arguments(sort)
        if utils.is_valid_search(search):
            tables = tables.union(
                utils.selected_tables_from_arguments(
                    search['columns']
                )
            )

        if 'tg_user' in tables:
            query = query.join(models.TgUser)
        if 'group_pypelines' in tables:
            query = query.join(models.GroupPypelines)
        if 'pipeline_stage' in tables:
            query = query.join(models.PipelineStage)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.distinct().order_by(*sort)

    def resolve_modules_list(self, info, sort=list(), search=None, **args):
        query = schemas.Modules.get_query(info)
        tables = utils.selected_tables_from_arguments(sort)
        if utils.is_valid_search(search):
            tables = tables.union(
                utils.selected_tables_from_arguments(
                    search['columns']))

        if 'tg_user' in tables:
            query = query.join(models.TgUser)
        if 'pipelines' in tables:
            query = query.join(models.PipelinesModules)
            query = query.join(models.Pipelines)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.distinct().order_by(*sort)

    def resolve_product_type_list(
            self,
            info,
            sort=list(),
            search=None,
            **args):
        query = schemas.ProductType.get_query(info)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_pipelines_by_stage_id_and_tag_id_and_field_id(
            self, info, stage_id=None, tag_id=None, field_id=None, **args):

        sub_query = db_session.query(
            func.distinct(models.Pipelines.pipeline_id).label('pipeline_id'),
            models.Pipelines.name.label('pipeline_name'),
            models.Pipelines.display_name.label('pipeline_display_name'),
            models.PipelineStage.display_name.label('stage_display_name'),
            func.count(func.distinct(models.Processes.process_id)).label('process_count'),
            func.max(models.Processes.process_id).label('last_process_id')
        ).select_from(
            models.Pipelines
        ).join(
            models.Pipelines.processes
        ).join(
            models.PipelineStage
        ).join(
            models.ProcessStatus
        ).group_by(
            models.Pipelines.pipeline_id,
            models.PipelineStage.pipeline_stage_id
        ).order_by(
            models.PipelineStage.display_name, models.Pipelines.display_name
        )

        _filters = list()
        # _filters.append(models.Processes.flag_removed == False)
        _filters.append(models.Processes.instance == INSTANCE)

        # The link between the table processes and release_tag table depends on
        # the table fields
        if field_id or tag_id:
            sub_query = sub_query.join(
                models.ProcessFields).join(
                models.Fields)
        if field_id:
            _filters.append(models.ProcessFields.field_id == field_id)
        if tag_id:
            sub_query = sub_query.join(models.ReleaseTag)
            _filters.append(models.ReleaseTag.tag_id == tag_id)
        if stage_id:
            _filters.append(models.Pipelines.pipeline_stage_id == stage_id)
        sub_query = sub_query.filter(and_(*_filters)).subquery()

        query = db_session.query(
            sub_query,
            models.Processes.start_time.label('last_process_start_time'),
            models.Processes.end_time.label('last_process_end_time'),
            models.ProcessStatus.name.label('last_process_status'),
        ).join(
            sub_query,
            models.Processes.process_id == sub_query.c.last_process_id).join(
            models.ProcessStatus).all()

        result = list()
        for row in query:
            result.append(schemas.PipelinesExecution(**row._asdict()))

        return result

    def resolve_processes_by_tag_id_and_field_id_and_pipeline_id(
            self, info, pipeline_id, tag_id=None, field_id=None):

        query = schemas.Processes.get_query(
            info
        ).join(
            models.ProcessPipeline
        ).join(
            models.ProcessStatus
        ).order_by(
            models.Processes.process_id.desc()
        )

        _filters = list()
        _filters.append(models.ProcessPipeline.pipeline_id == pipeline_id)
        # _filters.append(models.Processes.flag_removed == False)
        _filters.append(models.Processes.instance == INSTANCE)

        if field_id or tag_id:
            query = query.join(
                models.ProcessFields).join(
                models.Fields)
        if field_id:
            _filters.append(models.ProcessFields.field_id == field_id)
        if tag_id:
            query = query.join(models.ReleaseTag)
            _filters.append(models.ReleaseTag.tag_id == tag_id)

        return query.filter(and_(*_filters))

    def resolve_products_by_process_id(self, info, process_id):
        query = schemas.Products.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.Products.product_id
        )

    def resolve_process_components_by_process_id(self, info, process_id):
        query = schemas.ProcessComponent.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.ProcessComponent.module_id
        )

    def resolve_comments_by_process_id(self, info, process_id):
        query = schemas.Comments.get_query(info)
        return query.filter_by(
            process_id=process_id
        ).order_by(
            models.Comments.date
        )

    def resolve_process_by_process_id(self, info, process_id):
        query = schemas.Processes.get_query(info)
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

        query = schemas.ReleaseTag.get_query(info)
        query = query.join(models.Fields)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        if only_available:
            query = query.filter_by(status=True)

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
        query = schemas.Fields.get_query(info)
        if only_available:
            query = query.filter_by(status=True)

        tables = utils.selected_tables_from_arguments(sort)
        if utils.is_valid_search(search):
            tables = tables.union(utils.selected_tables_from_arguments(
                search['columns']
            ))

        if 'release_tag' in tables:
            query = query.join(models.ReleaseTag)

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.order_by(*sort)

    def resolve_processes_list(
            self,
            info,
            all_instances=None,
            running=None,
            failure=None,
            success=None,
            published=None,
            saved=None,
            removed=False,
            sort=list(),
            search=None,
            **args):

        query = schemas.Processes.get_query(info)

        if removed is False:
            query = query.filter_by(flag_removed=False)
        else:
            query = query.filter(models.Processes.flag_removed.isnot(False))

        if not all_instances:
            query = query.filter_by(instance=INSTANCE)

        if running is True:
            query = query.filter(models.Processes.end_time.is_(None))
        elif running is False:
            query = query.filter(models.Processes.end_time.isnot(None))

        if failure is True:
            query = query.filter(models.Processes.status_id == 3)

        if success is True:
            query = query.filter(models.Processes.status_id == 1)

        if published is True:
            query = query.filter(models.Processes.published_date.isnot(None))
        elif published is False:
            query = query.filter(models.Processes.published_date.is_(None))

        if removed is True:
            query = query.filter(models.Processes.flag_removed.isnot(False))

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

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.distinct().order_by(*sort)

    def resolve_products_list(
            self,
            info,
            tag_id=None,
            field_id=None,
            type_id=None,
            class_id=None,
            band=None,
            search=None,
            sort=list(),
            **args):
        query = schemas.Products.get_query(info)
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

        _filters = utils.prepare_sqlalchemy_filters_casting_columns_to_str(
            search)
        if _filters:
            query = query.filter(or_(*_filters))

        return query.distinct().order_by(*sort)

    def resolve_fields_by_tag_id(self, info, tag_id, only_available=True):
        query = schemas.Fields.get_query(info)

        if only_available:
            query = query.filter_by(status=True)

        return query.filter(models.Fields.release_tag_id == tag_id)

    def resolve_fields_by_tagname(self, info, tagname):
        query = schemas.Fields.get_query(info)
        query = query.join(models.ReleaseTag)
        return query.filter(models.ReleaseTag.name == tagname)

    def resolve_product_class_by_class_name(self, info, name):
        query = schemas.ProductClass.get_query(info)
        return query.filter(
            models.ProductClass.class_name == name).one_or_none()

    def resolve_product_class_by_type_id(self, info, type_id):
        query = schemas.ProductClass.get_query(info)
        query = query.join(models.ProductType)
        return query.filter(models.ProductType.type_id == type_id)

    def resolve_pipelines_by_name(self, info, name):
        query = schemas.Pipelines.get_query(info)
        return query.filter(models.Pipelines.name == name).one_or_none()

    def resolve_modules_by_name(self, info, name):
        query = schemas.Modules.get_query(info)
        return query.filter(models.Modules.name == name).one_or_none()

    def resolve_git_info(self, info, **args):
        current_branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]).strip()
        last_commit = subprocess.check_output(
            ["git", "log", "-1", "--format=%H"]).strip()
        last_commit_date = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd"]).strip()
        last_commit_author = subprocess.check_output(
            ["git", "log", "-1", "--pretty=format:%an"]).strip()
        last_tag = subprocess.check_output(
            ["git", "describe", "--tags"]).strip()

        return [schemas.GitInfo(
            current_branch=current_branch.decode("utf-8"),
            last_commit=last_commit.decode("utf-8"),
            last_commit_date=last_commit_date.decode("utf-8"),
            last_commit_author=last_commit_author.decode("utf-8"),
            last_tag=last_tag.decode("utf-8")
        )]

    def resolve_time_profile(self, info, process_id, **args):
        l_modules = list()

        modules = db_session.query(
            func.distinct(models.Modules.module_id).label('module_id'),
            models.Modules.name.label('name'),
            models.Modules.display_name.label('display_name')
        ).select_from(
            models.JobRuns
        ).join(
            models.Modules
        ).filter(
            models.JobRuns.process_id == process_id
        ).all()

        for module in modules:
            query = db_session.query(
                models.JobRuns.hid.label('hid'),
                models.JobRuns.start_time.label('start_time'),
                models.JobRuns.end_time.label('end_time')
            ).select_from(
                models.JobRuns
            ).join(
                models.Modules
            ).filter(
                models.JobRuns.process_id == process_id,
                models.Modules.module_id == module.module_id
            ).all()

            jobs = list()
            for row in query:
                jobs.append(schemas.JobRuns(**row._asdict()))

            l_modules.append(schemas.TimeProfile(
                display_name=module.display_name,
                module_name=module.name,
                jobs=jobs
            ))

        return l_modules

    def resolve_output_products_by_pipeline(self, info, pipeline_id, **args):
        l_modules = list()

        query = db_session.query(
            func.distinct(models.Modules.module_id).label('module_id'),
            models.Modules.name.label('module_name'),
            models.Modules.display_name.label('display_name')
        ).select_from(
            models.Modules
        ).join(
            models.ModuleOutput
        ).join(
            models.PipelinesModules
        ).join(
            models.Pipelines
        ).filter(
            models.Pipelines.pipeline_id == pipeline_id
        )

        for module in query.all():
            query = db_session.query(
                models.ProductClass.display_name
            ).select_from(
                models.ProductClass
            ).join(
                models.ModuleOutput
            ).filter(
                models.ModuleOutput.module_id == module.module_id
            )

            _products = list()
            for row in query.all():
                _products.append(row.display_name)

            l_modules.append(schemas.ProductsByPipeline(
                display_name=module.display_name,
                module_name=module.module_name,
                products=_products
            ))

        return l_modules

    def resolve_input_products_by_pipeline(self, info, pipeline_id, **args):
        l_modules = list()
        l_modules_from_pipeline_input = set()

        # get modules from pipeline_input
        query = db_session.query(
            func.distinct(models.PipelineInput.module_id).label('module_id'),
            models.Modules.name.label('module_name'),
            models.Modules.display_name.label('display_name')
        ).select_from(
            models.PipelineInput
        ).join(
            models.Modules
        ).filter(
            models.Pipelines.pipeline_id == pipeline_id
        )

        for module in query.all():
            l_modules_from_pipeline_input.add(module.module_id)

            query = db_session.query(
                models.ProductClass.display_name
            ).select_from(
                models.ProductClass
            ).join(
                models.PipelineInput
            ).filter(
                and_(
                    models.PipelineInput.module_id == module.module_id,
                    models.PipelineInput.pipeline_id == pipeline_id
                )
            )

            _products = list()
            for row in query.all():
                _products.append(row.display_name)

            l_modules.append(schemas.ProductsByPipeline(
                display_name=module.display_name,
                module_name=module.module_name,
                products=_products
            ))

        # get modules from module_input
        query = db_session.query(
            func.distinct(models.Modules.module_id).label('module_id'),
            models.Modules.name.label('module_name'),
            models.Modules.display_name.label('display_name')
        ).select_from(
            models.Modules
        ).join(
            models.ModuleInput
        ).join(
            models.PipelinesModules
        ).join(
            models.Pipelines
        ).filter(
            models.Pipelines.pipeline_id == pipeline_id
        )

        for module in query.all():
            if module.module_id in l_modules_from_pipeline_input:
                continue

            query = db_session.query(
                models.ProductClass.display_name
            ).select_from(
                models.ProductClass
            ).join(
                models.ModuleInput
            ).filter(
                models.ModuleInput.module_id == module.module_id
            )

            _products = list()
            for row in query.all():
                _products.append(row.display_name)

            l_modules.append(schemas.ProductsByPipeline(
                display_name=module.display_name,
                module_name=module.module_name,
                products=_products
            ))

        return l_modules


schema = Schema(query=Query)
