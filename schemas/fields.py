from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

import models
from schemas.release_tag import ReleaseTag

import utils


class FieldsAttribute():

    field_id = Int(description='Field ID')
    field_name = String(description='Field name')
    display_name = String(description='Field ID')
    install_date = DateTime(description='Instalation date')
    release_date = DateTime(description='Release date')
    status = Boolean(description='Field status: true = available / false = unavailable')
    start_date = DateTime(description='Start date')
    discovery_date = DateTime(description='Discovery date')
    release_tag_id = Int(description='Release ID')


class Fields(SQLAlchemyObjectType, FieldsAttribute):
    """Fields Tag node"""
    
    data_loader_release_tag = utils.DataLoaderOneToOne(
        models.Fields, models.ReleaseTag)

    def resolve_release_tag(self, info):
        return Fields.data_loader_release_tag.load(self.field_id)

    class Meta:
        model = models.Fields
        interfaces = (relay.Node,)
