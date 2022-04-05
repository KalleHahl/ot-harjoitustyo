import os 
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "kayttajat.db"))

connection.row_factory = sqlite3.Row

def get_database_route():
    return connection