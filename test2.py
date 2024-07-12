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
    INSERT INTO tracks (id ,title,duration, genre, ages, lyric, area, artist_id, permission)
    VALUES 
    (2,"Track Title1", 180, "pop", "All Ages", "Lyrics1", "LA", 3, 1),
    (3,"Track Title3", 180, "Ruck", "+18", "Lyrics2", "US", 2, 1),
    (7,"Track Title5", 180, "qq", "+21", "Lyrics3", "UK", 4, 1)
    
    ''',
    None
)


dbm.db_disconnect()