## Documentation

## Connect Database

*Postgresql is the only supported Database for now(Feel free contribute to add new database)*

```python
from sajilo_orm.manager import BaseManager

MY_DB_SETTINGS = {
    "database": "db_name",
    "user": "db_user",
    "password": "db_password",
    "host": "db_host", #localhost for local connection
    "port": "5432",
}

BaseManager.DB_SETTINGS = MY_DB_SETTINGS

```
### Create Table 

###### To create table , import `DamiModel` from `sajilo_orm.models` and use `Column` class to define column along with datatype 

```python

from sajilo_orm.models import DamiModel
from sajilo_orm.field import Column

class Country(DamiModel):
    table_ko_naam = "country" # this will be the name of the table created in database

    name = Column("string", max_length="50")
    no_of_province = Column("integer")


```
#####  Ths won't create table yet , To create table use `table banau` method

```python
    Country.bata.table_banau()
```

### QuerySet API

Here's the list of api that you can use for executin query
##### Get all data 

```python

country_list = Country.bata.sabaideu()  # Returns List of Model Objects
print(country_list)

#output
#[] since there is no data yet
```
##### ADD data 

```python

Country.ma.data_hala(name="nepal",no_of_province= 7)  
Country.ma.data_hala(name="japan",no_of_province= 37)  

# Now , if you call sabaideu

country_list = Country.bata.sabaideu()  
#[<Country :1>,<Country :2>]

# To get single object
a = country_list[0]

print(a.name,a.no_of_province)
# nepal,7

```

##### Filter and Get Data

```python
 filters = Team.bata.khojera(name="PSG")
```


##### For multiple column filter with 'AND' , add comma 


```python
 filters = Team.bata.khojera(name="PSG" , no_players =20)
```
##### For 'OR' filter , add an argument with value "or" before writing filter condition

```python
 filters = Team.bata.khojera("or",name="PSG" , no_players =20)
```

