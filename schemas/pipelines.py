from graphene import Int, String, Boolean, DateTime, List, Field, ObjectType, relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Pipelines as PipelinesModel
from schemas.processes import Processes


class PipelinesAttribute():
    pipeline_id = Int(description="Pipeline unique ID number")
    name = String(description="Pipeline name")
    display_name = String(description="Pipeline name displayed")
    group_id = Int(description="Group ID number")
    order_number = Int(description="Order of the pipeline in menu")
    user_id = Int(description="User ID number")
    version = String(description="Version number")
    version_date = DateTime(description="Version date")
    description = String(description="Pipeline description")
    pipeline_stage_id = Int(description="Stage ID number")
    xml_workflow = String(description="Components workflow of pipeline")
    pipeline_status_id = Int(description="Status ID number")
    multidataset = Boolean(description="Allows multiple datasets to be used if true")
    readme = String(description="Document describing how the pipeline works.")
    any_output_class = Boolean()
    processes = List(lambda: Processes) 


class Pipelines(SQLAlchemyObjectType, PipelinesAttribute):
    """Pipelines node"""

    
    class Meta:
        model = PipelinesModel
        interfaces = (relay.Node,)