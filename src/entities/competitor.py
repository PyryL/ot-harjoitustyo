from datetime import datetime
from enum import Enum

class SpecialResult(Enum):
    """Class representing rare result notations of a competitor.
    These include "did not start", "did not finish" and "disqualified".
    """
    DID_NOT_START = "dns"
    DID_NOT_FINISH = "dnf"
    DISQUALIFIED = "dq"

class Competitor:
    """Class representing one competitor"""

    def __init__(self, name, bib, club, finish):
        """Constructor creating a new competitor.

        Args:
            name (str): The name of the competitor
            bib (int): The bib number of the competitor
            club (Optional[str]): The club of the competitor
            finish (Optional[Union[SpecialResult, datetime.datetime]]): The finish time
                or result of the competitor, if already finished
        """
        self._name = name
        self._bib = bib
        self._club = club
        self._finish = finish

    @classmethod
    def init_from_dict(cls, obj):
        """Construct a new competitor from a dictionary.

        Args:
            obj (dict): Dictionary containing data about the competitor

        Returns:
            Competitor: The created competitor
        """
        if obj["finish"] in set(item.value for item in SpecialResult):
            finish = SpecialResult(obj["finish"])
        elif obj["finish"] is not None:
            finish = datetime.fromisoformat(obj["finish"])
        else:
            finish = None

        return Competitor(obj["name"], obj["bib"], obj["club"], finish)

    def save_into_dict(self):
        """Create a dictionary containing the data of this competitor.

        Returns:
            dict: The created dictionary
        """
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
        """The name of this competitor

        Returns:
            str: The name
        """
        return self._name

    @property
    def bib(self):
        """The bib number of this competitor

        Returns:
            int: The bib number
        """
        return self._bib

    @property
    def club(self):
        """The club of this competitor.

        Returns:
            Optional[str]: The club
        """
        return self._club

    @property
    def finish(self):
        """The finish data of this competitor.

        Returns:
            Optional[Union[SpecialResult, datetime.datetime]]:
                Datetime when the competitor finished.
        """
        return self._finish

    @property
    def finish_time(self):
        """The finish time of this competitor.
        Is None when not finished yet or marked with SpecialResult.

        Returns:
            Optional[datetime.datetime]: The finish datetime
        """
        if isinstance(self._finish, SpecialResult) or self._finish is None:
            return None
        return self._finish

    @property
    def has_finished(self):
        """Whether this competitor has already finished.

        Returns:
            bool: Whether has finished
        """
        return self._finish is not None

    def finish_now(self):
        """Set the finish time of this competitor to now."""
        self._finish = datetime.now()

    def special_result(self, result):
        """Mark this competitor with one of the SpecialResult instances.

        Args:
            result (SpecialResult): The special result marking to use
        """
        self._finish = result

    def __str__(self):
        if isinstance(self._finish, SpecialResult):
            finish = self._finish.value.upper()
        elif self._finish is not None:
            finish = "finished at " + self._finish.isoformat(" ", timespec="seconds")
        else:
            finish = "not finished"

        return f"{self._bib}: {self._name}, {self._club}, {finish}"
