import pymysql.cursors


def conectar():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='dbescola',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

