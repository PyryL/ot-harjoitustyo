from competitor import Competitor
from datetime import datetime

class Competition:
    def __init__(self, name, competitors, start_time):
        self._name = name
        self._competitors = competitors
        self._start_time = start_time
    
    @classmethod
    def init_from_dict(cls, obj):
        competitors = [Competitor.init_from_dict(competitor_obj) for competitor_obj in obj["competitors"]]
        return Competition(obj["name"], competitors, obj["start"])
    
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
