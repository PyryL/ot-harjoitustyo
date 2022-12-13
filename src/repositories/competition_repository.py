import json
from services.request import Request
from services.login import Login
from entities.competition import Competition

class CompetitionRepository:
    """Class managing storage of the competition instances."""

    def __init__(self, request = Request(), login = Login()):
        """Construct a new repository instance.

        Args:
            request (Request, optional): The class making HTTP requests. Defaults to Request().
            login (Login, optional): The class handling authentication tokens. Defaults to Login().
        """
        self._request = request
        self._login = login
        self._url = "https://pyry.info/timekeeper/competitions/index.php"

    def generate_new_id(self):
        """Reserve a new ID from the server for a new competition.

        Returns:
            int, optional: The received ID
        """
        params = {
            "token": self._login.get_token()
        }
        response_status, response_text = self._request.make_request(self._url, "POST", params)
        if response_status != 201:
            return None
        response_body = json.loads(response_text)
        return response_body["id"]

    def get_competition(self, competition_id):
        """Receive data about a competition from the servers.

        Args:
            competition_id (str): The ID of the competition

        Returns:
            Competition, optional: The received competition, or None in case or error
        """
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
        """Overwrite a competition with updated data.

        Args:
            competition_id (str): The ID of the competition
            new_value (Competition): The updated version of the competition

        Returns:
            bool: Whether the operation was successful
        """
        params = {
            "id": competition_id,
            "content": json.dumps(new_value.save_into_dict()),
            "token": self._login.get_token()
        }
        response_status, _ = self._request.make_request(self._url, "PUT", params)
        return response_status == 200
