from graphene import Int, String, Boolean, DateTime, List, relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import JobRuns as JobRunsModel


class JobRunsAttribute():
    job_id = Int()
    process_id = Int()
    xml_config = String()
    parent_job_id = Int()
    module_id = Int()
    rc = Int()
    end_time = DateTime()
    start_time = DateTime()
    nc_ip = String()
    hid = String()


class JobRuns(SQLAlchemyObjectType, JobRunsAttribute):
    """JobRuns node"""

    class Meta:
        model = JobRunsModel
        interfaces = (relay.Node,)
