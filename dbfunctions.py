from DBManagement import DBM
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
   
   
    # dbm.db_execute_query(
    #     """ 
    #     CREATE TABLE IF NOT EXISTS tracks (
    #      id INTEGER PRIMARY KEY AUTOINCREMENT,
    #      title TEXT  NOT NULL,
    #      artist TEXT NOT NULL,
    #      duration INTEGER NOT NULL,
    #      genre TEXT NOT NULL,
    #      ages TEXT NOT NULL,
    #      lyric TEXT NOT NULL,
    #      area TEXT NOT NULL,
    #      permission BOOLEAN NOT NULL
    #      );
    #     """,
    #     None,
    # )
    
    
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


    # dbm.db_execute_query(
    #     """
    #    CREATE TABLE IF NOT EXISTS tracks (
    #          id INTEGER PRIMARY KEY AUTOINCREMENT,
    #          title TEXT  NOT NULL,
    #          artist_id INTEGER NOT NULL,
    #          FOREIGN KEY (artist_id) REFERENCES user (id),
    #          album TEXT NOT NULL,
    #          duration INTEGER NOT NULL,
    #          genre TEXT NOT NULL,
    #          ages TEXT NOT NULL,
    #          lyric TEXT NOT NULL,
    #          area TEXT NOT NULL,
    #      );
    #     """,
    #     None,
    # )
    
    
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
             expired BOOLEAN defult 0,
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


def check_login(dbm: DBM, username: str, password: str):
    if not dbm or not username or username == "" or not password or password == "":
        return False
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
                user (fname,lname,email,address,username,password, subscription, singerornormal)
                VALUES
                ("{fname}","{lname}","{email}","{address}","{username}","{password}", 0, 0);
            """,
            None,
        )
    except Exception as e:
        return False

def get_one_user(dbm: DBM, id: str):
    if not dbm or not id or id == "":
        return None
    result = dbm.db_execute_read_query(
        f"""
        SELECT * FROM user WHERE id = "{id}";
        """,
        None,
    )
    return result

def is_subscribed(dbm: DBM, id: str):
    if not dbm or not id or id == "":
        return None
    result = dbm.db_execute_read_query(
        f"""
        SELECT subscription FROM user WHERE id = "{id}";
        """,
        None,
    )
    # print(f"{result=}\t{result[0][0]}")
    if result[0][0] is not None:
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
        
# def get_frieendIds( dbm, self.appstate["userid"]):
#         friendIds = []
#         dbm.cursor.execute("SELECT friendId FROM friends WHERE userId = %s", (userid,))
#         for row in dbm.cursor.fetchall():
#             friendIds.append(row[0])
#         return friendIds
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

def update_user_subscription(dbm: DBM, id=None, subscription=None):
    dbm.db_execute_query(
        f"""
        UPDATE user
        SET subscription = {subscription}
        WHERE id = "{id}";
        """,
        None,)
    
def update_user_artist(dbm: DBM, id=None, artist=None):
    dbm.db_execute_query(
        f"""
        UPDATE user
        SET singerornormal = {artist}
        WHERE id = "{id}";
        """,
        None,)
    
def update_user_balance(dbm: DBM, id=None, balance=None):
    dbm.db_execute_query(
        f"""
        UPDATE user
        SET wallet = {balance}
        WHERE id = "{id}";
        """,
        None,)
    
def get_followers(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        select username from user
        where id in (SELECT follower_id FROM followorfollowing WHERE following_id = "{userId}");
        ''',
        None,
    )
    if result is None:
        return None
    return [row[0] for row in result]

def get_followings(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        select username from user
        where id in (SELECT following_id FROM followorfollowing WHERE follower_id = "{userId}");
        ''',
        None,
    )
    if result is None:
        return None
    return [row[0] for row in result]
# define function to search for a track by title and artist and genre and ages and area 

def search_track(dbm: DBM, title=None, artist=None, genre=None, ages=None, area=None):
    if not dbm:
        return None
    
    conditions = []
    if title:
        conditions.append(f"title LIKE '%{title}%'")
    if artist:
        conditions.append(f"artist LIKE '%{artist}%'")
    if genre:
        conditions.append(f"genre LIKE '%{genre}%'")
    if ages:
        conditions.append(f"ages LIKE '%{ages}%'")
    if area:
        conditions.append(f"area LIKE '%{area}%'")
    
    if not conditions:
        return None
    
    query = "SELECT * FROM tracks WHERE " + " OR ".join(conditions)
    
    result = dbm.db_execute_read_query(query, None)
    return result

def add_follower(dbm: DBM, userId=None, followerId=None):
    if not dbm or not userId or userId == "" or not followerId or followerId == "" or userId == followerId:
        return False
    try:
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                followorfollowing (follower_id,following_id)
                VALUES
                ("{followerId}","{userId}");
            """,
            None,
        )
    except Exception as e:
        return False
    

def fetch_artist_tracks(dbm: DBM, artist=None):
    if not dbm or not artist or artist == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM tracks WHERE artist = "{artist}";
        ''',
        None,
    )
    return result

def send_friend_request(dbm: DBM, userId=None, friendId=None):
    if not dbm or not userId or userId == "" or not friendId or friendId == "" or userId == friendId:
        return False
    try:
        if are_friends(dbm, userId, friendId):
            return False
        return dbm.db_execute_query(
            f"""
            INSERT INTO
            friend_request (freind_send,friend_get, accept_reject)
            SELECT * FROM (SELECT "{userId}","{friendId}", 0) AS tmp
            WHERE NOT EXISTS (
            SELECT freind_send,friend_get FROM friend_request 
            WHERE freind_send = "{userId}" AND friend_get = "{friendId}"
            );
            """,
            None,
        )
    except Exception as e:
        return False

def are_friends(dbm: DBM, userId=None, friendId=None):
    if not dbm or not userId or userId == "" or not friendId or friendId == "":
        return False
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM friend
        WHERE (user_id = "{userId}" AND friend_id = "{friendId}")
        OR (user_id = "{friendId}" AND friend_id = "{userId}");
        ''',
        None,
    )
    return len(result) > 0
    
def get_requests(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT u.username FROM friend_request AS fr
        JOIN user AS u ON fr.freind_send = u.id
        WHERE fr.friend_get = "{userId}" and fr.accept_reject = 0;
        ''',
        None,
    )
    return result

def get_friends(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        select username from user
        where id in (SELECT friend_id FROM friend WHERE user_id = "{userId}")
        OR id in (SELECT user_id FROM friend WHERE friend_id = "{userId}");
        ''',
        None,
    )
    if result is None:
        return None
    return [row[0] for row in result]
    
def delete_friend(dbm: DBM, userId=None, friendId=None):
    if not dbm or not userId or userId == "" or not friendId or friendId == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            DELETE FROM friend
            WHERE user_id = "{userId}" AND friend_id = "{friendId}"
            OR user_id = "{friendId}" AND friend_id = "{userId}";
            """,
            None,
        )
    except Exception as e:
        return False


def accept_friend_request(dbm: DBM, userId=None, friendId=None):
    if not dbm or not userId or userId == "" or not friendId or friendId == "":
        return False
    try:
        dbm.db_execute_query(
            f"""
            DELETE FROM friend_request
            WHERE freind_send = "{friendId}" AND friend_get = "{userId}";
            """,
            None,
        )
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                friend (user_id,friend_id)
                VALUES
                ("{userId}","{friendId}");
            """,
            None,
        )
    except Exception as e:
        return False

def reject_friend_request(dbm: DBM, userId=None, friendId=None):
    if not dbm or not userId or userId == "" or not friendId or friendId == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            UPDATE friend_request
            SET accept_reject = 1
            WHERE freind_send = "{friendId}" AND friend_get = "{userId}";
            """,
            None,
        )
    except Exception as e:
        return False
    

def get_rejects(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT u.username FROM friend_request AS fr
        JOIN user AS u ON fr.freind_send = u.id
        WHERE fr.friend_get = "{userId}" and fr.accept_reject = 1;
        ''',
        None,
    )
    return result

def add_msg_toTable(dbm: DBM, senderId=None, receiverId=None, msgText=None):
    if not dbm or not senderId or senderId == "" or not receiverId or receiverId == "" or not msgText or msgText == "":
        return False
    try:
        if are_friends(dbm, senderId, receiverId):
            return dbm.db_execute_query(
                f"""
                INSERT INTO
                    message (sender_id, receiver_id, message_text)
                    VALUES
                    ("{senderId}", "{receiverId}", "{msgText}");
                """,
                None,
            )
        else:
            return False
    except Exception as e:
        return False
    
def get_messages(dbm: DBM, receiverId=None):
    if not dbm or not receiverId or receiverId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT m.message_text, u.username
        FROM message AS m
        JOIN user AS u ON m.sender_id = u.id
        WHERE m.receiver_id = "{receiverId}";
        ''',
        None,
    )
    return result

def search(dbm: DBM, title=None, artist=None, genre=None, ages=None, area=None):
    if  dbm is None or title is None or artist is None or genre is None or ages is None or area is None:
        return None
    
    result = dbm.db_execute_read_query(
        f'''
        SELECT * 
        FROM tracks INNER JOIN user ON tracks.artist_id = user.id
        WHERE title like "%{title}%" AND user.fname || " " || user.lname like "%{artist}%" AND genre like "%{genre}%" AND ages like "%{ages}%" AND area like "%{area}%";
        ''',
        None,
    )
    return result

def remove_follower_fromTable(dbm: DBM, userId=None, followerId=None):
    if not dbm or not userId or userId == "" or not followerId or followerId == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            DELETE FROM followorfollowing
            WHERE follower_id = "{followerId}" AND following_id = "{userId}";
            """,
            None,
        )
    except Exception as e:
        return False
    
def remove_following_fromTable(dbm: DBM, userId=None, followingId=None):
    if not dbm or not userId or userId == "" or not followingId or followingId == "":
        return False
    try:
        return dbm.db_execute_query(
            f"""
            DELETE FROM followorfollowing
            WHERE follower_id = "{userId}" AND following_id = "{followingId}";
            """,
            None,
        )
    except Exception as e:
        return False

    
def get_artist_musics(dbm: DBM, artist_id):
    if not dbm or not artist_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM tracks WHERE artist_id = "{artist_id}";
        ''',
        None
    )
    return result

def get_column_headers(dbm: DBM, table_name):
    if not dbm or not table_name:
        return None
    result = dbm.db_execute_read_query(
        f'''
        PRAGMA table_info({table_name});
        ''',
        None
    )
    return [row[1] for row in result]

def delete_from_tracks(dbm: DBM, track_id):
    if not dbm or not track_id:
        return False
    try:
        dbm.db_execute_query(
            f'''
            DELETE FROM tracks WHERE id = "{track_id}";
            ''',
            None
        )
        dbm.db_execute_query(
            f'''
            DELETE FROM albums WHERE track_id = "{track_id}";
            ''',
            None
        )
        dbm.db_execute_query(
            f'''
            DELETE FROM comment WHERE track_id = "{track_id}";
            ''',
            None
        )
        dbm.db_execute_query(
            f'''
            DELETE FROM likes WHERE track_id = "{track_id}";
            ''',
            None
        )
        dbm.db_execute_query(
            f'''
            DELETE FROM playlist_music WHERE track_id = "{track_id}";
            ''',
            None
        )
        return True
    except Exception as e:
        return False
    
def get_artist_concerts(dbm: DBM, artist_id):
    if not dbm or not artist_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM concert WHERE artist_id = "{artist_id}";
        ''',
        None
    )
    return result

def get_concert_price(dbm: DBM, concert_id):
    if not dbm or not concert_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT ticket_price FROM concert WHERE id = "{concert_id}";
        ''',
        None
    )
    return result[0][0] if result else None

def delete_from_concerts (dbm: DBM, concert_id):
    if not dbm or not concert_id:
        return False
    try:
        dbm.db_execute_query(
            f'''
            UPDATE user
            SET wallet = wallet + {get_concert_price(dbm, concert_id)}
            WHERE id IN (SELECT user_id FROM ticket WHERE concert_id = {concert_id});
            ''',
            None
        )
        dbm.db_execute_query(
            f'''
            DELETE FROM concert WHERE id = "{concert_id}";
            ''',
            None
        )
        dbm.db_execute_query(
            f'''
            DELETE FROM ticket WHERE concert_id = "{concert_id}";
            ''',
            None
        )
        return True
    except Exception as e:
        return False

def add_concert_toTable(dbm: DBM, name, artist_id, venue, date, ticket_price):
    if not dbm:
        return False
    if (
        not name
        or not artist_id
        or not venue
        or not date
        or not ticket_price
        or name == ""
        or artist_id == ""
        or venue == ""
        or date == ""
        or ticket_price == ""
    ):
        return False
    try:
        return dbm.db_execute_query(
            f"""
            INSERT INTO
                concert (name,artist_id,venue,date,ticket_price)
                VALUES
                ("{name}","{artist_id}","{venue}","{date}","{ticket_price}");
            """,
            None,
        )
    except Exception as e:
        return False
    
def get_user_tickets(dbm: DBM, user_id):
    if not dbm or not user_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT c.name FROM ticket t, concert c
        WHERE t.concert_id=c.id and user_id = "{user_id}" and expired = 0;
        ''',
        None
    )
    return result

def remove_ticket_fromTable(dbm: DBM, user_id, concert_title):
    if not dbm or not user_id or not concert_title:
        return False
    try:
        x= dbm.db_execute_read_query(
            f'''
            SELECT t.concert_id FROM ticket t, concert c
            WHERE t.concert_id=c.id and c.name = "{concert_title}" and t.user_id = "{user_id}";
            ''',
            None
        )
        return dbm.db_execute_query(
            f'''
            DELETE FROM ticket WHERE user_id = "{user_id}" AND concert_id="{x[0][0]}";
            ''',
            None
        )
    except Exception as e:
        return False
    
def get_username_by_userid(dbm: DBM, user_id):
    if not dbm or not user_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT username FROM user WHERE id = "{user_id}";
        ''',
        None
    )
    return result[0][0] if result else None

def add_music_toTable(dbm: DBM, title, artist_id, album, duration, genre, ages, lyric, area, permission):
    if not dbm:
        return False
    if (
        not title
        or not artist_id
        or not duration
        or not genre
        or not ages
        or not lyric
        or not area
        or title == ""
        or artist_id == ""
        or duration == ""
        or genre == ""
        or ages == ""
        or lyric == ""
        or area == ""
        or permission == ""
    ):
        return False
    try:
        dbm.db_execute_query(
            f"""
            INSERT INTO
            tracks (title,duration,genre,ages,lyric,area,artist_id,permission)
            VALUES
            ("{title}","{duration}","{genre}","{ages}","{lyric}","{area}","{artist_id}","{permission}");
            """,
            None,
        )
        if album != '' and album is not None:
            dbm.db_execute_query(
                f"""
                insert into albums (title,track_id,artist_id)
                  values ("{album}",(select id from tracks where (title,duration,genre,ages,lyric,area,artist_id,permission) = ("{title}","{duration}","{genre}","{ages}","{lyric}","{area}","{artist_id}","{permission}")),"{artist_id}");
                """,
                None,
            )
        return True
    except Exception as e:
        return False

def get_user_expired_tickets(dbm: DBM, user_id):
    if not dbm or not user_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT c.name FROM ticket t, concert c
        WHERE t.concert_id=c.id and user_id = "{user_id}" and expired = 1;
        ''',
        None
    )
    return result

def get_album_tracks(dbm: DBM, album_title):
    if not dbm or not album_title:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM tracks WHERE id in (select track_id from albums
                                          where title = "{album_title}");
        ''',
        None
    )
    return result
    

def get_albums(dbm: DBM):
    if not dbm:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM albums;
        ''',
        None
    )
    return result

def get_followingusername_userid(dbm: DBM, userId=None):
    if not dbm or not userId or userId == "":
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT username FROM user
        WHERE id IN (SELECT following_id FROM followorfollowing WHERE follower_id = {userId});
        ''',
        None
    )
    return result

def get_suggestion(dbm: DBM, user_id):
    if not dbm or not user_id:
        return None
    liked_genres = dbm.db_execute_read_query(
        f'''
        SELECT DISTINCT genre
        FROM tracks
        WHERE id IN (
            SELECT track_id
            FROM likes
            WHERE user_id = "{user_id}"
        );
        ''',
        None
    )
    result = dbm.db_execute_read_query(
        f'''
        SELECT *
        FROM tracks
        WHERE genre IN (
            SELECT DISTINCT genre
            FROM tracks
            WHERE id IN (
                SELECT track_id
                FROM likes
                WHERE user_id = "{user_id}"
            )
        )
        AND id NOT IN (
            SELECT track_id
            FROM likes
            WHERE user_id = "{user_id}"
        );
        ''',
        None
    )
    return result

def get_playlists(dbm: DBM):
    if not dbm:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM playlist where public_private = 0;
        ''',
        None
    )
    return result

def get_artists(dbm: DBM):
    if not dbm:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM user WHERE singerornormal = 1;
        ''',
        None
    )
    return result

def get_concerts(dbm: DBM):
    if not dbm:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM concert;
        ''',
        None
    )
    return result

def get_playlist_tracks(dbm: DBM, playlistname):
    if not dbm or not playlistname:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT * FROM tracks WHERE id in (select track_id from playlist_music
                                          where playlist_id in (select id from playlist where name = "{playlistname}"));
        ''',
        None
    )
    return result

def add_ticket_toTable(dbm: DBM, user_id, concert_id):
    if not dbm or not user_id or not concert_id or get_user_wallet(dbm, user_id) < get_concert_price(dbm, concert_id):
        return False
    try:
        # Check if ticket is already bought
        result = dbm.db_execute_read_query(
            f'''
            SELECT * FROM ticket WHERE user_id = "{user_id}" AND concert_id = "{concert_id}";
            ''',
            None
        )
        if result:
            return False
        
        dbm.db_execute_query(
            f"""
            INSERT INTO
                ticket (user_id,concert_id)
                VALUES
                ("{user_id}","{concert_id}");
            """,
            None,
        )
        dbm.db_execute_query(
            f"""
            update user
            set wallet = wallet - {get_concert_price(dbm, concert_id)}
            where id = "{user_id}";
            """,
            None,
        )
        return True
    except Exception as e:
        return False
    
def get_user_wallet(dbm: DBM, user_id):
    if not dbm or not user_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT wallet FROM user WHERE id = "{user_id}";
        ''',
        None
    )
    return result[0][0] if result else None

def add_to_playlist_table(dbm: DBM, playlistname, track_id, user_id):
    if not dbm or not playlistname or not track_id or not user_id:
        return False
    try:
        dbm.db_execute_query(
            f"""
            INSERT INTO
                playlist (name,user_id,public_private)
                VALUES
                ("{playlistname}","{user_id}",0);
            """,
            None,
        )
        dbm.db_execute_query(
            f"""
            INSERT INTO
                playlist_music (playlist_id,track_id)
                VALUES
                ((select id from playlist where name = "{playlistname}"),"{track_id}");

            """,
            None,
        )
        return True
    except Exception as e:
        return False
    
def get_user_playlists(dbm: DBM, user_id):
    if not dbm or not user_id:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT name FROM playlist WHERE user_id = "{user_id}";
        ''',
        None
    )
    return result
def make_playlist_public(dbm: DBM, playlistname):
    if not dbm or not playlistname:
        return False
    try:
        dbm.db_execute_query(
            f"""
            update playlist
            set public_private = 0
            where name = "{playlistname}";
            """,
            None,
        )
        return True
    except Exception as e:
        return False

def make_playlist_private(dbm: DBM, playlistname):
    if not dbm or not playlistname:
        return False
    try:
        dbm.db_execute_query(
            f"""
            update playlist
            set public_private = 1
            where name = "{playlistname}";
            """,
            None,
        )
        return True
    except Exception as e:
        return False
    
def like_playlistTable(dbm: DBM, user_id, playlist_id):
    if not dbm or not user_id or not playlist_id:
        return False
    try:
        result = dbm.db_execute_read_query(
            f'''
            SELECT * FROM like_playlist WHERE user_id = "{user_id}" AND playlist_id = "{playlist_id}";
            ''',
            None
        )
        if result:
            return False
        
        dbm.db_execute_query(
            f"""
            INSERT INTO
                like_playlist (user_id,playlist_id)
                VALUES
                ("{user_id}","{playlist_id}");
            """,
            None,
        )
        return True
    except Exception as e:
        return False
    
def get_playlistid_by_name(dbm: DBM, playlistname):
    if not dbm or not playlistname:
        return None
    result = dbm.db_execute_read_query(
        f'''
        SELECT id FROM playlist WHERE name = "{playlistname}";
        ''',
        None
    )
    return result[0][0] if result else None

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

