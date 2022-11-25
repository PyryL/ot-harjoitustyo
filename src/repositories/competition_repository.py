# import requests
import json
import os
import random
from string import ascii_lowercase, digits
from entities.competition import Competition

class CompetitionRepository:
    def __init__(self, base_path = "competitions"):
        self._base_path = base_path

    def generate_new_id(self):
        while True:
            competition_id = "".join(random.choices(ascii_lowercase+digits, k=8))
            if self.get_competition(competition_id) is None:
                return competition_id

    def get_competition(self, competition_id):
        try:
            with open(f"{self._base_path}/{competition_id}.json", encoding="utf-8") as file:
                obj = json.load(file)
                return Competition.init_from_dict(obj)
        except FileNotFoundError:
            return None

    def set_competition(self, competition_id, new_value):
        obj = new_value.save_into_dict()
        self._create_directory()
        with open(f"{self._base_path}/{competition_id}.json", "w", encoding="utf-8") as file:
            json.dump(obj, file)

    def _create_directory(self):
        if not os.path.exists(self._base_path):
            os.mkdir(self._base_path)
