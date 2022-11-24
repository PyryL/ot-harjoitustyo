from datetime import datetime
from .competitor import Competitor

class Competition:
    def __init__(self, name, competitors, start_time):
        self._name = name
        self._competitors = competitors
        self._start_time = start_time

    @classmethod
    def init_from_dict(cls, obj):
        competitors = [Competitor.init_from_dict(competitor) for competitor in obj["competitors"]]
        start_time = None if obj["start"] is None else datetime.fromisoformat(obj["start"])
        return Competition(obj["name"], competitors, start_time)

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
        if competitor.finish_time is None or self._start_time is None:
            return None
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
