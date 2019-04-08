from graphene import Int, Enum, Connection as graphConn
from sqlalchemy.inspection import inspect


class Connection(graphConn):
    class Meta:
        abstract = True

    total_count = Int()

    def resolve_total_count(self, info):
        return self.length


def sort_enum_for(cls):
   """Create Graphene Enum for sorting a SQLAlchemy class query"""

   name = cls.__name__+'SortEnum' 
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