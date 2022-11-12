from datetime import datetime

class Competitor:
    def __init__(self, name, bib, club, finish_time):
        self._name = name
        self._bib = bib
        self._club = club
        self._finish_time = finish_time
    
    @classmethod
    def init_from_dict(cls, obj):
        finish_time = None if obj["finish"] is None else datetime.fromisoformat(obj["finish"])
        return Competitor(obj["name"], obj["bib"], obj["club"], finish_time)

    @property
    def name(self):
        return self._name

    @property
    def bib(self):
        return self._bib

    @property
    def club(self):
        return self._club
    
    @property
    def finish_time(self):
        return self._finish_time
    
    def finish_now(self):
        self._finish_time = datetime.now()
    
    def __str__(self):
        if self._finish_time is None:
            finish_info = "not finished"
        else:
            finish_info = "finished at " + self._finish_time.isoformat(" ", timespec="seconds")
        return f"{self._bib}: {self._name}, {self._club}, {finish_info}"
