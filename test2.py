import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))

# create_db_tables(dbm)
dbm.db_execute_query(
    '''
    INSERT INTO tracks (id, title, artist, album, duration, genre, ages, lyric, area, date)
    VALUES
        (3, "treck1", "artist1", "album1", "00:01:40", "Rock", "18+", "Lyrics 1", "USA", "2021-12-12"),
        (4, "treck2", "artist2", "album2", "00:02:30", "Pop", "21+", "Lyrics 2", "UK", "2021-12-13"),
        (5, "treck3", "artist3", "album1", "00:03:20", "Hip Hop", "18+", "Lyrics 3", "USA", "2021-12-14"),
        (6, "treck4", "artist4", "album3", "00:04:10", "R&B", "21+", "Lyrics 4", "UK", "2021-12-15"),
        (7, "treck5", "artist5", "album3", "00:05:00", "Electronic", "18+", "Lyrics 5", "USA", "2021-12-16");
   
    ''', None
)
# dbm.db_execute_query(
#     '''
#     ALTER TABLE user
#     RENAME TO user_legacy;
#     ''', None
#     )

# dbm.db_execute_query(
#         """
#         CREATE TABLE IF NOT EXISTS user (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             fname TEXT NOT NULL,
#             lname TEXT NOT NULL,
#             email TEXT NOT NULL,
#             address TEXT NOT NULL,
#             username TEXT NOT NULL unique,
#             password TEXT NOT NULL,
#             subscription Boolean,
#             singerornormal Boolean,
#             wallet INTEGER
#         );
#         """,
#         None,
#     )

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