from sajilo_orm.field import Column
from sajilo_orm.query_manager import QueryManager
import inspect


class MetaModel(type):
    """
        Main Metaclass
        
        bata , ma and lai has exactly same methods and operations.
        It is just to make query gramatically correct in Nepali
        For eg:
         Table.bata.sabaideu() sounds correct
         Table.bata.data_hala(**data) doesnot sound that good
         But Table.ma.data_hal() sounds correct

         Same With:
           Table.bata.fala() will work and drop all table but
           Table.lai.fala() sounds more correct

    """
    @property
    def bata(self):
        return QueryManager(model_class=self)

    @property
    def ma(self):
        return QueryManager(model_class=self)

    @property
    def lai(self):
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
