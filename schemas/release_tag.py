from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import ReleaseTag as ReleaseTagModel


class ReleaseTagAttribute():

    tag_id = Int(description="Tag unique ID number")
    name = String(description="Pipeline name")
    version = String(description="Version number")
    release_date = DateTime(description="Release date")
    description = String(description="Tag description")
    doc_url = String(description="URL to documentation")
    release_display_name = String(description="Tag name displayed")


class ReleaseTag(SQLAlchemyObjectType, ReleaseTagAttribute):
    """Release Tag node"""

    class Meta:
        model = ReleaseTagModel
        interfaces = (relay.Node,)