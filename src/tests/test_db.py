from tests import  BaseManager, TEST_DB_SETTINGS, DatabaseConnectVayenaKanchha
import pytest




def test_fail_database_connection():
    BaseManager.DB_SETTINGS = {"jpt":"connection"}
    with pytest.raises(DatabaseConnectVayenaKanchha) as exc_info:   
        BaseManager()
    
    assert "Arrey !! Database ta ramrari connect gara paila !!" in str(exc_info.value)


def test_success_database_connection():
    BaseManager.DB_SETTINGS = TEST_DB_SETTINGS
    BaseManager()