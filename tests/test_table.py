from sajilo_orm.query_manager import QueryManager
from tests import Column, cursor, DamiModel, TableVetayenaKanchha
import pytest

#Use test db since we will be dropping every table at first




class Refree(DamiModel):
    table_ko_naam = "refree"

    name = Column("string", max_length="50")
    age = Column("integer")
    match_played = Column("integer")


class Random(DamiModel):
    table_ko_naam = "random"
    name = Column("string", max_length="50")



def test_table_xaina(cursor):
    assert Refree.bata.check_table_exists() == False


def test_table_banau(cursor):
    Refree.bata.table_banau()
    assert Refree.bata.check_table_exists() ==True


def test_table_vetayena(cursor):
    with pytest.raises(TableVetayenaKanchha) as exc_info:   
        Random.bata.sabaideu()
    
