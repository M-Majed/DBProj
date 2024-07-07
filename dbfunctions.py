from DBManagement import DBM

# dbm = DBManagement.DBM()
# dbm.db_connect()

# WARNING! Deletes all tables and their descriptions!
def drop_all_tables(dbm: DBM):
    # tables = ["user", "tracks", "artists", "albums"] # example 
    tables = ["user"] # later: add all table names 
    if not dbm:
        return False
    for elem in tables:
        dbm.db_execute_query(f'drop table if exists {elem}', None)
    return True

def create_db_tables(dbm: DBM):
    if not dbm:
        return False
    
    # signup: fname lname email address username password
    dbm.db_execute_query(
        '''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
            );
        ''', None
    )

    return True

def check_login(dbm: DBM, username: str, password: str):
    if not dbm or not username or username=="" or not password or password=="":
        return False
    result = dbm.db_execute_read_query(
        f'''
        SELECT COUNT(*) FROM user
        WHERE username = "{username}" AND password = "{password}"
        ''' , None
    )
    print(f'{result=}\t{result[0][0]}')
    countFromDB = result[0][0]
    if countFromDB != 1:
        return False
    return True

def insert_one_user(dbm:DBM, fname,lname,email,address,username,password):
    if not dbm:
        return False
    if not fname or not lname or not email or not address or not username or not password or fname=="" or lname=="" or email=="" or address=="" or username=="" or password=="":
        return False
    try:
        return dbm.db_execute_query(
            f'''
            INSERT INTO
                user (fname,lname,email,address,username,password)
                VALUES
                ("{fname}","{lname}","{email}","{address}","{username}","{password}");
            ''', None
        )
    except Exception as e:
        return False



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