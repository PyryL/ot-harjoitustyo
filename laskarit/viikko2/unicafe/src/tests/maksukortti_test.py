import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(350)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 13.50 euroa")
    
    def test_nostaminen_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")
    
    def test_liian_suuren_rahamaaran_nostaminen(self):
        self.maksukortti.ota_rahaa(1300)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_nostaminen_palauttaa_true(self):
        self.assertTrue(self.maksukortti.ota_rahaa(200))

    def test_rahan_nostaminen_palauttaa_false(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1300))