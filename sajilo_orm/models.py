from sajilo_orm.field import Column
from sajilo_orm.query_manager import QueryManager
import inspect


class MetaModel(type):
    @property
    def bata(self):
        return QueryManager(model_class=self)

    @property
    def ma(self):
        return QueryManager(model_class=self)


class DamiModel(metaclass=MetaModel):
    table_ko_naam = None
    fields = ["id"]

    def __init__(self) -> None:
        for name, field in inspect.getmembers(self):
            if isinstance(field, Column):
                self.fields.append(name)

    def setData(self, tup):
        for i, j in enumerate(tup):
            b = self.fields[i]
            setattr(self, b, j)

    def __repr__(self) -> str:
        return f"<{self.table_ko_naam} : {self.id} >"
