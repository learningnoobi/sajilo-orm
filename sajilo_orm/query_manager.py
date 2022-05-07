from sajilo_orm.manager import BaseManager


class QueryManager(BaseManager):
    cursor = None
    columns = None

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

    
