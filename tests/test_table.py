from sajilo_orm.query_manager import QueryManager
from tests import Column, cursor, DamiModel, TableVetayenaKanchha,ColumnNaiXainaKanchha
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

def test_data_hala_ani_sabaideu(cursor):
    Refree.bata.table_banau()
    
    assert Refree.bata.sabaideu() == []    
    Refree.ma.data_hala(name="bishal",age=21,match_played=69)
    Refree.ma.data_hala(name="rayon",age=34,match_played=9)
    b = Refree.bata.sabaideu()

    assert len(b) == 2
    assert b[0].__dict__ == {'id':1,'age':21,'match_played':69,'name':'bishal'}

    with pytest.raises(ColumnNaiXainaKanchha) as e:
        Refree.ma.data_hala(nama="rayon",umer=34,kheleko=9)   
    


    
