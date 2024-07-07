import DBManagement
from dbfunctions import *

dbm = DBManagement.DBM()
dbm.db_connect()
# delete_all_db(dbm)
#print(check_login(dbm, "negin", "1234"))

create_db_tables(dbm)
# dbm.db_execute_query(
#     f'''
#     INSERT INTO
#         user (fname,lname,email,address,username,password)
#         VALUES
#         ("negin","dashti","negin@gmail.com","Around YAZD Province","negin","1234");
#     ''', None
# )

dbm.db_disconnect()