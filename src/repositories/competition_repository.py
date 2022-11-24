import requests
import json
from entities.competition import Competition

class CompetitionRepository:
    def __init__(self):
        self._base_path = "competitions"

    def get_competition(self, id):
        try:
            file = open(f"{self._base_path}/{id}.json", encoding="utf-8")
        except FileNotFoundError:
            return None

        obj = json.load(file)
        file.close()
        return Competition.init_from_dict(obj)

    def set_competition(self, id, newValue):
        obj = newValue.save_into_dict()
        with open(f"{self._base_path}/{id}.json", "w", encoding="utf-8") as file:
            json.dump(obj, file)
