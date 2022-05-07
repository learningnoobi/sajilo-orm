from sajilo_orm.manager import BaseManager



class QueryManager(BaseManager):
    cursor = None

    def __init__(self, model_class) -> None:
        self.model_class = model_class
        self.does_table_exits = f"""select exists(select relname from pg_class 
                where relname = '{self.model_class}' and relkind='r');"""
    

    def sabaideu(self, size=2000):
        '''Gives all Data of the table'''

        query = f"""
            SELECT * FROM {self.model_class} ;
        """
        self._execute_query(query)
        data = self.cursor.fetchall()
        return self._return_queryset(data)
        
    
    def khojera(self, con="and",**condition):
        """ Filters the queryset from the ocondition """

        query = f"""
            SELECT * FROM {self.model_class} 
        """   

        condition_query=''
        for key,value in condition.items(): 
            condition_query = condition_query+f"{key} = '{value}' {con} " if isinstance(value,str) else condition_query + f"{key} = {value} {con}"
            
        query +=f"WHERE {condition_query[:-3]};"
        self._execute_query(query)
        data = self.cursor.fetchall()
        return self._return_queryset(data)
    

    def data_hala(self,**data):
        ''' Insert Value In Given Table '''
        keys,value_data = list(),list()
        for key,value in data.items():
            keys.append(key),value_data.append(value)

        keys = ','.join(keys) 
        value_data_str=f'{tuple(value_data)}'
        value_data =value_data_str[:-2]+")" if len(value_data)==1 else value_data_str        

        query = f""" INSERT INTO {self.model_class} ({keys}) values {value_data} """
        self._execute_query(query)
        

     



# from psycopg2.extras import execute_values
# execute_values(cur,
#     "INSERT INTO test (id, v1, v2) VALUES %s",
#     [(1, 2, 3), (4, 5, 6), (7, 8, 9)])