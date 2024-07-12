import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))
# dbm.db_execute_query("DROP TABLE IF EXISTS user_legacy;", None)
# create_db_tables(dbm)
# dbm.db_execute_query(
#     '''
<<<<<<< Updated upstream
#     ALTER TABLE albums
#     DROP COLUMN track_id;
#     ''',
#     None
# )

=======
#     DROP TABLE IF EXISTS albums;
#     ''',
#     None
# )
dbm.db_execute_query(
    """
    DROP TABLE IF EXISTS tracks;
    """,
    None,
)
dbm.db_execute_query(
        """
       CREATE TABLE IF NOT EXISTS tracks (
             title TEXT PRIMARY KEY NOT NULL,
             artist_id INTEGER NOT NULL,
             duration INTEGER NOT NULL,
             genre TEXT NOT NULL,
             ages TEXT NOT NULL,
             lyric TEXT NOT NULL,
             area TEXT NOT NULL,
             FOREIGN KEY (artist_id) REFERENCES user (id)
         );
        """,
        None,
    )
# dbm.db_execute_query(
#         """
#            CREATE TABLE IF NOT EXISTS ticket (
#              user_id INTEGER NOT NULL,
#              concert_id INTEGER NOT NULL,
#              PRIMARY KEY (user_id, concert_id),
#              FOREIGN KEY (user_id) REFERENCES user (id),
#              FOREIGN KEY (concert_id) REFERENCES concert (id)
#          );
#         """,
#         None,
#     )
# dbm.db_execute_query(
#         """
#           CREATE TABLE IF NOT EXISTS like_playlist (
#                 user_id INTEGER NOT NULL,
#                 playlist_id INTEGER NOT NULL,
#                 PRIMARY KEY (user_id, playlist_id),
#                 FOREIGN KEY (user_id) REFERENCES user (id),
#                 FOREIGN KEY (playlist_id) REFERENCES albums (id)
#          );
#         """,
#         None,
#     )
dbm.db_execute_query(
        """
             CREATE TABLE IF NOT EXISTS playlist_music (
             playlist_id INTEGER NOT NULL,
             track_id INTEGER NOT NULL,
             PRIMARY KEY (playlist_id, track_id),
             FOREIGN KEY (playlist_id) REFERENCES playlist (id),
             FOREIGN KEY (track_id) REFERENCES tracks (id)     
         );
        """,
        None,
        )
# dbm.db_execute_query(
#         """
#           CREATE TABLE IF NOT EXISTS friend (
#              user_id INTEGER NOT NULL,
#              friend_id INTEGER NOT NULL,
#              PRIMARY KEY (user_id, friend_id),
#              FOREIGN KEY (user_id) REFERENCES user (id),
#              FOREIGN KEY (friend_id) REFERENCES user (id)
#          );
#         """,
#         None,
#     )
>>>>>>> Stashed changes


# dbm.db_execute_query(
#     """
#     ALTER TABLE likes RENAME TO like_track;
#     """,
#     None,
# )

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

# dbm.db_execute_query(
#     '''
#     INSERT INTO concert (name, venue, date, ticket_price, artist_id)
#     VALUES ("Concert Name", "Concert Venue", "2022-01-01", 100, 2)
#     ''',
#     None
# )
dbm.db_execute_query(
    '''
    INSERT INTO ticket (user_id, concert_id)
    VALUES (2,4)
    ''',
    None
)


dbm.db_disconnect()