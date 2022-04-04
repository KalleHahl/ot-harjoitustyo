from oliot.elokuva import Elokuva
from oliot.kayttaja import Kayttaja

class Applikaatio:

    def __init__(self, ):
        self.kayttaja = None

    
    def lisaa_elokuva(self, elokuva):

        leffa = Elokuva(elokuva)
        return leffa

    #def luo_kayttaja(self, kayttaja):
