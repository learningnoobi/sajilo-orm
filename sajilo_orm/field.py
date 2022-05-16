
from sajilo_orm.exceptions import MaxLengthVayenaKanchha


sql_type = {
    "anka":"INT {} {}",
    "string":"VARCHAR({}) {} {}",
    "miti":"DATE {} {}",
    "ho_ki_haina":"BOOLEAN {} {}",
}

needs_q = {
    'miti':True,
    'string':True,
    'anka':False,
    'ho_ki_haina':True
}
class Column:
    constraint = {}
    def __init__(self,data_type,**kwargs):
        self.data_type = data_type
        self.constraint = kwargs
        self.check_null()
       
    def check_null(self):
         if not "null" in self.constraint:
            self.constraint.update({"null":True})

    
    def _is_null_or_not(self,data_type,default_val):
        if  self.constraint["null"] and not default_val:
            return sql_type[data_type].format('','')

        if self.constraint["null"] and  default_val:
            if needs_q[data_type]:
                if data_type == "miti" and default_val=="aja_ko_date":
                    return sql_type[data_type].format('',f"DEFAULT CURRENT_DATE")
                elif data_type == "ho_ki_haina" and default_val=="haina":
                    return sql_type[data_type].format('',f"DEFAULT 'f'")
                elif data_type == "ho_ki_haina" and default_val=="ho":
                    return sql_type[data_type].format('',f"DEFAULT 't'")
                else:
                    return sql_type[data_type].format('',f"DEFAULT '{default_val}'")
            return sql_type[data_type].format('',f" DEFAULT {default_val}")
        else:
            return sql_type[data_type].format('NOT NULL ','')


        

    @property
    def _get_sql_type(self):
        default_val = self.constraint.get("default")
        if self.data_type == "string":
            MAX =self.constraint.get("max_length")
            if not MAX:
                raise MaxLengthVayenaKanchha
            

            if self.constraint["null"] and  not default_val:
                return sql_type[self.data_type].format(MAX,'','')

            if self.constraint["null"] and  default_val:
                return sql_type[self.data_type].format(MAX, 'NOT NULL ',f" DEFAULT '{default_val}'")
            
            else:
                return sql_type[self.data_type].format(MAX,'NOT NULL' ,'')

            
        return self._is_null_or_not(self.data_type,default_val)

