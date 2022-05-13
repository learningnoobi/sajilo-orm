import psycopg2
# from sajilo_orm.settings import DB_SETTINGS
from sajilo_orm.exceptions import TableVetayenaKanchha,DatabaseConnectVayenaKanchha


class BaseManager:
    """
    This is the base manager which has database related function (like executing query )
    """

    cursor = None
    check_table = True
    DB_SETTINGS=None

    def __init__(self) -> None:
        try:
            self.connection = psycopg2.connect(**self.DB_SETTINGS)
            self.cursor = self.connection.cursor()
        except:
            raise DatabaseConnectVayenaKanchha



    def check_table_exists(self):
        self.cursor.execute(self.does_table_exits)
        return self.cursor.fetchone()[0] 

    def _execute_query(self, query):
        if not self.check_table_exists() and self.check_table:
            db_name = self.DB_SETTINGS["database"]
            raise TableVetayenaKanchha(self.table_name, db_name)
        self.cursor.execute(query)
        self.connection.commit()

    # def _return_queryset(self, data):
    #     result = [r for r in data]
    #     self.cols = [desc[0] for desc in self.cursor.description]
    #     queryset = [dict(zip(self.cols, i)) for i in result]
    #     return queryset
