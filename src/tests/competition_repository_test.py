import unittest
import os
from repositories.competition_repository import CompetitionRepository
from tests.exporting_test import ExportTestHelper

class CompetitionRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.base_path = "test-competitions"
        self._init_directory()
        self.repository = CompetitionRepository(self.base_path)
    
    def tearDown(self):
        # remove the test directory and its contents
        self._init_directory()

    def _init_directory(self):
        try:
            # remove all the contents of the directory
            for file in os.listdir(self.base_path):
                os.remove(os.path.join(self.base_path, file))

            # remove the directory itself
            os.rmdir(self.base_path)
        except FileNotFoundError:
            pass

    def test_getting_nonexistant_competition(self):
        competition = self.repository.get_competition("ab12cd34")
        self.assertIsNone(competition)

    def test_setting_competition_makes_it_available(self):
        competition = ExportTestHelper.generate_competition()
        competition_id = "oi4uty63"
        self.repository.set_competition(competition_id, competition)

        received_competition = self.repository.get_competition(competition_id)
        self.assertIsNotNone(received_competition)
        self.assertEqual(received_competition.name, "Helsinki marathon")
        self.assertEqual(len(received_competition.competitors), 3)
    
    def test_updating_competition_applies_changes(self):
        # add first version of the competition
        competition = ExportTestHelper.generate_competition()
        competition_id = "oi4uty63"
        self.repository.set_competition(competition_id, competition)

        # make a little change
        competition.remove_competitor(competition.competitors[0])
        self.repository.set_competition(competition_id, competition)

        # check that the change has been saved
        received_competition = self.repository.get_competition(competition_id)
        self.assertEqual(len(received_competition.competitors), 2)
