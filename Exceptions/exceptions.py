from BaseObjects.RaceID import RaceID
from BaseObjects.HorseID import HorseID

class HorseNotFoundException(Exception):
    pass

class PerformanceNotFoundException(Exception):
    def __init__(self, race_id: RaceID, horse_id: HorseID):
        self.race = race_id
        self.horse = horse_id

class RaceNotFoundException(Exception):
    def __init__(self, race_id: RaceID):
        self.race = race_id