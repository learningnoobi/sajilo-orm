"""
This shows example on how to use sajilo orm .

"""

from sajilo_orm.models import DamiModel

from sajilo_orm.field import Column


class Refree(DamiModel):
    table_ko_naam = "refree"

    name = Column("string",max_length="50")
    age = Column("integer")
    match_played = Column("integer")


def main():

    b =Refree.bata.khojera(id=1)[0]
    print(b.__dict__)


if __name__ == "__main__":
    main()
