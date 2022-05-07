import psycopg2
from sajilo_orm.settings import DB_SETTINGS
from sajilo_orm.exceptions import TableVetayenaKanchha



class BaseManager:
    '''
    This is the base manager which has database related function (like executing query )
    '''
    def _connect_database(self) -> None:
        connection = psycopg2.connect(**DB_SETTINGS)
        self.cursor = connection.cursor()

    def _execute_query(self, query) :
        self._connect_database()
        self.cursor.execute(self.does_table_exits)

        if not self.cursor.fetchone()[0]:
            db_name = DB_SETTINGS["database"]
            raise TableVetayenaKanchha(self.model_class,db_name)
        self.cursor.execute(query)


    def _return_queryset(self,data):
        result = [r for r in data]
        self.cols = [desc[0] for desc in self.cursor.description]
        
        queryset = []

        for i in result:
            dictresult = dict(zip(self.cols, i))
            queryset.append(dictresult)

        return queryset
