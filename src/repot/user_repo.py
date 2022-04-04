import sqlite3
import oliot.kayttaja
db = sqlite3.connect("kayttajat.db")


class Kayttajarepo:

    def __init__(self, filu):
        self._filu = filu
    
    def luo_kayttaja(self, kayttaja):

        cursor = self._filu.cursor()
        cursor.execute("INSERT INTO Kayttajat (nimi, salasana) VALUES (?, ?)", (kayttaja.nimi, kayttaja.salis) )
        self._filu.commit()
        return kayttaja






kayttajarepo = Kayttajarepo(db)