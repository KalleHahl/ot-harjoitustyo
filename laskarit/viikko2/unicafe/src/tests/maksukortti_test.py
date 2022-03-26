import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataus_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    def test_rahan_ottaminen_liikaa(self):
        if self.maksukortti.ota_rahaa(50):
            return True
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        return False
    
    def test_rahan_ottaminen_sopivasti(self):
        if self.maksukortti.ota_rahaa(5):
            return True
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        return False