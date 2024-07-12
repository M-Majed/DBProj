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
    ALTER TABLE albums
    DROP COLUMN track_id;
    ''',
    None
)



# dbm.db_execute_query(
#     """
#     CREATE TABLE IF NOT EXISTS albums (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         artist_id INTEGER NOT NULL,
#         FOREIGN KEY (artist_id) REFERENCES user (id)
#     );
#     """,
#     None,
#     )


# dbm.db_execute_query(
#         """
#            CREATE TABLE IF NOT EXISTS concert (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              name TEXT NOT NULL,
             
#              venue TEXT NOT NULL,
#              date DATE NOT NULL,
#              ticket_price INTEGER NOT NULL,
#              artist_id INTEGER  NOT NULL,
#              FOREIGN KEY (artist_id) REFERENCES user (id)
             
#          );
#         """,
#         None,
#     )

# dbm.db_execute_query(
#         """
#            CREATE TABLE IF NOT EXISTS playlist (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              name TEXT NOT NULL,
#              user_id INTEGER NOT NULL,
#              public_private BOOLEAN NOT NULL,
#              FOREIGN KEY (user_id) REFERENCES user (id)
#          );
#         """,
#         None,
#     )


# dbm.db_execute_query(
#         """
#           CREATE TABLE IF NOT EXISTS concert (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              name TEXT NOT NULL,
            
#              venue TEXT NOT NULL,
#              date DATE NOT NULL,
#              ticket_price INTEGER NOT NULL,
#               artist_id INTEGER  NOT NULL,
#              FOREIGN KEY (artist_id) REFERENCES user (id)
             
#          );
#         """,
#         None,
#     )
# dbm.db_execute_query(
#         """
#        CREATE TABLE IF NOT EXISTS tracks (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              title TEXT  NOT NULL,
#              album TEXT NOT NULL,
#              duration INTEGER NOT NULL,
#              genre TEXT NOT NULL,
#              ages TEXT NOT NULL,
#              lyric TEXT NOT NULL,
#              area TEXT NOT NULL,
#              artist_id INTEGER NOT NULL,
#              permission BOOLEAN NOT NULL,
#              FOREIGN KEY (artist_id) REFERENCES user (id)
#          );
#         """,
#         None,
#     )
# dbm.db_execute_query(
#     '''
#     ALTER TABLE playlist
#     ADD COLUMN public_private BOOLEAN;
#     ''',
#     None
# )

# dbm.db_execute_query(
#         """
#           CREATE TABLE IF NOT EXISTS like_playlist (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER NOT NULL,
#                 playlist_id INTEGER NOT NULL,
#                 FOREIGN KEY (user_id) REFERENCES user (id),
#                 FOREIGN KEY (playlist_id) REFERENCES playlist (id)
#          );
#         """,
#         None,
#     )
# dbm.db_execute_query(
#         """
#           CREATE TABLE IF NOT EXISTS like_album (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER NOT NULL,
#                 album_id INTEGER NOT NULL,
#                 FOREIGN KEY (user_id) REFERENCES user (id),
#                 FOREIGN KEY (album_id) REFERENCES albums (id)
#          );
#         """,
#         None,
#     )
# dbm.db_execute_query(
#     """
#     CREATE TABLE IF NOT EXISTS albums (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         artist TEXT NOT NULL,
#         track_id INTEGER NOT NULL,
#         artist_id INTEGER NOT NULL,
#         FOREIGN KEY (track_id) REFERENCES tracks (id),
#         FOREIGN KEY (artist_id) REFERENCES user (id)
#     );
#     """,
#     None,
# )
# dbm.db_execute_query(
#     '''
#     DELETE FROM friend;
#     ''',
#     None
# )
# dbm.db_execute_query(
#     '''
#     DELETE FROM followorfollowing;
#     ''',
#     None
# )


dbm.db_disconnect()