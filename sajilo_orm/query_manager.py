from operator import concat
from sajilo_orm.exceptions import (ColumnNaiXainaKanchha, DateFormatMilenaKanchha, IdXainaKanchha, NotNullMaDataVayenaKanchha, SyntaxBigryoKanchha)
import psycopg2
from sajilo_orm.manager import BaseManager
import psycopg2
from sajilo_orm import (
    CHECK_TABLE,
    CREATE_TABLE,
    SELECT_ALL,
    INSERT_INTO,
    DELETE_ALL,
    UPDATE,
    DROP_TABLE
)


class QueryManager(BaseManager):
    table_name = None

    def __init__(self, model_class) -> None:
        super().__init__()
        self.model_class = model_class
        self.table_name = model_class.table_ko_naam
        self.does_table_exits = CHECK_TABLE.format(self.table_name)

    def get_columns(self):
        import inspect
        from sajilo_orm.field import Column

        fields = [("id", "SERIAL PRIMARY KEY")]
        for name, field in inspect.getmembers(self.model_class):
            if isinstance(field, Column):
                fields.append((name, field._get_sql_type))
        return fields

    def table_banau(self):
        self.check_table = False
        fields = self.get_columns()
        self.base_q = [" ".join(i) for i in fields]
        query = CREATE_TABLE.format(self.table_name, " , ".join(self.base_q))
        # print(query)
        self._execute_query(query)
        

    def give_object_list(self, data):
        querysets = []
        for da in data:
            b = self.model_class()
            b.setData(da)
            querysets.append(b)
        return querysets

    def sabaideu(self):
        """Gives all Data of the table"""

        query = SELECT_ALL.format(self.table_name)
        self._execute_query(query)
        data = self.cursor.fetchall()
        return self.give_object_list(data)

    def _give_condition_query(self, con, **condition):
        condition_query = ""
        for key, value in condition.items():
            condition_query = (
                condition_query + f"{key} = '{value}' {con} "
                if isinstance(value, str)
                else condition_query + f"{key} = {value} {con}"
            )
        return condition_query

    def khojera(self, con="and", **condition):
        """Filters the queryset from the ocondition"""

        query = SELECT_ALL.format(self.table_name)
        condition_query = self._give_condition_query(con, **condition)
        query += f"WHERE {condition_query[:-3]};"
        self._execute_query(query)
        data = self.cursor.fetchall()
        return self.give_object_list(data)

    def data_hala(self, **data):
        """Insert Value In Given Table"""

        keys, value_data = list(), list()
        for key, value in data.items():
            keys.append(key), value_data.append(value)

        keys = ",".join(keys)
        value_data_str = f"{tuple(value_data)}"
        value_data = (
            value_data_str[:-2] + ")" if len(value_data) == 1 else value_data_str
        )

        query = INSERT_INTO.format(self.table_name, keys, value_data)
        try:
            self._execute_query(query)

        except psycopg2.errors.UndefinedColumn:
            raise ColumnNaiXainaKanchha(self.table_name)
        
        except psycopg2.errors.InvalidDatetimeFormat:
            raise DateFormatMilenaKanchha

        except psycopg2.errors.NotNullViolation: 
            raise NotNullMaDataVayenaKanchha


    #delete data
    def data_fala(self, con="and ", **condition):
        query = DELETE_ALL.format(self.table_name)
        if len(condition) > 0:
            condition_query = self._give_condition_query(con, **condition)
            query += f"WHERE {condition_query[:-4]} ;"
        try:
            self._execute_query(query)
        except psycopg2.errors.UndefinedColumn:
            raise ColumnNaiXainaKanchha(self.table_name)

    #update data
    def data_fera(self, **condition):
        try:
            pk = condition.pop("id")
        except KeyError:
            raise IdXainaKanchha
        condition_query = self._give_condition_query(",", **condition)[:-2]
        query = UPDATE.format(self.table_name,condition_query,f'id = {pk}' )
        try:
            self._execute_query(query)
        except psycopg2.errors.UndefinedColumn:
            raise ColumnNaiXainaKanchha(self.table_name)
        
        except psycopg2.errors.SyntaxError: 
            raise SyntaxBigryoKanchha
    
    #delete table
    def fala(self):
        query = DROP_TABLE.format(self.table_name)
        self._execute_query(query)
    



