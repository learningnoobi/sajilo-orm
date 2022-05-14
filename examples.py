"""
This shows example on how to use sajilo orm .
"""

from email.policy import default
from sajilo_orm.models import DamiModel
from sajilo_orm.field import Column
from sajilo_orm.manager import BaseManager
from sajilo_orm.settings import DB_SETTINGS


BaseManager.DB_SETTINGS = DB_SETTINGS
class Boy(DamiModel):
    table_ko_naam = "boy"

    name = Column("string", max_length="50",null=False)
    age = Column("anka",null=True,default=34)
    match_played = Column("miti")
    aja_date = Column("miti",default='aja_ko_date')
    won = Column("ho_ki_haina",default=True)


def main():
    Boy.bata.table_banau()
    Boy.ma.data_hala(match_played='2001-01-01',won=False)
    # print(b.__dict__)


if __name__ == "__main__":
    main()