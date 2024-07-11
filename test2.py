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
# dbm.db_execute_query(
#         """
#         CREATE TABLE IF NOT EXISTS friend_request (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              accept_reject Boolean,
#              freind_send INTEGER NOT NULL,
#              friend_get INTEGER NOT NULL,
#              FOREIGN KEY (freind_send) REFERENCES user (id),
#              FOREIGN KEY (friend_get) REFERENCES user (id)
#     );
#         """,
#         None,
# #     )
# dbm.db_execute_query(
#     '''
#     INSERT INTO albums (title, artist, track_id, artist_id)
#     VALUES
#         ("Album 1", "Artist 1", 1, 1),
#         ("Album 2", "Artist 2", 2, 2),
#         ("Album 3", "Artist 3", 3, 3);
#     ''',
#     None
# )

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
# dbm.db_execute_query(
#     """
#     CREATE TABLE IF NOT EXISTS albums (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         track_id INTEGER NOT NULL,
#         artist_id INTEGER NOT NULL,
#         FOREIGN KEY (track_id) REFERENCES tracks (id),
#         FOREIGN KEY (artist_id) REFERENCES user (id)
#     );
#     """,
#     None,
# )
# dbm.db_execute_query(f"drop table if exists user", None)
# dbm.db_execute_query(
#     """
#     ALTER TABLE tracks
#     ADD COLUMN artist_id INTEGER NOT NULL;
#     FOREIGN KEY (artist_id) REFERENCES user (id);
#     """,
#     None,
# )
# dbm.db_execute_query(
#     '''
#     DROP TABLE IF EXISTS concert;
#     ''',
#     None
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

dbm.db_execute_query(
        """
           CREATE TABLE IF NOT EXISTS playlist (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             user_id INTEGER NOT NULL,
             public_private BOOLEAN NOT NULL,
             FOREIGN KEY (user_id) REFERENCES user (id)
         );
        """,
        None,
    )


dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS concert (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
            
             venue TEXT NOT NULL,
             date DATE NOT NULL,
             ticket_price INTEGER NOT NULL,
              artist_id INTEGER  NOT NULL,
             FOREIGN KEY (artist_id) REFERENCES user (id)
             
         );
        """,
        None,
    )
dbm.db_execute_query(
        """
       CREATE TABLE IF NOT EXISTS tracks (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT  NOT NULL,
             album TEXT NOT NULL,
             duration INTEGER NOT NULL,
             genre TEXT NOT NULL,
             ages TEXT NOT NULL,
             lyric TEXT NOT NULL,
             area TEXT NOT NULL,
             artist_id INTEGER NOT NULL,
             permission BOOLEAN NOT NULL,
             FOREIGN KEY (artist_id) REFERENCES user (id)
         );
        """,
        None,
    )
# dbm.db_execute_query(
#     '''
#     ALTER TABLE playlist
#     ADD COLUMN public_private BOOLEAN;
#     ''',
#     None
# )

dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS like_playlist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                playlist_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id),
                FOREIGN KEY (playlist_id) REFERENCES playlist (id)
         );
        """,
        None,
    )
dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS like_album (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                album_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id),
                FOREIGN KEY (album_id) REFERENCES albums (id)
         );
        """,
        None,
    )
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