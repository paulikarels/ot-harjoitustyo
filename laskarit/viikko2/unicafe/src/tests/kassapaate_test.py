import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate  = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_aseta_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_alussa_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0.0)
        self.assertEqual(self.kassapaate.maukkaat, 0.0)

    def test_edullisen_osto_toimii_maksun_ollessa_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(300.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240.0)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukkaan_osto_toimii_maksun_ollessa_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_osto_ei_toimi_maksun_ollessa_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(100.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_osto_ei_toimi_maksun_ollessa_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(100.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_korttiosto_true_jos_saldoa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_maukkaan_korttiosto_true_jos_saldoa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortilla_false_jos_ei_tarpeeksi_saldoa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_syo_maukkaasti_kortilla_false_jos_ei_tarpeeksi_saldoa(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    
    def test_edullisen_osto_kortilla_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_ostaminen_kortilla_onnistuu(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahan_lataaminen_kortille_onnistuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20)
    
    def test_rahan_lataaminen_kortille_ei_onnistu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)