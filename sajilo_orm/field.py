
sql_type = {
    "integer":"INT",
    "string":"VARCHAR({})"
}

class Column:
    constraint = {}
    def __init__(self,data_type,**kwargs):
        self.data_type = data_type

        self.constraint = kwargs

    @property
    def _get_sql_type(self):
        if self.data_type == "string":
            return sql_type[self.data_type].format(self.constraint["max_length"])
        
        if self.data_type == "integer":
            return sql_type[self.data_type]

