from graphene import Int, String, Boolean, DateTime, List, Field, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import SavedProcesses as SavedProcessesModel
import os


class SavedProcessesAttribute():
    process_id = Int()
    saved_date = DateTime()
    user_comments = String()
    saved_date_end = DateTime()
    volume = Int()
    number_files = Int()


class SavedProcesses(SQLAlchemyObjectType, SavedProcessesAttribute):
    """SavedProcesses node"""


    class Meta:
        model = SavedProcessesModel
        interfaces = (relay.Node,)
