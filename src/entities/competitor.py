from datetime import datetime
from enum import Enum

class SpecialResult(Enum):
    DID_NOT_START = "dns"
    DID_NOT_FINISH = "dnf"
    DISQUALIFIED = "dq"

class Competitor:
    def __init__(self, name, bib, club, finish):
        self._name = name
        self._bib = bib
        self._club = club
        self._finish = finish

    @classmethod
    def init_from_dict(cls, obj):
        if obj["finish"] in set(item.value for item in SpecialResult):
            finish = SpecialResult(obj["finish"])
        elif obj["finish"] is not None:
            finish = datetime.fromisoformat(obj["finish"])
        else:
            finish = None

        return Competitor(obj["name"], obj["bib"], obj["club"], finish)

    def save_into_dict(self):
        if isinstance(self._finish, SpecialResult):
            finish = self._finish.value
        elif self._finish is not None:
            finish = self._finish.isoformat()
        else:
            finish = None

        return {
            "name": self._name,
            "bib": self._bib,
            "club": self._club,
            "finish": finish
        }

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
    def finish(self):
        return self._finish

    @property
    def finish_time(self):
        if isinstance(self._finish, SpecialResult) or self._finish is None:
            return None
        return self._finish

    @property
    def has_finished(self):
        return self._finish is not None

    def finish_now(self):
        self._finish = datetime.now()

    def special_result(self, result):
        self._finish = result

    def __str__(self):
        if isinstance(self._finish, SpecialResult):
            finish = self._finish.value.upper()
        elif self._finish is not None:
            finish = "finished at " + self._finish.isoformat(" ", timespec="seconds")
        else:
            finish = "not finished"

        return f"{self._bib}: {self._name}, {self._club}, {finish}"
