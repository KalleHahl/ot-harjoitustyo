from oliot.elokuva import Elokuva
from oliot.kayttaja import Kayttaja
from repot.user_repo import (kayttajarepo as default_kayttaja_repo)

class Applikaatio:

    def __init__(self, ):
        self.kayttaja = None
        self._kayttajarepo = default_kayttaja_repo
        self._kayttaja = None

    
    def lisaa_elokuva(self, elokuva):

        leffa = Elokuva(elokuva)
        return leffa

    def luo_kayttaja(self, nimi, salasana, login=True):
        kayttaja = self._kayttajarepo.luo_kayttaja(Kayttaja(nimi, salasana))
        if login:
            self._user = kayttaja

        return kayttaja



applikaatio = Applikaatio()

