
import pymysql

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='Abcd268377',
        database='',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        # create table
        with connection.cursor() as cursor:
            pass

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)