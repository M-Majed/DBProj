from DBManagement import DBM
import Variable
# dbm = DBManagement.DBM()
# dbm.db_connect()


# WARNING! Deletes all tables and their descriptions!
def drop_all_tables(dbm: DBM):
    tables = ["user", "tracks"]  # example
    # tables = ["user"] # later: add all table names
    if not dbm:
        return False
    for elem in tables:
        dbm.db_execute_query(f"drop table if exists {elem}", None)
    return True


def create_db_tables(dbm: DBM):
    if not dbm:
        return False

    # signup: fname lname email address username password
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
    # signup: fname lname email address username password
    dbm.db_execute_query(
        """ 
        CREATE TABLE IF NOT EXISTS tracks (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT  NOT NULL,
         artist TEXT NOT NULL,
         album TEXT NOT NULL,
         duration INTEGER NOT NULL,
         genre TEXT NOT NULL,
         ages TEXT NOT NULL,
         lyric TEXT NOT NULL,
         area TEXT NOT NULL
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
            subscription Boolean,
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
             artist TEXT NOT NULL,
             album TEXT NOT NULL,
             duration INTEGER NOT NULL,
             genre TEXT NOT NULL,
             ages TEXT NOT NULL,
             lyric TEXT NOT NULL,
             area TEXT NOT NULL,
             date Date NOT NULL,
         );
        """,
        None,
    )
    dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS concert (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             artist TEXT NOT NULL,
             venue TEXT NOT NULL,
             date DATE NOT NULL,
             ticket_price INTEGER NOT NULL
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
             FOREIGN KEY (user_id) REFERENCES user (id)
         );
        """,
        None,
    )
    
    dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS followorfollowing (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             follower_id INTEGER NOT NULL,
             following_id INTEGER NOT NULL,
             FOREIGN KEY (follower_id) REFERENCES user (id),
             FOREIGN KEY (following_id) REFERENCES user (id)
         );
        """,
        None,
    )
    dbm.db_execute_query(
        """
          CREATE TABLE IF NOT EXISTS friend (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER NOT NULL,
             friend_id INTEGER NOT NULL,
             FOREIGN KEY (user_id) REFERENCES user (id),
             FOREIGN KEY (friend_id) REFERENCES user (id)
         );
        """,
        None,
    )

    return True


def check_login(dbm: DBM, username: str, password: str):
    if not dbm or not username or username == "" or not password or password == "":
        return False, False
    result = dbm.db_execute_read_query(
        f"""
        SELECT Count(*) FROM user
        WHERE username = "{username}" AND password = "{password}"
        """,
        None,
    )
    print(f"{result=}\t{result[0][0]}")
    # countFromDB = len(result)
    countFromDB = result[0][0]
    if countFromDB != 1:
        return False
    return True

# def check_attribute(dbm: DBM):
#     result = dbm.db_execute_read_query(
#         f"""
#         SELECT * FROM tracks
#         limit 1 offset {Variable.selected_index};
#         """,
#         None,
#     )
#     Variable.music_detail_title=result[0][1]


def insert_one_user(dbm: DBM, fname, lname, email, address, username, password):
    if not dbm:
        return False
    if (
        not fname
        or not lname
        or not email
        or not address
        or not username
        or not password
        or fname == ""
        or lname == ""
        or email == ""
        or address == ""
        or username == ""
        or password == ""
    ):
        return False
    try:
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                user (fname,lname,email,address,username,password)
                VALUES
                ("{fname}","{lname}","{email}","{address}","{username}","{password}");
            """,
            None,
        )
    except Exception as e:
        return False

def get_one_user(dbm: DBM, username: str):
    if not dbm or not username or username == "":
        return None
    result = dbm.db_execute_read_query(
        f"""
        SELECT * FROM user WHERE username = "{username}";
        """,
        None,
    )
    return result

def is_subscribed(dbm: DBM, username: str):
    if not dbm or not username or username == "":
        return None
    result = dbm.db_execute_read_query(
        f"""
        SELECT subscription FROM user WHERE username = "{username}";
        """,
        None,
    )
    # print(f"{result=}\t{result[0][0]}")
    if result[0][0]:
        return True if result[0][0] == 1 else False
    else:
        return None

def show_tracks(dbm: DBM):
    if not dbm:
        return None
    result = dbm.db_execute_read_query(
        """
        SELECT * FROM tracks;
        """,
        None,
    )
    return result

def get_track_comments(dbm: DBM, trackId=None):
    if not dbm or not trackId or trackId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM comment WHERE track_id = "{trackId}";
        ''',
        None,
    )
    return result

def set_like_for_track(dbm: DBM, userId=None, trackId=None):
    if not dbm or not userId or userId == "" or not trackId or trackId == "":
        return False
    like_count = get_like_for_track(dbm, userId, trackId)
    if like_count is not None and like_count > 0:
        return True
    try:
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                likes (user_id,track_id)
                VALUES
                ("{userId}","{trackId}");
            """,
            None,
        )
    except Exception as e:
        return False

def clear_like_for_track(dbm: DBM, userId=None, trackId=None):
    if not dbm or not userId or userId == "" or not trackId or trackId == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            DELETE FROM likes
            WHERE user_id = "{userId}" AND track_id = "{trackId}";
            """,
            None,
        )
    except Exception as e:
        return False

def get_like_for_track(dbm: DBM, userId=None, trackId=None):
    if not dbm or not userId or userId == "" or not trackId or trackId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT Count(*) FROM likes WHERE user_id = "{userId}" AND track_id = "{trackId}";
        ''',
        None,
    )
    return result[0][0] if result else None
 

def get_userid_by_username(dbm: DBM, username=None):
    if not dbm or not username or username == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT id FROM user WHERE username = "{username}";
        ''',
        None,
    )
    return result[0][0] if result else None
def post_comment(dbm: DBM, userId=None, trackId=None, commentText=None):
    if not dbm or not userId or userId == "" or not trackId or trackId == "" or not commentText or commentText == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                comment (track_id,user_id,comment_text)
                VALUES
                ("{trackId}","{userId}","{commentText}");
            """,
            None,
        )
    except Exception as e:
        return False

def get_friendIds(dbm: DBM,  userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT friend_id FROM friend WHERE user_id = "{userId}";
        ''',
        None,
    )
    return [row[0] for row in result]
def follow(dbm: DBM, userId=None, friendId=None):
    if not dbm or not userId or userId == "" or not friendId or friendId == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                followorfollowing (follower_id,following_id)
                VALUES
                ("{userId}","{friendId}");
            """,
            None,
        )
    except Exception as e:
        return False
    
def get_comments(dbm: DBM, userId=None, friendIds=None, trackId=None):
    if not dbm or not userId or userId == "" or not friendIds or not trackId or trackId == "":
        return None
    friendIds.append(userId)
    friendIds = tuple(friendIds)
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM comment WHERE user_id IN {friendIds} AND track_id = "{trackId}" order by id asc;
        ''',
        None,
    )
    return result

def update_user_subscription(dbm: DBM, username=None, subscription=None):
    dbm.db_execute_query(
        f"""
        UPDATE user
        SET subscription = {subscription}
        WHERE username = "{username}";
        """,
        None,)
    
def update_user_artist(dbm: DBM, username=None, artist=None):
    dbm.db_execute_query(
        f"""
        UPDATE user
        SET singerornormal = {artist}
        WHERE username = "{username}";
        """,
        None,)
    
def update_user_balance(dbm: DBM, username=None, balance=None):
    dbm.db_execute_query(
        f"""
        UPDATE user
        SET wallet = {balance}
        WHERE username = "{username}";
        """,
        None,)
        
def get_friends(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT friend_id FROM friend WHERE user_id = "{userId}";
        ''',
        None,
    )
    return [row[0] for row in result]
        
    
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


# dbm.db_disconnect()

