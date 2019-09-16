from datetime import date
from BaseObjects import RaceID

class RaceID:
    def __init__(self, _date: date, track: str, race_num: int):
        self.date: date = _date
        self._track: str = track
        self._race_num: int = race_num
        self._race_id: str = self._get_race_id()

    def _get_race_id(self) -> str:
        return f'{self.date}{self._track}{self._race_num}'

    def __str__(self):
        return f'{self.date}{self._track}{self._race_num}'

    def __hash__(self):
        return hash((self._race_id, self._track, self._race_num))

    def __eq__(self, other: RaceID):
        return (self._race_id, self._track, self._race_num) == (other._race_id, other._track, other._race_num)
