from typing import Dict

from BaseObjects.RaceID import RaceID


class TimeSplits:
    def __init__(self, race_id: RaceID):
        self.race_id = race_id
        self.time: Dict[int, float] = dict()
        self.time[440] = None
        self.time[660] = None
        self.time[880] = None
        self.time[990] = None
        self.time[1100] = None
        self.time[1210] = None
        self.time[1320] = None
        self.time[1430] = None
        self.time[1540] = None
        self.time[1650] = None
        self.time[1760] = None
        self.time[1800] = None
        self.time[1830] = None
        self.time[1870] = None
        self.time[1980] = None
        self.time[2310] = None
        self.time[2640] = None
        self.time[3080] = None
        self.time[3520] = None

