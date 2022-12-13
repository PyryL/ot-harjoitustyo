from datetime import datetime
from .competitor import Competitor

class Competition:
    """
    Class representing one competition and its data.

    Attributes:
        name: The name of the competition
        competitors: List of competitors participating the competition
        start_time: Datetime when competition started
    """

    def __init__(self, name, competitors, start_time):
        """Constructor creating a new competition

        Args:
            name (str): The name of the competition
            competitors (Sequence[Competitor]): The participants of the competition
            start_time (Optional[datetime.datetime]): The start time of the competition
        """
        self._name = name
        self._competitors = competitors
        self._start_time = start_time

    @classmethod
    def init_from_dict(cls, obj):
        """Constructor creating a new competition from dictionary.

        Args:
            obj (dict): Dictionary containing data about the competition.
            Possible keys are "competitors", "start", and "name".

        Returns:
            Competition: The constructed competition.
        """

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
        """Creates a dictionary that contains this competition's data.

        Returns:
            dict: The created dictionary.
        """
        return {
            "name": self._name,
            "start": None if self._start_time is None else self._start_time.isoformat(),
            "competitors": [competitor.save_into_dict() for competitor in self._competitors]
        }

    @property
    def name(self):
        """The name of this competition.

        Returns:
            str: The name
        """
        return self._name

    @property
    def competitors(self):
        """Competitors of this competition

        Returns:
            Sequence[Competitor]: The competitors
        """
        return self._competitors

    def add_competitor(self, competitor):
        """Adds new competitor into the list of participants.

        Args:
            competitor (Competitor): The new competitor
        """
        self._competitors.append(competitor)

    def remove_competitor(self, competitor):
        """Remove the competitor from the list of participants of this competition.
        If the competitor does not exist, nothing is done.

        Args:
            competitor (Competitor): The competitor to be removed.
        """
        self._competitors.remove(competitor)

    def result_of_competitor(self, competitor):
        """Calculates the result of the competitor.

        Args:
            competitor (Competitor): The participant whose result is calculated.

        Returns:
            Optional[Union[SpecialResult, datetime.timedelta]]: The result of the competitor.
        """
        if not competitor.has_finished or self._start_time is None:
            return None
        if competitor.finish_time is None:
            return competitor.finish
        return competitor.finish_time - self._start_time

    @property
    def start_time(self):
        """The datetime when this competition started.

        Returns:
            Optional[datetime.datetime]: The start time or `None` if not started yet.
        """
        return self._start_time

    def start_now(self):
        """Sets the start datetime of this competition to now"""
        self._start_time = datetime.now()

    def __str__(self):
        if self._start_time is None:
            timer_info = "not running"
        else:
            timer_info = "started " + self._start_time.isoformat(" ", "seconds")
        return f"{self._name}, {timer_info}, {len(self._competitors)} competitors"
