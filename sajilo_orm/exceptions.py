from colorama import Fore

class TableVetayenaKanchha(Exception):
    """
    Diyeko table nai vetayena yaar ! 
    """

    def __init__(self, message) -> None:
        super().__init__(Fore.RED+message)

    