import psycopg2
from sajilo_orm.settings import DB_SETTINGS
from sajilo_orm.exceptions import TableVetayenaKanchha



class BaseManager:
    def _connect_database(self) -> None:
        connection = psycopg2.connect(**DB_SETTINGS)
        self.cursor = connection.cursor()

    def _execute_query(self, query) :
        self._connect_database()
        self.cursor.execute(self.does_table_exits)

        if not self.cursor.fetchone()[0]:
            db_name = DB_SETTINGS["database"]
            raise TableVetayenaKanchha(f"Timle deko table '{self.model_class}' {db_name} vanne database ma nai vetayena ! Spelling bigryo ki herata ramro sanga !")
        self.cursor.execute(query)

    def _return_queryset(self,data):
        result = [r for r in data]
        self.cols = [desc[0] for desc in self.cursor.description]
        
        queryset = []

        for i in result:
            dictresult = dict(zip(self.cols, i))
            queryset.append(dictresult)

        return queryset
