from graphene import Int, String, Boolean, DateTime, List, Field, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import Processes as ProcessesModel
import os

SCIENCE_URL = os.getenv('SCIENCE_URL')


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
    product_log = String()


class Processes(SQLAlchemyObjectType, ProcessesAttribute):
    """Processes node"""


    class Meta:
        model = ProcessesModel
        interfaces = (relay.Node,)


    def resolve_product_log(self, info):
        """ Mount the product_log link """

        return os.path.join(
            SCIENCE_URL,
            "VP/getViewProcessCon?process_id=%s" % self.process_id
        )
