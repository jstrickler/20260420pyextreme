from databaseconnection import DatabaseConnection

from builddb import build_database

build_database()

db_conn = DatabaseConnection()
db_conn2 = DatabaseConnection()
db_conn3 = DatabaseConnection()

db_conn.cursor.execute(
    '''
        select first_name, last_name
        from computer_people
    '''
)

for row in db_conn.cursor.fetchall():
    print(' '.join(row))

for conn in db_conn, db_conn2, db_conn3:
    print(id(conn))