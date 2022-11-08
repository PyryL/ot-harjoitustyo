import unittest
from competition import Competition
from competitor import Competitor

class CompetitionTest(unittest.TestCase):
    def setUp(self):
        self.john_doe = Competitor("John Doe", 57, "Compile & Run club")
        self.competition = Competition("Helsinki marathon", [self.john_doe])
    
    def test_competition_name(self):
        self.assertEqual(self.competition.name, "Helsinki marathon")
    
    def test_competitor_list_at_start(self):
        self.assertListEqual(self.competition.competitors, [self.john_doe])
    
    def test_competitor_adding(self):
        another_competitor = Competitor("Matti Meikäläinen", 175, "Hello world runners")
        self.competition.add_competitor(another_competitor)
        self.assertListEqual(self.competition.competitors, [self.john_doe, another_competitor])
    
    def test_competitor_removal(self):
        self.competition.remove_competitor(self.john_doe)
        self.assertListEqual(self.competition.competitors, [])
    
    def test_initialization_from_dictionary(self):
        competition_dict = {
            "name": "Helsinki marathon",
            "competitors": [
                {
                    "name": "John Doe",
                    "bib": 57,
                    "club": "Compile & Run club"
                }
            ]
        }
        competition = Competition.init_from_dict(competition_dict)
        self.assertEqual(str(competition), "Helsinki marathon, 1 competitors")
        
    def test_invalid_initialization_from_dictionary(self):
        invalid_competition_dict = {
            "competitors": []
        }
        self.assertRaises(KeyError, lambda : Competition.init_from_dict(invalid_competition_dict))
