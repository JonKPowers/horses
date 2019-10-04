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

class DuplicateHorseException(Exception):
    def __init__(self, horse_1: HorseID, horse_2: HorseID):
        self.horse_1 = horse_1
        self.horse_2 = horse_2
