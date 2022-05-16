__title__ = 'Sajilo ORM'
__version__ = '0.0.6'
__author__ = 'learningnoobi (Bishal Rai)'


SELECT_ALL = "SELECT * FROM {} "
INSERT_INTO = " INSERT INTO {} ({}) values {} "
DELETE_ALL = "DELETE FROM {} "
CHECK_TABLE =  "select exists(select relname from pg_class where relname = '{}' and relkind='r');"
UPDATE = "Update {} SET {} WHERE {} ;"
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS {} ({}) "
DROP_TABLE = "DROP TABLE {} "
#  "Update {} set {player_name='XOLOK',trophy_won = 999} where player_id=8;"


