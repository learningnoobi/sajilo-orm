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
    won = Column("ho_ki_haina",default=True)


def main():

    #some operations you can perform with sajilo

    # create table
    Player.bata.table_banau()

    



    






    # print(b.__dict__)


if __name__ == "__main__":
    main()




# Making Python ORM that uses Nepali language (romanized)

# This last week , I decided to make a simple Python BaseM
# but I wanted to add Nepali based words in it . So I made this simple library called sajilo-orm which allows you to perform simple operations . (Shown below)

# Github: https://lnkd.in/g-Gxy96M
# Pypi: https://lnkd.in/g4QjxXn5

# #python #github #orm #nepali

