# coding: utf-8

from database import Base
from sqlalchemy import (
    BigInteger, Boolean, CheckConstraint, Column, DateTime, Date,
    SmallInteger, Integer, String, Text, text, Sequence, Float,
    ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship, backref, deferred


class ProductType(Base):
    __tablename__ = 'product_type'

    seq = Sequence('product_type_type_id_seq', metadata=Base.metadata)

    type_id = Column(Integer, seq, primary_key=True)
    type_name = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(128))


class ProductClass(Base):
    __tablename__ = 'product_class'

    seq = Sequence('product_class_class_id_seq', metadata=Base.metadata)

    class_id = Column(Integer, seq, primary_key=True)
    type_id = Column(ForeignKey('product_type.type_id'), nullable=False)
    class_name = Column(String(128), nullable=False, unique=True)
    display_name = Column(String(128))
    is_system = Column(Boolean)

    product_type = relationship('ProductType')


class FileMimetype(Base):
    __tablename__ = 'file_mimetype'

    seq = Sequence('file_types_file_type_id_seq', metadata=Base.metadata)

    file_type_id = Column(Integer, seq, primary_key=True)
    mimetype_name = Column(String(32), nullable=False, unique=True)
    display_name = Column(String(64))


class GroupPypelines(Base):
    __tablename__ = 'group_pypelines'

    seq = Sequence('group_pypelines_group_id_seq', metadata=Base.metadata)

    group_id = Column(Integer, seq, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    parent_group_id = Column(ForeignKey('group_pypelines.group_id'))
    order_number = Column(Integer, nullable=False)
    display_name = Column(String(128), nullable=False)

    parent_group = relationship('GroupPypelines', remote_side=[group_id])


class PipelineStage(Base):
    __tablename__ = 'pipeline_stage'

    seq = Sequence('pypeline_stages_id_seq', metadata=Base.metadata)

    pipeline_stage_id = Column(Integer, seq, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    display_name = Column(String(128), nullable=False)
    level = Column(Integer)


class PipelineStatus(Base):
    __tablename__ = 'pipeline_status'

    seq = Sequence('pipeline_status_pipeline_status_id_seq', metadata=Base.metadata)

    pipeline_status_id = Column(Integer, seq, primary_key=True)
    name = Column(String(128), nullable=False)
    display_name = Column(String(128), nullable=False)


class ProcessStatus(Base):
    __tablename__ = 'process_status'

    seq = Sequence('process_status_process_status_id', metadata=Base.metadata)

    process_status_id = Column(Integer, seq, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    display_name = Column(String(64), nullable=False)


class ProcessingSite(Base):
    __tablename__ = 'processing_site'

    seq = Sequence('processing_site_id_site_seq', metadata=Base.metadata)

    id_site = Column(BigInteger, seq, primary_key=True)
    site_name = Column(String(32), nullable=False)


class Tables(Base):
    __tablename__ = 'tables'
    __table_args__ = (
        UniqueConstraint('schema_name', 'table_name'),
    )

    seq = Sequence('tables_table_id_seq', metadata=Base.metadata)

    table_id = Column(Integer, seq, primary_key=True)
    schema_name = Column(String(128), nullable=False)
    table_name = Column(String(128), nullable=False)

    map = relationship('Map', uselist=False, primaryjoin="Map.table_id == Tables.table_id")
    mask = relationship('Mask', uselist=False, primaryjoin="Mask.table_id == Tables.table_id")
    catalog = relationship('Catalog', uselist=False, primaryjoin="Catalog.table_id == Tables.table_id")


class TgUser(Base):
    __tablename__ = 'tg_user'

    seq = Sequence('tg_user_user_id_seq', metadata=Base.metadata)

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(64), unique=True)
    email_address = Column(String(255), unique=True)
    display_name = Column(String(255))
    created = Column(DateTime)
    affiliation = Column(String(255))
    status = Column(String(40))
    url_photo = Column(String(32))
    about = Column(Text)


class FileLocator(Base):
    __tablename__ = 'file_locator'

    seq = Sequence('file_locator_file_id_seq', metadata=Base.metadata)

    file_id = Column(Integer, seq, primary_key=True)
    uri = Column(String(256), nullable=False)
    provenance_id = Column(Integer)
    survey_id = Column(Integer)
    category_id = Column(Integer)
    file_name = Column(String(256))
    file_type_id = Column(ForeignKey('file_mimetype.file_type_id'))
    namespace = Column(String(256), nullable=False)

    file_type = relationship('FileMimetype')


class Modules(Base):
    __tablename__ = 'modules'

    seq = Sequence('modules_module_id_seq', metadata=Base.metadata)

    module_id = Column(Integer, seq, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    version = Column(String(10))
    display_name = Column(String(32), nullable=False)
    xml_config = Column(Text)
    description = Column(Text)
    version_date = Column(DateTime)
    grade = Column(Float)
    user_id = Column(ForeignKey('tg_user.user_id'))

    user = relationship('TgUser')
    pipelines_modules = relationship('PipelinesModules')


class Session(Base):
    __tablename__ = 'session'

    session_id = Column(Text, primary_key=True)
    data = Column(Text, nullable=False, server_default=text("now()"))
    expiration_time = Column(DateTime)
    user_id = Column(ForeignKey('tg_user.user_id'), nullable=False)
    tg_session = Column(String(64))

    user = relationship('TgUser')


class Pipelines(Base):
    __tablename__ = 'pipelines'

    seq = Sequence('pipelines_pipeline_id_seq', metadata=Base.metadata)

    pipeline_id = Column(Integer, seq, primary_key=True)
    group_id = Column(ForeignKey('group_pypelines.group_id'), nullable=False)
    display_name = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False, unique=True)
    order_number = Column(Integer)
    user_id = Column(ForeignKey('tg_user.user_id'))
    version = Column(String(10))
    version_date = Column(DateTime)
    description = Column(Text)
    pipeline_stage_id = Column(ForeignKey('pipeline_stage.pipeline_stage_id', match='FULL'))
    xml_workflow = Column(Text, nullable=False)
    pipeline_status_id = Column(ForeignKey('pipeline_status.pipeline_status_id'), nullable=False)
    multidataset = Column(Boolean, nullable=False, server_default=text("false"))
    readme = Column(Text)
    any_output_class = Column(Boolean, nullable=False, server_default=text("false"))

    group = relationship('GroupPypelines')
    pipeline_stage = relationship('PipelineStage')
    pipeline_status = relationship('PipelineStatus')
    user = relationship('TgUser')

    processes = relationship('Processes', secondary='process_pipeline')
    user_manual = Column(Text)
    pipeline_history = Column(Text)


class Processes(Base):
    __tablename__ = 'processes'
    __table_args__ = (
        CheckConstraint("namespace = ANY (ARRAY['scratch', 'archive'])"),
    )

    seq = Sequence('processes_process_id_seq', metadata=Base.metadata)

    process_id = Column(Integer, seq, primary_key=True)
    xml_config = deferred(Column(Text))
    session_id = Column(ForeignKey('session.session_id'), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    xml_before_run = Column(Text)
    namespace = Column(String(256))
    name = Column(String(40))
    process_dir = Column(String(64))
    expiration_time = Column(DateTime)
    id_site = Column(ForeignKey('processing_site.id_site'), server_default=text("1"))
    pype_input = deferred(Column(Text))
    comments = Column(Text)
    start_ingestion = Column(DateTime)
    end_ingestion = Column(DateTime)
    flag_published = Column(Boolean, server_default=text("false"))
    published_date = Column(DateTime)
    readme = Column(Text)
    instance = Column(String(80))
    flag_removed = Column(Boolean, server_default=text("false"))
    status_id = Column(ForeignKey('process_status.process_status_id'), nullable=False)
    size = Column(BigInteger)
    config_id = Column(ForeignKey('pipelines_config.config_id'))

    config = relationship('PipelinesConfig')
    processing_site = relationship('ProcessingSite')
    session = relationship('Session')
    process_status = relationship('ProcessStatus')

    fields = relationship('Fields', secondary='coadd.process_fields')
    inputs = relationship('Products', secondary='process_inputs')
    products = relationship('Products')
    process_comments = relationship('Comments')
    saved_processes = relationship('SavedProcesses', uselist=False, backref=backref("processes"))


class ProcessPipeline(Base):
    __tablename__ = 'process_pipeline'
    __table_args__ = (
        UniqueConstraint('pipeline_id', 'process_id'),
    )

    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    pipeline_id = Column(ForeignKey('pipelines.pipeline_id'), primary_key=True, nullable=False)
    version = Column(String(10), nullable=False)
    version_date = Column(DateTime)

    process = relationship('Processes', backref=backref("process_pipeline"))


class JobRuns(Base):
    __tablename__ = 'job_runs'
    __table_args__ = (
        CheckConstraint('rc = ANY (ARRAY[0, 1, 2, 3, 4, (-11), (-9)])'),
    )

    seq = Sequence('jobs_job_id_seq', metadata=Base.metadata)

    job_id = Column(Integer, seq, primary_key=True)
    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'), nullable=False)
    xml_config = Column(Text)
    parent_job_id = Column(ForeignKey('job_runs.job_id'))
    module_id = Column(ForeignKey('modules.module_id'), nullable=False)
    rc = Column(Integer, nullable=False)
    end_time = Column(DateTime)
    start_time = Column(DateTime)
    nc_ip = Column(String(15))
    hid = Column(String(10))

    module = relationship('Modules')
    parent_job = relationship('JobRuns', remote_side=[job_id])
    process = relationship('Processes')


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = (
        CheckConstraint('((file_id IS NOT NULL) AND (table_id IS NULL)) OR ((table_id IS NOT NULL) AND (file_id IS NULL))'),
    )

    seq = Sequence('products_product_id_seq', metadata=Base.metadata)

    product_id = Column(Integer, seq, primary_key=True)
    file_id = Column(ForeignKey('file_locator.file_id', ondelete='CASCADE'))
    job_id = Column(ForeignKey('job_runs.job_id', ondelete='CASCADE'), nullable=False)
    table_id = Column(ForeignKey('tables.table_id', ondelete='CASCADE'))
    class_id = Column(ForeignKey('product_class.class_id'), nullable=False)
    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'), nullable=False)
    flag_removed = Column(Boolean, nullable=False, server_default=text("false"))
    display_name = Column(String(75))
    version = Column(Integer)
    selected_name = Column(String(75))

    _class = relationship('ProductClass')
    file = relationship('FileLocator')
    job = relationship('JobRuns')
    table = relationship('Tables')
    process = relationship('Processes')


class ProcessInputs(Base):
    __tablename__ = 'process_inputs'

    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('products.product_id', ondelete='CASCADE'), primary_key=True, nullable=False)

    process = relationship('Processes', backref=backref("process_inputs"))
    products = relationship('Products', backref=backref("process_inputs"))


class ReleaseTag(Base):
    __tablename__ = 'release_tag'
    __table_args__ = {'schema': 'coadd'}

    seq = Sequence('coadd.release_tag_tag_id_seq', metadata=Base.metadata)

    tag_id = Column(Integer, seq, primary_key=True)
    name = Column(String(60), nullable=False, unique=True)
    version = Column(String(60))
    release_date = Column(Date)
    description = Column(Text)
    doc_url = Column(Text)
    release_display_name = Column(String(60))

    fields = relationship('Fields')


class Fields(Base):
    __tablename__ = 'fields'
    __table_args__ = {'schema': 'coadd'}

    seq = Sequence('coadd.fields_field_id_seq', metadata=Base.metadata)

    field_id = Column(Integer, seq, primary_key=True)
    field_name = Column(String(60), nullable=False, unique=True)
    display_name = Column(String(80))
    install_date = Column(Date)
    release_date = Column(Date)
    status = Column(Boolean)
    start_date = Column(Date)
    discovery_date = Column(Date, server_default=text("now()"))
    release_tag_id = Column(ForeignKey('coadd.release_tag.tag_id'), nullable=False)

    release_tag = relationship('ReleaseTag')


class ProcessFields(Base):
    __tablename__ = 'process_fields'
    __table_args__ = {'schema': 'coadd'}

    field_id = Column(ForeignKey('coadd.fields.field_id'), primary_key=True, nullable=False)
    process_id = Column(ForeignKey('processes.process_id'), primary_key=True, nullable=False)

    fields = relationship('Fields', backref=backref("coadd.process_fields"))


class PipelinesModules(Base):
    __tablename__ = 'pipelines_modules'

    pipeline_id = Column(ForeignKey('pipelines.pipeline_id'), primary_key=True, nullable=False)
    module_id = Column(ForeignKey('modules.module_id'), primary_key=True, nullable=False)
    xml_config = Column(Text)

    module = relationship('Modules')
    pipeline = relationship('Pipelines')


class PipelinesConfig(Base):
    __tablename__ = 'pipelines_config'

    seq = Sequence('pipelines_config_id_seq', metadata=Base.metadata)

    config_id = Column(Integer, seq, primary_key=True)
    owner_id = Column(ForeignKey('tg_user.user_id', ondelete='CASCADE'), nullable=False)
    name = Column(String(35), nullable=False, unique=True)
    description = Column(Text)
    comments = Column(Text)
    creation_date = Column(DateTime(True), nullable=False, server_default=text("now()"))
    last_time_used = Column(DateTime(True))
    pipeline_id = Column(ForeignKey('pipelines.pipeline_id'), nullable=False)
    default_date = Column(DateTime(True))
    xml_workflow = Column(Text)

    owner = relationship('TgUser')
    pipeline = relationship('Pipelines')


class ProcessComponent(Base):
    __tablename__ = 'process_component'

    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    module_id = Column(ForeignKey('modules.module_id'), primary_key=True, nullable=False)
    version = Column(String(10), nullable=False)
    version_date = Column(DateTime)

    module = relationship('Modules')
    process = relationship('Processes')


class Comments(Base):
    __tablename__ = 'comments'

    seq = Sequence('comments_comment_id_seq', metadata=Base.metadata)

    comment_id = Column(Integer, seq, primary_key=True)
    comments = Column(Text, nullable=False)
    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'))
    date = Column(DateTime, nullable=False)
    user_id = Column(ForeignKey('tg_user.user_id'), nullable=False)
    hid = Column(Float)
    hid_title = Column(Text)

    process = relationship('Processes')
    user = relationship('TgUser')


class SavedProcesses(Base):
    __tablename__ = 'saved_processes'

    process_id = Column(ForeignKey('processes.process_id', ondelete='CASCADE'), primary_key=True)
    saved_date = Column(DateTime, nullable=False, server_default=text("now()"))
    user_comments = Column(Text)
    saved_date_end = Column(DateTime)
    volume = Column(BigInteger)
    number_files = Column(Integer)


class Mask(Base):
    __tablename__ = 'mask'

    seq = Sequence('mask_mask_id_seq', metadata=Base.metadata)

    mask_id = Column(Integer, seq, primary_key=True)
    filter = Column(String(1), nullable=False)
    date = Column(DateTime, nullable=False)
    flag_removed = Column(Boolean, nullable=False, server_default=text("false"))
    tag_id = Column(ForeignKey('coadd.release_tag.tag_id'))
    field_id = Column(ForeignKey('coadd.fields.field_id'))
    table_id = Column(ForeignKey('tables.table_id', ondelete='CASCADE'), nullable=False)

    table = relationship('Tables')
    tag = relationship('ReleaseTag')
    field = relationship('Fields')


class CatalogStatus(Base):
    __tablename__ = 'catalog_status'

    seq = Sequence('catalog_status_status_id_seq', metadata=Base.metadata)

    status_id = Column(Integer, seq, primary_key=True)
    name = Column(String(16), nullable=False, unique=True)
    description = Column(String(64), nullable=False)


class Map(Base):
    __tablename__ = 'map'

    seq = Sequence('map_map_id_seq', metadata=Base.metadata)

    map_id = Column(Integer, seq, primary_key=True)
    tag_id = Column(ForeignKey('coadd.release_tag.tag_id'))
    nside = Column(Integer)
    filter = Column(String(10))
    date = Column(DateTime)
    flag_removed = Column(Boolean, server_default=text("false"))
    ordering = Column(String(8), nullable=False)
    field_id = Column(Integer)
    table_id = Column(ForeignKey('tables.table_id', ondelete='CASCADE'), nullable=False)
    image = Column(String(256))
    snr = Column(Integer)
    type = Column(String(54))
    magnitude = Column(String(54))

    table = relationship('Tables')
    tag = relationship('ReleaseTag')


class Catalog(Base):
    __tablename__ = 'catalog'

    seq = Sequence('catalog_catalog_id_seq', metadata=Base.metadata)

    catalog_id = Column(Integer, seq, primary_key=True)
    num_tiles = Column(Integer, nullable=False)
    num_objects = Column(BigInteger, nullable=False)
    num_columns = Column(Integer, nullable=False)
    visibility = Column(SmallInteger, nullable=False)
    catalog_name = Column(String(128))
    version = Column(String(128))
    ingestion_date = Column(DateTime)
    user_id = Column(Integer)
    description = Column(Text)
    status_id = Column(ForeignKey('catalog_status.status_id'), nullable=False)
    flag_removed = Column(Boolean, server_default=text("false"))
    table_id = Column(ForeignKey('tables.table_id', ondelete='CASCADE'), nullable=False)

    status = relationship('CatalogStatus')
    table = relationship('Tables')


class ProductField(Base):
    __tablename__ = 'product_field'

    field_id = Column(ForeignKey('coadd.fields.field_id'), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('products.product_id'), primary_key=True, nullable=False)

    fields = relationship('Fields', backref=backref("coadd.fields"))
    products = relationship('Products', backref=backref("products"))


class Filters(Base):
    __tablename__ = 'des'
    __table_args__ = {'schema': 'filters'}

    id = Column(Text, nullable=False)
    filter = Column(Text, primary_key=True, nullable=False)
    lambda_min = Column(Float)
    lambda_max = Column(Float)
    lambda_mean = Column(Float)


class ModuleInput(Base):
    __tablename__ = 'module_input'

    module_id = Column(ForeignKey('modules.module_id'), primary_key=True, nullable=False)
    input_class_id = Column(ForeignKey('product_class.class_id'), primary_key=True, nullable=False)
    optional = Column(Boolean, nullable=False, server_default=text("false"))
    multivalue = Column(Boolean, nullable=False, server_default=text("false"))
    exportable = Column(Boolean, nullable=False, server_default=text("false"))

    _class = relationship('ProductClass')
    module = relationship('Modules')


class ModuleOutput(Base):
    __tablename__ = 'module_output'

    module_id = Column(ForeignKey('modules.module_id'), primary_key=True, nullable=False)
    output_class_id = Column(ForeignKey('product_class.class_id'), primary_key=True, nullable=False)

    _class = relationship('ProductClass')
    module = relationship('Modules')


class PipelineInput(Base):
    __tablename__ = 'pipeline_input'
    __table_args__ = (
        UniqueConstraint('pipeline_id', 'module_id', 'input_class_id'),
    )

    pipeline_id = Column(ForeignKey('pipelines.pipeline_id', ondelete='CASCADE'), primary_key=True, nullable=False)
    module_id = Column(ForeignKey('modules.module_id'), primary_key=True, nullable=False)
    input_class_id = Column(ForeignKey('product_class.class_id'), primary_key=True, nullable=False)
    optional = Column(Boolean, nullable=False, server_default=text("false"))
    multivalue = Column(Boolean, nullable=False, server_default=text("false"))
    exportable = Column(Boolean, nullable=False, server_default=text("false"))
