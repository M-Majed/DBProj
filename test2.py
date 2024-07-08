import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))

# create_db_tables(dbm)
dbm.db_execute_query(
    '''
    INSERT INTO
        concert (id, name, artist, venue, date, ticket_price)
        VALUES
        (1, "concert1", "artist1", "venue1", "2021-12-12", 100),
        (2, "concert2", "artist2", "venue2", "2021-12-13", 200),
        (3, "concert3", "artist3", "venue3", "2021-12-14", 300),
        (4, "concert4", "artist4", "venue4", "2021-12-15", 400),
        (5, "concert5", "artist5", "venue5", "2021-12-16", 500);
    ''', None
    )

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