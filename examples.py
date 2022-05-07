"""
This shows example on how to use sajilo orm .

"""

from sajilo_orm.models import DamiModel


class Team(DamiModel):
    table_ko_naam = "team"


def main():
    filters = Team.bata.khojera("or",name="PSG",no_players=69)
    print(filters)


if __name__ == "__main__":
    main()
