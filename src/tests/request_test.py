import unittest
from services.request import Request

class TestRequest(unittest.TestCase):
    def test_ping_request(self):
        url = "https://pyry.info/timekeeper/ping"
        response_status, response_text = Request().make_request(url, "GET", {})
        self.assertEqual(response_status, 200)
        self.assertEqual(response_text, "pong")
