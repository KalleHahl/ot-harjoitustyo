import sqlite3
from database_connection import hae_tietokanta_reitti



def luo_taulut(yhteys):
    cursor = yhteys.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Kayttajat (id INTEGER PRIMARY KEY, nimi, salasana)")

    yhteys.commit()

def luo():
    yhteys = hae_tietokanta_reitti()
    luo_taulut(yhteys)

if __name__ == "__main__":
    luo()



