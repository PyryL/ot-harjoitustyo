import requests
import json
import os
import random
from string import ascii_lowercase, digits
from entities.competition import Competition
from services.login import Login

class CompetitionRepository:
    def __init__(self, base_path = "competitions"):
        self._base_path = base_path
        self._login = Login()

    def generate_new_id(self):
        url = "https://pyry.info/timekeeper/competitions/index.php"
        params = {
            "token": self._login.get_token()
        }
        response = requests.request("POST", url, data=params)
        if response.status_code != 201:
            return None
        response_body = json.loads(response.text)
        return response_body["id"]

    def get_competition(self, competition_id):
        url = "https://pyry.info/timekeeper/competitions"
        params = {
            "id": competition_id,
            "token": self._login.get_token()
        }
        response = requests.request("GET", url, params=params)
        if response.status_code != 200:
            return None
        response_body = json.loads(response.text)
        return Competition.init_from_dict(response_body)

    def set_competition(self, competition_id, new_value):
        url = "https://pyry.info/timekeeper/competitions/index.php"
        params = {
            "id": competition_id,
            "content": json.dumps(new_value.save_into_dict()),
            "token": self._login.get_token()
        }
        response = requests.request("PUT", url, data=params)
        return response.status_code == 200

    def _create_directory(self):
        if not os.path.exists(self._base_path):
            os.mkdir(self._base_path)
