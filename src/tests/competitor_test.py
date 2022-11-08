import unittest
from competitor import Competitor

class CompetitorTest(unittest.TestCase):
    def setUp(self):
        self.competitor = Competitor("John Doe", 57, "Compile & Run club")
    
    def test_competitor_name(self):
        self.assertEqual(self.competitor.name, "John Doe")
    
    def test_competitor_bib(self):
        self.assertEqual(self.competitor.bib, 57)
    
    def test_competitor_club(self):
        self.assertEqual(self.competitor.club, "Compile & Run club")
    
    def test_competitor_string(self):
        self.assertEqual(str(self.competitor), "57: John Doe, Compile & Run club")

    def test_initialization_from_dictionary(self):
        competitor_dict = {
            "name": "John Doe",
            "bib": 57,
            "club": "Compile & Run club"
        }
        competitor = Competitor.init_from_dict(competitor_dict)
        self.assertEqual(str(competitor), "57: John Doe, Compile & Run club")
    
    def test_invalid_initialization_from_dictionary(self):
        # make sure that the initialization raises when required dictionary key (club) is missing
        invalid_competitor_dict = {
            "name": "John Doe",
            "bib": 57
        }
        self.assertRaises(KeyError, lambda : Competitor.init_from_dict(invalid_competitor_dict))
