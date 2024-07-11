import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))

# create_db_tables(dbm)
# dbm.db_execute_query(
#     '''
#     INSERT INTO tracks (id, title, artist, album, duration, genre, ages, lyric, area)
#     VALUES
        
#                        (10, "treck4", "artist4", "album3", "00:04:10", "Pop", "21+", "Lyrics 4", "UK");
   
#     ''', None
# )
# dbm.db_execute_query(
#     '''
    
#     INSERT INTO tracks (id, title, artist, album, duration, genre, ages, lyric, area)
#     VALUES
        
#                        (10, "treck4", "artist4", "album3", "00:04:10", "Pop", "21+", "Lyrics 4", "UK");
   
#     ''', None
# )
# dbm.db_execute_query(
#         """
#              CREATE TABLE IF NOT EXISTS playlist_music (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         playlist_id INTEGER NOT NULL,
#         track_id TEXT NOT NULL,
#         FOREIGN KEY (playlist_id) REFERENCES playlist (id),
#         FOREIGN KEY (track_id) REFERENCES tracks (id)
#     );
#         """,
#         None,
#     )

dbm.db_execute_query(
    '''
    INSERT INTO playlist_music (id, playlist_id, track_id)
    VALUES (1, 1, 10);
    ''',
    None
)

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