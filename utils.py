from graphene import Int, Enum, Connection as graphConn
from sqlalchemy.inspection import inspect

from database import db_session
import collections

from promise import Promise
from promise.dataloader import DataLoader

import sys


class Connection(graphConn):
    class Meta:
        abstract = True

    total_count = Int()

    def resolve_total_count(self, info):
        return self.length


def sort_enum_for(cls):
    """Create Graphene Enum for sorting a SQLAlchemy class query"""

    name = cls.__name__ + 'SortEnum'
    items = list()

    for attr in inspect(cls).attrs:
        try:
            asc = attr.expression
            desc = asc.desc()
        except AttributeError as error:
            pass
        else:
            key = attr.key.lower()
            items.extend([(key + '_asc', asc), (key + '_desc', desc)])

    return Enum(name, items)


class DataLoaderOneToOne(DataLoader):
    def __init__(self, inner_model, outer_model, pk_inner_model=None):
        DataLoader.__init__(self)
        self._inner_model = inner_model
        self._outer_model = outer_model
        if pk_inner_model:
            self._pk_inner_model = pk_inner_model
        else:
            self._pk_inner_model = getattr(self._inner_model, inspect(self._inner_model).primary_key[0].name)

    def batch_load_fn(self, keys):
        pk_model = db_session.query(self._pk_inner_model, self._outer_model).\
            join(self._outer_model).\
            filter(self._pk_inner_model.in_(keys)).all()

        d = dict.fromkeys(keys)
        for pp in pk_model:
            d[pp[0]] = pp[1]

        return Promise.resolve([d[key] for key in keys])


class DataLoaderOneToMany(DataLoader):
    def __init__(self, inner_model, secondary_model, outer_model, pk_inner_model=None):
        DataLoader.__init__(self)
        self._inner_model = inner_model
        self._secondary_model = secondary_model
        self._outer_model = outer_model
        if pk_inner_model:
            self._pk_inner_model = pk_inner_model
        else:
            self._pk_inner_model = getattr(self._inner_model, inspect(self._inner_model).primary_key[0].name)

    def batch_load_fn(self, keys):
        pk_model = db_session.query(self._pk_inner_model, self._outer_model).\
            join(self._secondary_model).\
            join(self._outer_model).\
            filter(self._pk_inner_model.in_(keys)).all()
        d = dict([(key, []) for key in keys])
        for pp in pk_model:
            d[pp[0]].append(pp[1])

        return Promise.resolve([d[key] for key in keys])