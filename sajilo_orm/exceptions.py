from colorama import Fore


class TableVetayenaKanchha(Exception):
    """
    Database ma nai table navayesi aaune error ! 
    """
    def __init__(self, table_name,db_name) -> None:
        super().__init__(Fore.RED + f"Timle deko table '{table_name}' {db_name} vanne database ma nai vetayena ! Spelling bigryo ki herata ramro sanga !")


class ColumnNaiXainaKanchha(Exception):
    """
    Table ma nai navako column diyesi aaune error ! 
    """

    def __init__(self,table_name) -> None:
        super().__init__(Fore.RED + f"Timle deko column Table '{table_name}' ma nai vetayena ! Spelling bigryo ki ramro sanga herata !")
    

class DatabaseConnectVayenaKanchha(Exception):
    """
    Database connection config namilda aaune error ! 
    """

    def __init__(self) -> None:
        super().__init__(Fore.RED + f"Arrey !! Database ta ramrari connect gara paila !!")
    
class IdXainaKanchha(Exception):
    """
        Data ferda id diyena vane aaune error 
    """

    def __init__(self) -> None:
        super().__init__(Fore.RED + f"Data fernalai euta unique ID chainxa . Unique Id diyerw feri try gara !!")
    
class SyntaxBigryoKanchha(Exception):
    """
    Syntax nai bigrexi aaune error ! 
    """

    def __init__(self) -> None:
        super().__init__(Fore.RED + f"Query ko syntax bigrye xa . Yedi update garda aako vaye id bahek arko field ni chainxa !!")
    