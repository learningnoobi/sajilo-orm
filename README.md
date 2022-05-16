## Documentation
### Installation

```python
 pip install sajilo-orm
```


#### Table of Contents
- [Connect Database](#connect-database)
- [Create Table](#create-table)
- [QuerySet API](#queryset-api)
- [Add Data](#add-data)
- [Filter And Get Data](#filter-and-get-data)
- [Update Data](#update-data)
- [Delete Data](#delete-data)
- [Check If Table Exists](#check-if-table-exists)
- [Types of Exception](#types-of-exception)



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

###### To create table , import `DamiModel` from `sajilo_orm.models` and use `Column` class to define column along with datatype which is in Nepali
Note: `id serial primary key` is added automatically when creating table

```python

from sajilo_orm.models import DamiModel
from sajilo_orm.field import Column

class Country(DamiModel):
    table_ko_naam = "country" # this will be the name of the table created in database

    name = Column("string", max_length="50")
    no_of_province = Column("anka")  #number
    new_year = Column("miti", default='2000-01-01')   #date
    today = Column("miti", default='aja_ko_date')   #gives CURRENT_DATE
    ramro = Column("ho_ki_haina" , default="ho")    #boolean
    data = Column("string", null=False,max_length="20")    #by default null=True

```
Here's what data type type is behind the scene
```
sql_type = {
    "anka":"INT ",
    "string":"VARCHAR({max_length})
    "miti":"DATE ",
    "ho_ki_haina":"BOOLEAN ",
}
(string chai nepali ma k rakhne vanera sochirako)

```
#####  Ths won't create table yet , To create table use `table_banau` method

```python
    Country.bata.table_banau()
```

### QuerySet API

Here's the list of api that you can use for executing query
##### Get all data 

```python

country_list = Country.bata.sabaideu()  # Returns List of Model Objects
print(country_list)

#output
#[] since there is no data yet
```
#### Add Data 
For adding data in the table , use `data_hala` method. 
`Table.ma.data_hala(**dataharu)`

```python

Country.ma.data_hala(name="nepal",no_of_province= 8,data="nice country") # will update below  
Country.ma.data_hala(name="japan",no_of_province= 37,data="nice country")  #default value are added

# Now , if you call sabaideu

country_list = Country.bata.sabaideu()  
#[<Country :1>,<Country :2>]

# To get single object
a = country_list[0]

print(a.name,a.no_of_province)
# nepal,8

```
Note: `Country.bata.data_hala(name="japan",no_of_province= 37) ` also works
`ma` was adding cause it sounds gramatically correct than `bata` :sweat_smile:

#### Filter and Get Data
For filter , use `khojera` method

```python
 filters = Team.bata.khojera(name="PSG")
```


###### For multiple column filter with 'AND' , add comma 


```python
 filters = Country.bata.khojera(name="nepal" , no_of_province =20)
```
###### For 'OR' filter , add an argument with value "or" before writing filter condition

```python
 filters = Country.bata.khojera("or",name="japan" , no_of_province =20)
```
 
####  Update Data

To Update data, we need to add `id` before specifying updating column
If not id is provided `IdXainaKanchha` exception will be raised

```python
 Country.bata.data_fera(id=1, name="Nepal", no_of_province=7,new_year='1999-01-01')
 # this will update Country with id 1 and rest will be updated with data provided
 a = country_list[0]

 print(a.name,a.no_of_province,a.new_year)
# Nepal,7,1999-01-01
```
##### Exceptions
If nothing is provided after id , then `SyntaxBigryoKanchha` exception will be raised
```python
Refree.bata.data_fera(id=1) #raises SyntaxBigryoKanchha Exception

Refree.bata.data_fera(name="sinpachi") # raises IdXainaKanchha Exception
```

#### Delete Data
With this , this ORM will be able to perform simple `CRUD OPERATIONS`

To delete `data_fala` (lol) is used . Use this wisely .

```python
   Country.bata.data_fala(id=2)
   Country.bata.data_fala(name='japan')`
   Country.bata.data_fala(no_of_provinces=')
```

#### Check if table exists 

```python
    Refree.bata.check_table_exists()
```

###### To get the use case of this orm , read the [Test Case Here](https://github.com/learningnoobi/sajilo-orm/blob/main/tests/test_table.py)


#### Types of Exeptions
Below is the list of exception you might get using `sajilo orm`
- ###### TableVetayenaKanchha  `Database ma nai table navayesi aaune error ! `
- ###### ColumnNaiXainaKanchha `Table ma nai navako column diyesi aaune error ! `
- ###### DatabaseConnectVayenaKanchha `Database connection config namilda aaune error !  `
- ###### IdXainaKanchha `Data ferda id diyena vane aaune error `
- ###### SyntaxBigryoKanchha `Syntax nai bigrexi aaune error ! `
- ###### DateFormatMilenaKanchha `Date Format nai bigrexi aaune error ! `
- ###### NotNullMaDataVayenaKanchha `Not Null ma Data navayesi aaune error !`
