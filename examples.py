"""
This shows example on how to use sajilo orm .

"""

from sajilo_orm.models import DamiModel
from sajilo_orm.field import Column
from sajilo_orm.manager import BaseManager
from sajilo_orm.settings import DB_SETTINGS


BaseManager.DB_SETTINGS = DB_SETTINGS
class Refree(DamiModel):
    table_ko_naam = "refree"

    name = Column("string", max_length="50")
    age = Column("integer")
    match_played = Column("integer")


def main():
    b = Refree.bata.khojera(id=1)[0]
    Refree.bata.data_fera(id=1)
    # print(b.__dict__)


if __name__ == "__main__":
    main()
    
