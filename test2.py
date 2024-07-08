import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))

# create_db_tables(dbm)
# dbm.db_execute_query(
#     '''
#     INSERT INTO
#         tracks (id, title, artist, album,  duration, genre, ages, lyric, area,date)
#         VALUES
#             (3, 'Track Title', 'Artist Name', 'Album Name', '00:03:30', 'Genre', 'Ages', 'Lyrics', 'Area' , '2021-06-01');
#     ''', None
# )

# dbm.db_execute_query(f"drop table if exists user", None)
# dbm.db_execute_query(
#         """
#         CREATE TABLE IF NOT EXISTS user (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             fname TEXT NOT NULL,
#             lname TEXT NOT NULL,
#             email TEXT NOT NULL,
#             address TEXT NOT NULL,
#             username TEXT NOT NULL,
#             password TEXT NOT NULL,
#             subscription Boolean,
#             singerornormal Boolean,
#             wallet INTEGER
#         );
#         """,
#         None,
#     )

# dbm.db_execute_query(
#     f'''
#      UPDATE user
#     SET subscription = 1
#     WHERE username = "q"; 
#     '''
#     , None
# )

dbm.db_disconnect()