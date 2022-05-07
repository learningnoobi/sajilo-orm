
from sajilo_orm.query_manager import QueryManager


class MetaModel(type):
    @property
    def bata(self):
        return QueryManager(model_class=self.table_ko_naam)


class DamiModel(metaclass=MetaModel):
    table_ko_naam = ""
