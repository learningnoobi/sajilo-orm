"""
This shows example on how to use sajilo orm .
"""

from email.policy import default
from sajilo_orm.models import DamiModel
from sajilo_orm.field import Column
from sajilo_orm.manager import BaseManager
from sajilo_orm.settings import DB_SETTINGS


BaseManager.DB_SETTINGS = DB_SETTINGS


from sajilo_orm.models import DamiModel

class Player(DamiModel):
    table_ko_naam = "boy"

    name = Column("string", max_length="50",null=False)
    name = Column("string",null=False)
    age = Column("anka",null=True,default=34)
    match_played = Column("miti")
    aja_date = Column("miti",default='aja_ko_date')
    won = Column("ho_ki_haina",default=True,max_length="34")


def main():

    #some operations you can perform with sajilo

    # create table
    Player.bata.table_banau()


if __name__ == "__main__":
    main()



