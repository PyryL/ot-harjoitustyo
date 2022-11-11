import unittest
from datetime import datetime
from competitor import Competitor

class CompetitorTest(unittest.TestCase):
    def setUp(self):
        self.competitor = Competitor("John Doe", 57, "Compile & Run club", None)
    
    def test_competitor_name(self):
        self.assertEqual(self.competitor.name, "John Doe")
    
    def test_competitor_bib(self):
        self.assertEqual(self.competitor.bib, 57)
    
    def test_competitor_club(self):
        self.assertEqual(self.competitor.club, "Compile & Run club")
    
    def test_competitor_finish_time(self):
        self.assertEqual(self.competitor.finish_time, None)
    
    def test_competitor_string(self):
        self.assertEqual(str(self.competitor), "57: John Doe, Compile & Run club, not finished")
    
    def test_competitor_string_with_finish_time(self):
        finish_time = datetime(2022, 11, 10, 17, 38, 2, 741963)
        competitor = Competitor("John Doe", 57, "Compile & Run club", finish_time)
        self.assertEqual(str(competitor), "57: John Doe, Compile & Run club, finished at 2022-11-10 17:38:02")

    def test_initialization_from_dictionary(self):
        competitor_dict = {
            "name": "John Doe",
            "bib": 57,
            "club": "Compile & Run club",
            "finish": "2022-11-10T17:28:02.741963"
        }
        competitor = Competitor.init_from_dict(competitor_dict)
        self.assertEqual(str(competitor), "57: John Doe, Compile & Run club, finished at 2022-11-10 17:28:02")
    
    def test_invalid_initialization_from_dictionary(self):
        # make sure that the initialization raises when required dictionary key (club) is missing
        invalid_competitor_dict = {
            "name": "John Doe",
            "bib": 57
        }
        self.assertRaises(KeyError, lambda : Competitor.init_from_dict(invalid_competitor_dict))
