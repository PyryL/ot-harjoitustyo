import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)
    

    def test_kassan_raha_aluksi(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_myytyja_edullisia_aluksi(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myytyja_maukkaita_aluksi(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_edullinen_kateisella_kasvattaa_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_kateisella_kasvattaa_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_edullinen_kateisella_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)

    def test_edullinen_riittamaton_kateisella_maaraa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_edullinen_riittamaton_kateisella_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_riittamaton_kateisella_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
    

    def test_maukas_kateisella_kasvattaa_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_kateisella_kasvattaa_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    
    def test_maukas_kateisella_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(vaihtoraha, 50)

    def test_maukas_riittamaton_kateisella_maaraa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukas_riittamaton_kateisella_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_riittamaton_kateisella_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)

    
    def test_edullinen_korttimaksu_ei_muuta_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_korttimaksu_vahentaa_kortin_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 260)
    
    def test_edullinen_korttimaksu_palauttaa_true(self):
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(palautus)
    
    def test_edullinen_korttimaksu_kasvattaa_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_riittamaton_korttimaksu_ei_muuta_saldoa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
    
    def test_edullinen_riittamaton_korttimaksu_palauttaa_false(self):
        kortti = Maksukortti(200)
        palautus = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertFalse(palautus)
    
    def test_edullinen_riittamaton_korttimaksu_maara_ei_muutu(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_maukas_korttimaksu_vahentaa_kortin_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 100)
    
    def test_maukas_korttimaksu_palauttaa_true(self):
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(palautus)
    
    def test_maukas_korttimaksu_kasvattaa_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_riittamaton_korttimaksu_ei_muuta_saldoa(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
    
    def test_maukas_riittamaton_korttimaksu_palauttaa_false(self):
        kortti = Maksukortti(200)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(palautus)
    
    def test_maukas_riittamaton_korttimaksu_maara_ei_muutu(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_kortin_lataus_saldo_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_kortin_lataus_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_negatiivinen_lataus_ei_muuta_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 500)