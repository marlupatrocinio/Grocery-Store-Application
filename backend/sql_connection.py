import mysql.connector

__conn = None

def get_sql_connection():
    global __conn
    if __conn is None:
        __conn = mysql.connector.connect(user = 'root', password = '123456Pw!',
                                host = 'localhost',
                                database = 'GS_app')
    return __conn