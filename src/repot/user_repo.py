import sqlite3
from database_connection import get_database_route
db = get_database_route()


class Kayttajarepo:

    def __init__(self, filu):
        self._filu = filu
    
    def luo_kayttaja(self, kayttaja):

        cursor = self._filu.cursor()
        cursor.execute("INSERT INTO Kayttajat (nimi, salasana) VALUES (?, ?)", (kayttaja.nimi, kayttaja.salis) )
        self._filu.commit()
        return kayttaja






kayttajarepo = Kayttajarepo(db)