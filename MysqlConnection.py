import mysql.connector
try:

    con=mysql.connector.connect(
        user='root',
        password='root',
        database='test',
        host='localhost',
        port=3306

    )
    print(con.is_connected())
    con.close()
except Exception as e:
    print(f'Exception occured : {e}')
    print(f'Exception class name : {e.__class__}')

