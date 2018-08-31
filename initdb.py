# coding: utf-8

from database import engine, db_session
from models import ProductType, ProductClass
import json


def has_table(tablename):
    """ Check if the table exists in the database
    
    Arguments:
        tablename {str} -- tablename
    
    Returns:
        boolean -- True has table, False not has table
    """
            
    return engine.dialect.has_table(engine, tablename)


def ingest_json(class_table):
    """ Ingest tests json in database
    
    Arguments:
        class_table {class} -- sqlalchemy model (DeclarativeMeta)
    """


    with open('{}/{}.json'.format(
        'tests/data', class_table.__tablename__
    )) as json_file:
        data = json.load(json_file)

    db_session.bulk_insert_mappings(
        class_table, [dict(i) for i in data]
    )
    db_session.commit()


if not has_table(tablename=ProductType.__tablename__):
    ProductType.metadata.create_all(bind=engine, tables=[ProductType.__table__])
    ingest_json(ProductType)

if not has_table(tablename=ProductClass.__tablename__):
    ProductClass.metadata.create_all(bind=engine, tables=[ProductClass.__table__])
    ingest_json(ProductClass)