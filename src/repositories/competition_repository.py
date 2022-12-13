import json
from services.request import Request
from services.login import Login
from entities.competition import Competition

class CompetitionRepository:
    def __init__(self, request = Request(), login = Login()):
        self._request = request
        self._login = login
        self._url = "https://pyry.info/timekeeper/competitions/index.php"

    def generate_new_id(self):
        params = {
            "token": self._login.get_token()
        }
        response_status, response_text = self._request.make_request(self._url, "POST", params)
        if response_status != 201:
            return None
        response_body = json.loads(response_text)
        return response_body["id"]

    def get_competition(self, competition_id):
        params = {
            "id": competition_id,
            "token": self._login.get_token()
        }
        response_status, response_text = self._request.make_request(self._url, "GET", params)
        if response_status != 200:
            return None
        response_body = json.loads(response_text)
        return Competition.init_from_dict(response_body)

    def set_competition(self, competition_id, new_value):
        params = {
            "id": competition_id,
            "content": json.dumps(new_value.save_into_dict()),
            "token": self._login.get_token()
        }
        response_status, _ = self._request.make_request(self._url, "PUT", params)
        return response_status == 200
