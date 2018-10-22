from graphene import Int, String, Boolean, DateTime, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import GroupPypelines as GroupPypelinesModel


class GroupPypelinesAttribute():
    group_id = Int(description="Group ID number")
    name = String(description="Group name")
    parent_group_id = Int(description="Parent Group ID number")
    order_number = Int(description="Order of the group in menu")
    display_name = String(description="Group name displayed")


class GroupPypelines(SQLAlchemyObjectType, GroupPypelinesAttribute):
    """GroupPypelines node"""

    class Meta:
        model = GroupPypelinesModel
        interfaces = (relay.Node,)