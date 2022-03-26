
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahat_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukkaita_ja_edullisia_0_alussa(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)
    
    def test_riittava_kateinen_edullinen(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_liian_vahan_kateista_edullinen(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(24), 24)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_riittava_kateinen_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_liian_vahan_kateista_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_tarpeeksi_rahaa_kortilla_edullinen(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(str(kortti), "saldo: 2.6")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_liian_vahan_kortilla_edullinen(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_tarpeeksi_rahaa_kortilla_maukas(self):
        kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(str(kortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.maukkaat, 1) 
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  

    def test_liian_vahan_kortilla_maukas(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    
    def test_kortin_lataus_oikein(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, 50)
        self.assertEqual(str(kortti), "saldo: 5.5")
    
    def test_kortin_lataus_vaarin(self):
        kortti = Maksukortti(500)
        self.kassapaate.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual(str(kortti), "saldo: 5.0")

    






