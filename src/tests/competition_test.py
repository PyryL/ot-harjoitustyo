import unittest
from datetime import datetime
from competition import Competition
from competitor import Competitor

class CompetitionTest(unittest.TestCase):
    def setUp(self):
        self.john_doe = Competitor("John Doe", 57, "Compile & Run club", None)
        self.competition = Competition("Helsinki marathon", [self.john_doe], None)
    
    def test_competition_name(self):
        self.assertEqual(self.competition.name, "Helsinki marathon")
    
    def test_competitor_list_at_start(self):
        self.assertListEqual(self.competition.competitors, [self.john_doe])
    
    def test_start_time_after_init(self):
        self.assertIsNone(self.competition.start_time)
    
    def test_competitor_adding(self):
        another_competitor = Competitor("Matti Meikäläinen", 175, "Hello world runners", None)
        self.competition.add_competitor(another_competitor)
        self.assertListEqual(self.competition.competitors, [self.john_doe, another_competitor])
    
    def test_competitor_removal(self):
        self.competition.remove_competitor(self.john_doe)
        self.assertListEqual(self.competition.competitors, [])
    
    def test_timer_starting(self):
        self.competition.start_now()
        self.assertAlmostEqual(self.competition.start_time.timestamp(), datetime.now().timestamp(), delta=0.01)
    
    def test_str(self):
        competition = Competition("Helsinki marathon", [self.john_doe], None)
        self.assertEqual(str(competition), "Helsinki marathon, not running, 1 competitors")
    
    def test_initialization_from_dictionary(self):
        competition_dict = {
            "name": "Helsinki marathon",
            "start": "2022-11-10T17:05:11.318524",
            "competitors": [
                {
                    "name": "John Doe",
                    "bib": 57,
                    "club": "Compile & Run club",
                    "finish": None
                }
            ]
        }
        competition = Competition.init_from_dict(competition_dict)
        self.assertEqual(str(competition), "Helsinki marathon, started 2022-11-10 17:05:11, 1 competitors")
        
    def test_invalid_initialization_from_dictionary(self):
        invalid_competition_dict = {
            "competitors": [],
            "start": None
        }
        self.assertRaises(KeyError, lambda : Competition.init_from_dict(invalid_competition_dict))
