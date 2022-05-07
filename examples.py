"""
This shows example on how to use sajilo orm .

"""

from sajilo_orm.models import DamiModel


class Team(DamiModel):
    table_ko_naam = "team"


class League(DamiModel):
    table_ko_naam = "league"


def main():
    
    # filters = Team.bata.khojera(name="PsSG",no_players=69)
    # print(filters)
    # Team.ma.data_hala(name="Alvi",created_on='1999-05-08',no_players=3)
    # League.ma.data_hala(name="Alvi")
    print(League.bata.sabaideu())


if __name__ == "__main__":
    main()
