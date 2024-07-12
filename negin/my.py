
import sqlite3
from sqlite3 import Error


class DBM:
    db_path = "my.db"
    db_conn = None

    def db_create_connection(self, path=db_path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("\nConnection to SQLite DB successful.")
        except Error as e:
            print(f"\nError '{e}' occurred.")
            return None
        return connection

    def db_connect(self):
        if self.db_conn:
            return
        self.db_conn = self.db_create_connection(self.db_path)

    def db_disconnect(self):
        if self.db_conn:
            self.db_conn.close()

    def db_execute_query(self, query, connection):
        if not connection:
            connection = self.db_conn
        if not connection:
            self.db_connect()

        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("\nQuery executed successfully.")
            return True
        except Error as e:
            print(f"\nError '{e}' occurred.")
            # suppress error
            return False

    def db_execute_read_query(self, query, connection):
        if not connection:
            connection = self.db_conn
        if not connection:
            self.db_connect()

        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"\nError '{e}' occurred.")
            return None


# db_execute_query('drop table if exists person', None)
# db_execute_query('drop table if exists personsecret', None)
# db_execute_query('drop table if exists relying', None)
# db_execute_query('drop table if exists perm', None)

# db_execute_query(
#     '''
#     CREATE TABLE IF NOT EXISTS person (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         melli TEXT UNIQUE NOT NULL,
#         fname TEXT NOT NULL,
#         lname TEXT NOT NULL,
#         father_fname TEXT NOT NULL,
#         mother_fname TEXT NOT NULL,
#         mother_lname TEXT NOT NULL,
#         y INTEGER NOT NULL,
#         m INTEGER NOT NULL,
#         d INTEGER NOT NULL,
#         gender INTEGER NOT NULL,
#         nationality TEXT
#         );
#     ''', None
# )

# db_execute_query(
#     '''
#     CREATE TABLE IF NOT EXISTS personsecret (
#         melli TEXT,
#         secret TEXT,
#         PRIMARY KEY (melli,secret),
#         FOREIGN KEY(melli) REFERENCES person(melli)
#         );
#     ''', None
# )

# db_execute_query(
#     '''
#     CREATE TABLE IF NOT EXISTS relying (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT UNIQUE NOT NULL
#         );
#     ''', None
# )

# db_execute_query(
#     '''
#     CREATE TABLE IF NOT EXISTS perm (
#         relying_id INTEGER,
#         melli TEXT,
#         full_access INTEGER NOT NULL,
#         PRIMARY KEY (relying_id, melli),
#         FOREIGN KEY(relying_id) REFERENCES relying(id),
#         FOREIGN KEY(melli) REFERENCES person(melli)
#         );
#     ''', None
# )


# db_execute_query(
#     '''
#     INSERT INTO
#         person (melli,fname,lname,father_fname,mother_fname,mother_lname,y,m,d,gender,nationality)
#         VALUES
#         ("1279876543","Ali","Akbari","Reza","Zahra","Asqari",2000,3,22,1,"Iranian"),
#         ("1289876543","Fateme","Mirzayi","Ahmad","Zeynab","Mohammadi",1987,11,17,0,"Iranian");
#     ''', None
# )

# db_execute_query(
#     f'''
#     INSERT INTO
#         personsecret (melli,secret)
#         VALUES
#         ("1279876543","{pyotp.random_base32(length=128)}"),
#         ("1289876543","{pyotp.random_base32(length=128)}");
#     ''', None
# )

# db_execute_query(
#     f'''
#     INSERT INTO
#         relying (name)
#         VALUES
#         ("IUT"),
#         ("Sejam");
#     ''', None
# )

# db_execute_query(
#     f'''
#     INSERT INTO
#         perm (relying_id, melli, full_access)
#         VALUES
#         (1, "1279876543", 0),
#         (2, "1279876543", 1);
#     ''', None
# )

# def get_current(melli: str):
#     if not melli:
#         return None
#     result = db_execute_read_query(
#         f'''
#         SELECT secret FROM personsecret WHERE melli = {melli};
#         ''', None
#     )
#     secret = result[0][0]
#     global totp_interval
#     p = pyotp.TOTP(s=secret, interval=totp_interval, digits=totp_length)
#     return p.now()

# def get_remaining_time():
#     return totp_interval - datetime.datetime.now().timestamp() % totp_interval

# def verify_code(melli: str, code: str):
#     if not melli:
#         return None
#     result = db_execute_read_query(
#         f'''
#         SELECT secret FROM personsecret WHERE melli = {melli};
#         ''', None
#     )
#     secret = result[0][0]
#     global totp_interval
#     global totp_length
#     p = pyotp.TOTP(s=secret, interval=totp_interval, digits=totp_length)
#     return p.now() == code

# print(get_current('1279876543'))
# print(get_remaining_time())
# print(verify_code('1279876543','1713190839'))


# def get_personal_data(melli: str, relying: int):
#     if not melli:
#         return None

#     # Check if relying has [full] access
#     result = db_execute_read_query(
#         f'''
#         SELECT * FROM perm WHERE melli = {melli} AND relying_id = {relying};
#         ''', None
#     )
#     full_access = None
#     if result:
#         full_access = result[0][-1]
#     print(f'{full_access=}')

#     # Fetching personal data from db based on access information
#     if full_access:
#         result = db_execute_read_query(
#             f'''
#             SELECT * FROM person WHERE melli = {melli};
#             ''', None
#         )
#         return result[0]
#     elif full_access == 0:
#         result = db_execute_read_query(
#             f'''
#             SELECT melli, fname, lname, y, m, d, gender FROM person WHERE melli = {melli};
#             ''', None
#         )
#         return result[0]
#     else:
#         print('\nPermission not found!')
#         return None

# print(get_personal_data("1279876543",2))






def create_db_tables(dbm: DBM):
    if not dbm:
        return False
    dbm.db_execute_query(
    """
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        artist_id INTEGER NOT NULL,
        FOREIGN KEY (artist_id) REFERENCES user (id)
    );
    """,
    None,
    )

    # signup: fname lname email address username password
    dbm.db_execute_query(
        """
        CREATE TABLE IF NOT EXISTS message (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            FOREIGN KEY (sender_id) REFERENCES user (id),
            FOREIGN KEY (receiver_id) REFERENCES user (id)
        );
        """,
        None,
    )

    dbm.db_execute_query(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            username TEXT NOT NULL unique,
            password TEXT NOT NULL,
            subscription Boolean default 0,
            singerornormal Boolean,
            wallet INTEGER
        );
        """,
        None,
    )
    dbm.db_execute_query(
        """
             
            CREATE TABLE IF NOT EXISTS suggestion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                track_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id),
                FOREIGN KEY (track_id) REFERENCES tracks (id)
            );  """,
        None,
    )


    dbm.db_execute_query(
        """
       CREATE TABLE IF NOT EXISTS tracks (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT  NOT NULL,
             artist_id INTEGER NOT NULL,
             FOREIGN KEY (artist_id) REFERENCES user (id),
             album TEXT NOT NULL,
             duration INTEGER NOT NULL,
             genre TEXT NOT NULL,
             ages TEXT NOT NULL,
             lyric TEXT NOT NULL,
             area TEXT NOT NULL,
         );
        """,
        None,
    )
    
    
    dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS concert (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             artist_id INTEGER  NOT NULL,
             FOREIGN KEY (artist_id) REFERENCES user (id),
             venue TEXT NOT NULL,
             date DATE NOT NULL,
             ticket_price INTEGER NOT NULL,
             
         );
        """,
        None,
    )
    dbm.db_execute_query(
        """
           CREATE TABLE IF NOT EXISTS likes (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER NOT NULL,
             track_id INTEGER NOT NULL,
             FOREIGN KEY (user_id) REFERENCES user (id),
             FOREIGN KEY (track_id) REFERENCES tracks (id)
         );
        """,
        None,
    )
    dbm.db_execute_query(
        """
            CREATE TABLE IF NOT EXISTS comment (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             track_id INTEGER NOT NULL,
             user_id INTEGER NOT NULL,
             comment_text TEXT NOT NULL,
             FOREIGN KEY (track_id) REFERENCES tracks (id),
             FOREIGN KEY (user_id) REFERENCES user (id)
         );
        """,
        None,
    )
    dbm.db_execute_query(
        """
           CREATE TABLE IF NOT EXISTS ticket (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER NOT NULL,
             concert_id INTEGER NOT NULL,
             FOREIGN KEY (user_id) REFERENCES user (id),
             FOREIGN KEY (concert_id) REFERENCES concert (id)
         );
        """,
        None,
    )
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
             CREATE TABLE IF NOT EXISTS playlist_music (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             playlist_id INTEGER NOT NULL,
             FOREIGN KEY (playlist_id) REFERENCES playlist (id),
             track_id INTEGER NOT NULL,
             FOREIGN KEY (track_id) REFERENCES tracks (id),     
         );
        """,
        None,
    )
    dbm.db_execute_query(
        """
        CREATE TABLE IF NOT EXISTS friend_request (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             freind_send INTEGER NOT NULL,
             friend_get INTEGER NOT NULL,
             FOREIGN KEY (freind_send) REFERENCES user (id),
             FOREIGN KEY (friend_get) REFERENCES user (id),
             accept_reject Boolean
            
         );
        """,
        None,
    )
    
    dbm.db_execute_query(
    """
    CREATE TABLE IF NOT EXISTS followorfollowing (
        follower_id INTEGER NOT NULL,
        following_id INTEGER NOT NULL,
        PRIMARY KEY (follower_id, following_id),
        FOREIGN KEY (follower_id) REFERENCES user (id),
        FOREIGN KEY (following_id) REFERENCES user (id)
    );
    """,
    None,
)
    dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS friend (
             user_id INTEGER NOT NULL,
             friend_id INTEGER NOT NULL,
             PRIMARY KEY (user_id, friend_id),
             FOREIGN KEY (user_id) REFERENCES user (id),
             FOREIGN KEY (friend_id) REFERENCES user (id)
         );
        """,
        None,
    )
    
    dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS like_album (
                user_id INTEGER NOT NULL,
                album_id INTEGER NOT NULL,
                PRIMARY KEY (user_id, album_id),
                FOREIGN KEY (user_id) REFERENCES user (id),
                FOREIGN KEY (album_id) REFERENCES albums (id)
         );
        """,
        None,
    )
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
    return True

dbm=DBM()
dbm.db_connect()
create_db_tables(dbm)