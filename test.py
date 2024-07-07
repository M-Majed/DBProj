import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))

create_db_tables(dbm)
dbm.db_execute_query(
    '''
    INSERT INTO
        tracks (id, title, artist, album,  duration, genre, ages, lyric, area)
        VALUES
            (1, 'Track Title', 'Artist Name', 'Album Name', '00:03:30', 'Genre', 'Ages', 'Lyrics', 'Area');
    ''', None
)

dbm.db_disconnect()