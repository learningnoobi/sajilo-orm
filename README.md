### This is for learning purpose 


## Documentation

### Get Table from database

Say you have a table in database named for example 'team' , then create a class such with table_ko_naam attribute  :

```python
from sajilo_orm.models import DamiModel

class Team(DamiModel):
    table_ko_naam = "team" #must be same as database table name
```

Then you can use query such as :

Get all data 

```python
Team.bata.sabaideu() #returns list of dictionary
```

Filter and Get Data

```python
 filters = Team.bata.khojera(name="PSG")
```

For multiple column filter with 'AND' , add comma 

```python
 filters = Team.bata.khojera(name="PSG" , no_players =20)
```
For 'OR' filter , add an argument with value "or" before writing filter condition

```python
 filters = Team.bata.khojera("or",name="PSG" , no_players =20)
```
