import psycopg2
from sajilo_orm.settings import DB_SETTINGS
from sajilo_orm.exceptions import TableVetayenaKanchha



class BaseManager:
    '''
    This is the base manager which has database related function (like executing query )
    '''
    cursor = None
    check_table =True
    

    def __init__(self) -> None:
        self.connection = psycopg2.connect(**DB_SETTINGS)
        self.cursor = self.connection.cursor()

    def _execute_query(self, query) :
        self.cursor.execute(self.does_table_exits)

        if not self.cursor.fetchone()[0] and self.check_table:
            db_name = DB_SETTINGS["database"]
            raise TableVetayenaKanchha(self.table_name,db_name)
        self.cursor.execute(query)
        self.connection.commit()


    def _return_queryset(self,data):
        result = [r for r in data]
        self.cols = [desc[0] for desc in self.cursor.description]
        queryset = [dict(zip(self.cols, i)) for i in result] 
        return queryset
