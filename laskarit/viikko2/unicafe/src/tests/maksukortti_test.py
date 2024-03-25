import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortille_laataminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_kortin_saldon_vahentaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test__kortin_saldo_vahentaminen_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    #palauttaa True, jos rahat riittivät, muuten False
    def test_rahat_ottaminen_palauttaa_oikean_arvon_jos_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)