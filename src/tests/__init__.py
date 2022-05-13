from sajilo_orm.models import DamiModel
from sajilo_orm.field import Column
from sajilo_orm.manager import BaseManager
from sajilo_orm.exceptions import *
import pytest

TEST_DB_SETTINGS = {
    "database": "testdb",
    "user": "bishal",
    "password": "rayon123",
    "host": "localhost",
    "port": "5432",
}



BaseManager.DB_SETTINGS = TEST_DB_SETTINGS

@pytest.fixture(scope="module")
def cursor():
    b = BaseManager()
    yield b.cursor
    b.cursor = b.connection.cursor()
    #Drop all tables after a test
    b.cursor.execute(f'''
            DO $$ DECLARE
            r RECORD;
        BEGIN
            FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
                EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
            END LOOP;
        END $$;
    ''')
    b.connection.commit()
    b.connection.close()
   
    