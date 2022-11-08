from competitor import Competitor

class Competition:
    def __init__(self, name, competitors):
        self._name = name
        self._competitors = competitors
    
    @classmethod
    def init_from_dict(cls, obj):
        competitors = [Competitor.init_from_dict(competitor_obj) for competitor_obj in obj["competitors"]]
        return Competition(obj["name"], competitors)
    
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
    
    def __str__(self):
        return f"{self._name}, {len(self._competitors)} competitors"
