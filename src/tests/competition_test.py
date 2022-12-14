import unittest
from datetime import datetime, timedelta
from entities.competition import Competition
from entities.competitor import Competitor, SpecialResult

class CompetitionTest(unittest.TestCase):
    def setUp(self):
        self.john_doe = Competitor("John Doe", 57, "Compile & Run club", None)
        start_time = datetime(2022, 11, 24, 12, 5, 17, 937554)
        self.competition = Competition("Helsinki marathon", [self.john_doe], start_time)
    
    def test_competition_name(self):
        self.assertEqual(self.competition.name, "Helsinki marathon")
    
    def test_competitor_list_at_start(self):
        self.assertListEqual(self.competition.competitors, [self.john_doe])
    
    def test_start_time_after_init(self):
        self.assertEqual(str(self.competition.start_time), "2022-11-24 12:05:17.937554")
    
    def test_competitor_adding(self):
        another_competitor = Competitor("Matti Meikäläinen", 175, "Hello world runners", None)
        self.competition.add_competitor(another_competitor)
        self.assertListEqual(self.competition.competitors, [self.john_doe, another_competitor])
    
    def test_competitor_removal(self):
        self.competition.remove_competitor(self.john_doe)
        self.assertListEqual(self.competition.competitors, [])
    
    def test_competitor_result(self):
        finish_time = datetime(2022, 11, 24, 12, 27, 13, 614432)
        competitor = Competitor("Matti Meikäläinen", 175, "Hello world runners", finish_time)
        result = self.competition.result_of_competitor(competitor)
        self.assertEqual(result, timedelta(0, 1315, 676878))

    def test_competitior_special_result(self):
        competitor = Competitor("Matti Meikäläinen", 175, "Hello world runners", SpecialResult.DID_NOT_START)
        result = self.competition.result_of_competitor(competitor)
        self.assertEqual(result, SpecialResult.DID_NOT_START)
    
    def test_competitor_result_with_none(self):
        result = self.competition.result_of_competitor(self.john_doe)
        self.assertIsNone(result)
    
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

    def test_initialization_from_dictionary_with_missing_keys(self):
        competition = Competition.init_from_dict({})
        self.assertEqual(competition.name, "")
        self.assertListEqual(competition.competitors, [])
        self.assertIsNone(competition.start_time)

    def test_saving_to_dictionary(self):
        # make competition to have one competitor who has finished
        self.competition.remove_competitor(self.john_doe)
        finish_time = datetime(2022, 11, 24, 12, 32, 58, 2314)
        competitor = Competitor("Matti Meikäläinen", 121, "Hello world runners", finish_time)
        self.competition.add_competitor(competitor)

        obj = self.competition.save_into_dict()
        correct_obj = {
            "name": "Helsinki marathon",
            "start": "2022-11-24T12:05:17.937554",
            "competitors": [{
                "name": "Matti Meikäläinen",
                "bib": 121,
                "club": "Hello world runners",
                "finish": "2022-11-24T12:32:58.002314"
            }]
        }
        self.assertDictEqual(obj, correct_obj)
