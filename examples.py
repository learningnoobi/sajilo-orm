"""
This shows example on how to use sajilo orm .

"""

from sajilo_orm.models import DamiModel


class Team(DamiModel):
    table_ko_naam = "team"


class League(DamiModel):
    table_ko_naam = "league"

class Players(DamiModel):
    table_ko_naam = "players"


def main():
    Players.ma.data_hala(player_name="Prajwal",stats=69,jersey_num=69,team_id=1)


if __name__ == "__main__":
    main()
