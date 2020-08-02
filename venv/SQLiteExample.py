import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c=conn.cursor()
        c.execute("CREATE TABLE employee (ID INTEGER NOT NULL,NAME TEXT,AGE INTEGER )")

        sql="INSERT INTO employee (ID,NAME,AGE) VALUES (?,?,?)"

        data = [(1, 'Alice', 21),(2, 'Bob', 22), (3, 'Chris', 23)]

        c.executemany(sql,data)

        c.execute("SELECT * FROM employee")

        print(c.fetchmany(4))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.commit()
            conn.close()


if __name__ == '__main__':
    create_connection("pythonsqlite.db")
    ## r"C:\sqlite\db\pythonsqlite.db"