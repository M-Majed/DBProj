import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))
# dbm.db_execute_query("DROP TABLE IF EXISTS user_legacy;", None)
# create_db_tables(dbm)
dbm.db_execute_query(
    '''
    INSERT INTO albums (id, title, track_id, artist_id)
    VALUES
    (1, "Album Title1", "3", 3),
    (2, "Album Title2", "3", 2),
    (3, "Album Title3", "1", 4)
    ''',
    None
)
dbm.db_disconnect()