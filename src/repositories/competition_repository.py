# import requests
import json
from entities.competition import Competition

class CompetitionRepository:
    def __init__(self):
        self._base_path = "competitions"

    def get_competition(self, competition_id):
        try:
            with open(f"{self._base_path}/{competition_id}.json", encoding="utf-8") as file:
                obj = json.load(file)
                return Competition.init_from_dict(obj)
        except FileNotFoundError:
            return None

    def set_competition(self, competition_id, new_value):
        obj = new_value.save_into_dict()
        with open(f"{self._base_path}/{competition_id}.json", "w", encoding="utf-8") as file:
            json.dump(obj, file)
