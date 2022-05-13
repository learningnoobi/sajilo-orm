
SELECT_ALL = "SELECT * FROM {} "
INSERT_INTO = " INSERT INTO {} ({}) values {} "
DELETE_ALL = "DELETE FROM {} "
CHECK_TABLE =  "select exists(select relname from pg_class where relname = '{}' and relkind='r');"
UPDATE = "Update {} SET {} WHERE {} ;"
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS {} ({}) "
#  "Update {} set {player_name='XOLOK',trophy_won = 999} where player_id=8;"