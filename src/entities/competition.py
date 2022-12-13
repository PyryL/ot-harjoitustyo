from datetime import datetime
from .competitor import Competitor

class Competition:
    def __init__(self, name, competitors, start_time):
        self._name = name
        self._competitors = competitors
        self._start_time = start_time

    @classmethod
    def init_from_dict(cls, obj):
        if "competitors" in obj.keys():
            competitors = [
                Competitor.init_from_dict(competitor)
                for competitor in obj["competitors"]
            ]
        else:
            competitors = []

        start_time = None if "start" not in obj.keys() or obj["start"] is None\
                          else datetime.fromisoformat(obj["start"])
        name = obj["name"] if "name" in obj.keys() else ""

        return Competition(name, competitors, start_time)

    def save_into_dict(self):
        return {
            "name": self._name,
            "start": None if self._start_time is None else self._start_time.isoformat(),
            "competitors": [competitor.save_into_dict() for competitor in self._competitors]
        }

    @property
    def name(self):
        return self._name

    @property
    def competitors(self):
        return self._competitors

    def add_competitor(self, competitor):
        self._competitors.append(competitor)

    def remove_competitor(self, competitor):
        self._competitors.remove(competitor)

    def result_of_competitor(self, competitor):
        if not competitor.has_finished or self._start_time is None:
            return None
        if competitor.finish_time is None:
            return competitor.finish
        return competitor.finish_time - self._start_time

    @property
    def start_time(self):
        return self._start_time

    def start_now(self):
        self._start_time = datetime.now()

    def __str__(self):
        if self._start_time is None:
            timer_info = "not running"
        else:
            timer_info = "started " + self._start_time.isoformat(" ", "seconds")
        return f"{self._name}, {timer_info}, {len(self._competitors)} competitors"
