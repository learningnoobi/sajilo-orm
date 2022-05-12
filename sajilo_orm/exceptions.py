from colorama import Fore


class TableVetayenaKanchha(Exception):
    """
    Diyeko table nai vetayena yaar ! 
    """
    def __init__(self, table_name,db_name) -> None:
        super().__init__(Fore.RED + f"Timle deko table '{table_name}' {db_name} vanne database ma nai vetayena ! Spelling bigryo ki herata ramro sanga !")


class ColumnNaiXainaKanchha(Exception):
    """
    Diyeko column nai xaina yaar ! 
    """

    def __init__(self,table_name) -> None:
        super().__init__(Fore.RED + f"Timle deko column Table '{table_name}' ma nai vetayena ! Spelling bigryo ki ramro sanga herataclear !")
    

class DatabaseConnectVayena(Exception):
    """
    Diyeko column nai xaina yaar ! 
    """

    def __init__(self) -> None:
        super().__init__(Fore.RED + f"Arrey !! Database ta ramrari connect gara paila !!")
    