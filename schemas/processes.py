from graphene import Int, String, Boolean, DateTime, List, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from schemas.fields import Fields
from models import Processes as ProcessesModel


class ProcessesAttribute():
    process_id = Int()
    xml_config = String()
    session_id = Int()
    start_time = DateTime()
    end_time = DateTime()
    xml_before_run = String()
    namespace = String()
    name = String()
    process_dir = String()
    expiration_time = DateTime()
    id_site = String()
    pype_input = String()
    comments = String()
    start_ingestion = DateTime()
    end_ingestion = DateTime()
    flag_published = Boolean()
    published_date = DateTime()
    readme = String()
    instance = String()
    flag_removed = Boolean()
    status_id = Int()
    size = Int()
    config_id = Int()
    fields = List(lambda: Fields)


class Processes(SQLAlchemyObjectType, ProcessesAttribute):
    """Processes node"""

    class Meta:
        model = ProcessesModel
        interfaces = (relay.Node,)