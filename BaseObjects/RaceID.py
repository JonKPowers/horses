from datetime import date
from BaseObjects import RaceID

class RaceID:
    def __init__(self, _date: date, track: str, race_num: int):
        self.date: date = _date
        self.track: str = track
        self.race_num: int = race_num
        self.race_id: str = self._get_race_id()

    def _get_race_id(self) -> str:
        return f'{self.date}{self.track}{self.race_num}'

    def __str__(self):
        return f'{self.date}{self.track}{self.race_num}'

    def __hash__(self):
        return hash((self.race_id, self.track, self.race_num))

    def __eq__(self, other: RaceID):
        return self.race_id == other.race_id
