from colorama import Fore



class TableVetayenaKanchha(Exception):
    """
    Diyeko table nai vetayena yaar ! 
    """

    def __init__(self, table_name,db_name) -> None:
        super().__init__(Fore.RED + f"Timle deko table '{table_name}' {db_name} vanne database ma nai vetayena ! Spelling bigryo ki herata ramro sanga !")
    