
class Competitor:
    def __init__(self, name, bib, club):
        self._name = name
        self._bib = bib
        self._club = club
    
    @classmethod
    def init_from_dict(cls, obj):
        return Competitor(obj["name"], obj["bib"], obj["club"])

    @property
    def name(self):
        return self._name

    @property
    def bib(self):
        return self._bib

    @property
    def club(self):
        return self._club
    
    def __str__(self):
        return f"{self._bib}: {self._name}, {self._club}"
