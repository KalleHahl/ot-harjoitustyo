from multiprocessing import connection
import sqlite3
from database_connection import get_database_route



def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Kayttajat (id INTEGER PRIMARY KEY, nimi, salasana)")

    connection.commit()

def create():
    connection = get_database_route()
    create_tables(connection)

if __name__ == "__main__":
    create()



