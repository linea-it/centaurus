from graphene import Int, Enum, List, Connection as graphConn
from sqlalchemy.inspection import inspect
from sqlalchemy import or_, String as String_
from sqlalchemy.sql.expression import cast

from database import db_session

from promise import Promise
from promise.dataloader import DataLoader


class Connection(graphConn):
    class Meta:
        abstract = True

    total_count = Int()

    def resolve_total_count(self, info):
        return self.length


def sort_enum_for(models):
    """Create Graphene Enum for sorting a SQLAlchemy class query"""

    if not isinstance(models, list):
        models = [models]

    items = list()
    for cls in models:
        for attr in inspect(cls).attrs:
            try:
                asc = attr.expression
                desc = asc.desc()
            except AttributeError as error:
                pass
            else:
                key = attr.key.lower()
                items.extend([(cls.__name__.lower() + '_' + key + '_asc', asc),
                              (cls.__name__.lower() + '_' + key + '_desc', desc)])

    return List(Enum(models[0].__name__ + 'SortEnum', items))


def column_from_classes(models):
    """Create Graphene List to select the columns from SQLAlchemy classes"""

    if not isinstance(models, list):
        models = [models]

    items = list()
    for model in models:
        try:
            for col in model.__table__.c:
                items.extend([(str(col).replace('.', '_'), col)])
        except AttributeError as error:
            raise(error)

    return List(Enum(models[0].__name__ + 'SearchEnum', items))


def selected_tables_from_arguments(*argv):
    tables = set()
    for _filters in argv:
        if _filters:
            for _filter in _filters:
                tables.add(str(_filter).split('.')[0])
    return tables

    
def is_valid_search(search):
    return search and 'text' in search and 'columns' in search


def prepare_sqlalchemy_filters_casting_columns_to_str(search):
    _filters = list()
    if is_valid_search(search):
        _filters = [cast(column, String_).ilike("%{}%".format(
            search['text'])) for column in search['columns']]
    return _filters


class DataLoaderOneToOne(DataLoader):
    def __init__(self, inner_model, outer_model, pk_inner_model=None):
        DataLoader.__init__(self)
        self._inner_model = inner_model
        self._outer_model = outer_model
        if pk_inner_model:
            self._pk_inner_model = pk_inner_model
        else:
            self._pk_inner_model = getattr(
                self._inner_model, inspect(
                    self._inner_model).primary_key[0].name)

    def batch_load_fn(self, keys):
        pk_model = db_session.query(self._pk_inner_model, self._outer_model).\
            join(self._outer_model).\
            filter(self._pk_inner_model.in_(keys)).all()

        d = dict.fromkeys(keys)
        for pp in pk_model:
            d[pp[0]] = pp[1]

        return Promise.resolve([d[key] for key in keys])


class DataLoaderOneToMany(DataLoader):
    def __init__(
            self,
            inner_model,
            secondary_model,
            outer_model,
            pk_inner_model=None):
        DataLoader.__init__(self)
        self._inner_model = inner_model
        self._secondary_model = secondary_model
        self._outer_model = outer_model
        if pk_inner_model:
            self._pk_inner_model = pk_inner_model
        else:
            self._pk_inner_model = getattr(
                self._inner_model, inspect(
                    self._inner_model).primary_key[0].name)

    def batch_load_fn(self, keys):
        pk_model = db_session.query(self._pk_inner_model, self._outer_model).\
            join(self._secondary_model).\
            join(self._outer_model).\
            filter(self._pk_inner_model.in_(keys)).all()
        d = dict([(key, []) for key in keys])
        for pp in pk_model:
            d[pp[0]].append(pp[1])

        return Promise.resolve([d[key] for key in keys])
