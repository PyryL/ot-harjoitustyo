import unittest
import os
from services.login import Login

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = Login(".test_login")
        self.valid_token = "0123456789012345678901234567890123456789012345678901234567890123"

    def tearDown(self):
        if os.path.exists(".test_login"):
            os.remove(".test_login")

    def _write_token(self, token = None):
        content = self.valid_token if token is None else token
        with open(".test_login", "w", encoding="utf-8") as file:
            file.write(content)

    def test_getting_token(self):
        self._write_token()
        token = self.login.get_token()
        self.assertEqual(token, self.valid_token)

    def test_getting_token_with_empty_file(self):
        token = self.login.get_token()
        self.assertIsNone(token)

    def test_getting_token_with_invalid_content(self):
        # length is not 64 characters
        self._write_token("abc123")
        token = self.login.get_token()
        self.assertIsNone(token)

    def test_login(self):
        success = self.login.log_in("username", "password")
        self.assertTrue(success)
        token = self.login.get_token()
        self.assertEqual(token, "d839f4e67d83ab6916277d3342203bf00ff6a159a4a661a77b43667569523fb4")

    def test_login_with_hashtag_in_username(self):
        success = self.login.log_in("user#name", "password")
        self.assertFalse(success)

    def test_login_with_empty_username(self):
        success = self.login.log_in("", "password")
        self.assertFalse(success)

    def test_login_with_empty_password(self):
        success = self.login.log_in("username", "")
        self.assertFalse(success)

    def test_logout(self):
        self._write_token()
        self.login.log_out()
        self.assertIsNone(self.login.get_token())
