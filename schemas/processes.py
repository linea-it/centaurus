from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models

import utils
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
    session_loader = utils.DataLoaderOneToOne(models.Processes, models.Session)
    fields_loader = utils.DataLoaderOneToMany(
        models.Processes, models.ProcessFields, models.Fields)
    inputs_loader = utils.DataLoaderOneToMany(
        models.Processes, models.ProcessInputs, models.Products)

    def resolve_session(self, info):
        return Processes.session_loader.load(self.process_id)

    def resolve_fields(self, info):
        return Processes.fields_loader.load(self.process_id)

    def resolve_inputs(self, info):
        return Processes.inputs_loader.load(self.process_id)

    class Meta:
        model = models.Processes
        interfaces = (relay.Node,)
        connection_class = utils.Connection

    def resolve_product_log(self, info):
        """ Mount the product_log link """

        return os.path.join(
            SCIENCE_URL,
            "VP/getViewProcessCon?process_id={}".format(self.process_id)
        )
