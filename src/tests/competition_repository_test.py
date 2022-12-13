import unittest
from repositories.competition_repository import CompetitionRepository
from tests.exporting_test import ExportTestHelper
from entities.competition import Competition

class RequestStub:
    def __init__(self):
        self.url = None
        self.request_method = None
        self.params = None
        self.failure = False

    def make_request(self, url, request_method, params):
        self.url = url
        self.request_method = request_method
        self.params = params

        if self.failure:
            status_code = 404
        else:
            status_code = 201 if request_method == "POST" else 200

        if request_method == "POST" and not self.failure:
            response = '{"id": "1234"}'
        elif request_method == "GET" and not self.failure:
            response = '{}'
        else:
            response = ""
        return (status_code, response)

class LoginStub:
    def get_token(self):
        return "0123456789012345678901234567890123456789012345678901234567890123"

class CompetitionRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.request = RequestStub()
        self.login = LoginStub()
        self.repository = CompetitionRepository(self.request, self.login)

    def test_getting_competition(self):
        competition = self.repository.get_competition("1234")
        self.assertEqual(type(competition), Competition)
        self.assertEqual(self.request.url, "https://pyry.info/timekeeper/competitions/index.php")
        self.assertEqual(self.request.request_method, "GET")
        expected_params = {
            "id": "1234",
            "token": "0123456789012345678901234567890123456789012345678901234567890123"
        }
        self.assertDictEqual(self.request.params, expected_params)

    def test_getting_competition_with_failure(self):
        self.request.failure = True
        competition = self.repository.get_competition("1234")
        self.assertIsNone(competition)

    def test_setting_competition(self):
        competition = ExportTestHelper.generate_competition()
        competition_id = "1234"
        self.repository.set_competition(competition_id, competition)

        self.assertEqual(self.request.request_method, "PUT")
        self.assertEqual(self.request.url, "https://pyry.info/timekeeper/competitions/index.php")
        self.assertListEqual(list(self.request.params.keys()), ["id", "content", "token"])

    def test_id_generation(self):
        competition_id = self.repository.generate_new_id()
        self.assertEqual(competition_id, "1234")
        self.assertEqual(self.request.url, "https://pyry.info/timekeeper/competitions/index.php")
        self.assertEqual(self.request.request_method, "POST")
        expected_params = {
            "token": "0123456789012345678901234567890123456789012345678901234567890123"
        }
        self.assertDictEqual(self.request.params, expected_params)

    def test_id_generation_with_failure(self):
        self.request.failure = True
        competition_id = self.repository.generate_new_id()
        self.assertIsNone(competition_id)
