from BaseObjects.RaceID import RaceID
from BaseObjects.HorseID import HorseID
from BaseObjects.RaceClass import RaceClass
from BaseObjects.TimeSplits import TimeSplits
from BaseObjects.Payouts import Payouts

from typing import List, Dict

from datetime import date
from datetime import datetime

class Race:
    def __init__(self, race_id: RaceID):
        self.race_id = race_id
        self.track: str = race_id.track
        self.race_num: int = race_id.race_num
        self.race_date : date = race_id.date
        self.race_time: datetime = None

        self.race_class: RaceClass = None

        self.temp: float = None
        self.surface: str = None
        self.surface_condition: str = None
        self.surface_change: bool = None

        # Information about horses in race:
        # horse_in_race dict has format {post_position: HorseID}
        self.horses_in_race: Dict[int, HorseID] = dict()
        self.horses_scratched: List[HorseID] = list()

        # Information about race times:
        self.splits: TimeSplits = None

        # Finish information
        self.win: HorseID = None
        self.place: HorseID = None
        self.show: HorseID = None

        # Payout information
        self.payouts: Payouts = None
