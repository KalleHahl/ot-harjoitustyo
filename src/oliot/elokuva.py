class Elokuva:

    def __init__(self, nimi, ohjaaja=None, kasikirjoittaja=None, kuvaaja=None, katsottu=False, kayttaja=None, elokuva_id=None):
        self.nimi = nimi
        self.ohjaaja = ohjaaja
        self.kasikirjoittaja = kasikirjoittaja 
        self.kuvaaja = kuvaaja
        self.katsottu = katsottu
        self.kayttaja = kayttaja
        self.id = elokuva_id