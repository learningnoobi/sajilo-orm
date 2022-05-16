from typing import Type
from sajilo_orm.query_manager import QueryManager
from tests import (Column,
        cursor,
        DamiModel, 
        TableVetayenaKanchha,
        ColumnNaiXainaKanchha,
        IdXainaKanchha,
        NotNullMaDataVayenaKanchha,
        DateFormatMilenaKanchha,
        SyntaxBigryoKanchha,
        MaxLengthVayenaKanchha
        )
import pytest

# Use test db since we will be dropping every table at first


class Refree(DamiModel):
    table_ko_naam = "refree"

    name = Column("string", max_length="50")
    age = Column("anka")
    whens = Column("miti",default='aja_ko_date')
    won = Column("ho_ki_haina",default="haina",null=False)
    match_played = Column("anka")



# T his Student model is to check field and Column section only
# basically using all the field with all the case (like null=True,default="example")
# to ensure every case is working
class Student(DamiModel):
    table_ko_naam = "students"

    name = Column("string", max_length="50",default="hero")
    bio = Column("string", max_length="50",null=False )
    graduate = Column("ho_ki_haina",default="ho")
    fail_vako = Column("ho_ki_haina",default="haina")
    whens = Column("miti",default='aja_ko_date')
    kaile = Column("miti",default='2000-01-01')
    match_played = Column("anka",default=69)



class Random(DamiModel):
    table_ko_naam = "random"
    name = Column("string",max_length="34") 

class Boy(DamiModel):
    table_ko_naam = "random"
    name = Column("string") #no max_legnth then error must come


def test_table_xaina(cursor):
    assert Refree.bata.check_table_exists() == False


def test_table_banau(cursor):
    Refree.bata.table_banau()
    assert Refree.bata.check_table_exists() == True


def test_table_vetayena(cursor):
    with pytest.raises(TableVetayenaKanchha) as exc_info:
        Random.bata.sabaideu()


def test_crud_operations(cursor):
    from datetime import date

    today = date.today()
    # today = today.strftime("%Y-%m-%d")
    Refree.bata.table_banau()
    Student.bata.table_banau()

    # LIST
    assert Refree.bata.sabaideu() == []

    # INSERT
    Refree.ma.data_hala(name="bishal", age=21, match_played=69,won=False)
    Refree.ma.data_hala(name="rayon", age=34, match_played=9,won=True)
    b = Refree.bata.sabaideu()
    assert len(b) == 2

    # filter

    filter = Refree.bata.khojera(id=1)[0]
    assert repr(filter) == "<refree : 1 >"

    assert filter.name == "bishal"
    assert filter.age != 23

    # RETRIEVE
    print(b[0].__dict__)
    assert b[0].__dict__ == {"id": 1, "age": 21, "match_played": 69, "name": "bishal","won":False,"whens":today}

    # DELETE
    Refree.bata.data_fala(id=2)
    assert len(Refree.bata.sabaideu()) == 1


def test_exception_error(cursor):
    Refree.bata.table_banau()
    with pytest.raises(ColumnNaiXainaKanchha):
        Refree.ma.data_hala(nama="rayon", umer=34, kheleko=9)

    with pytest.raises(ColumnNaiXainaKanchha):
        Refree.ma.data_fala(nama="rayon", umer=34, kheleko=9)

    with pytest.raises(NotNullMaDataVayenaKanchha):
        Refree.bata.data_hala(age=31, match_played=999)
        
    with pytest.raises(MaxLengthVayenaKanchha):
        Boy.bata.table_banau()

    with pytest.raises(DateFormatMilenaKanchha):
        Refree.bata.data_hala(name='kagura' ,age=31, match_played=999,whens='12012')

    

    


def test_data_update(cursor):
    Refree.bata.table_banau()
    Refree.ma.data_hala(name="bishal", age=21, match_played=69,won=True)
    first_ref = Refree.bata.khojera(id=1)[0]
    
    assert first_ref.id == 1
    assert first_ref.name == "bishal"
    assert first_ref.age == 21
    assert first_ref.match_played == 69

    # data ferne
    Refree.bata.data_fera(id=1, name="gintoki", age=31, match_played=999)
    first_ref = Refree.bata.khojera(id=1)[0]
    assert first_ref.id == 1
    assert first_ref.name == "gintoki"
    assert first_ref.age == 31
    assert first_ref.match_played == 999

    with pytest.raises(ColumnNaiXainaKanchha):
        Refree.bata.data_fera(id=1, jpt_column="gintoki")

    with pytest.raises(IdXainaKanchha):
        Refree.bata.data_fera(name="sinpachi")

    with pytest.raises(IdXainaKanchha):
        Refree.bata.data_fera()
    
    with pytest.raises(SyntaxBigryoKanchha):
        Refree.bata.data_fera(id=1)

def test_table_fala(cursor):
    Refree.bata.table_banau()
    Random.bata.table_banau()
    assert Refree.bata.check_table_exists() == True
    Refree.lai.fala()
    assert Refree.bata.check_table_exists() == False
    assert Random.bata.check_table_exists() == True
    Random.lai.fala()
    assert Random.bata.check_table_exists() == False




