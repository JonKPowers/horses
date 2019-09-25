from BaseObjects.RaceID import RaceID
from BaseObjects.HorseID import HorseID
from BaseObjects.RaceClass import RaceClass
from BaseObjects.TimeSplits import TimeSplits
from BaseObjects.Payouts import Payouts

from Exceptions.exceptions import RaceNotFoundException

from typing import List, Dict
from DBHandler.DBHandler import DBHandler

from BaseObjects.race_db_mappings import consolidated_races_attribute_map

from datetime import date
from datetime import datetime

class Race:
    def __init__(self, race_id: RaceID, db_handler: DBHandler):
        self.db = db_handler

        self.race_id = race_id
        self.track: str = race_id.track
        self.race_num: int = race_id.race_num
        self.race_date : date = race_id.date
        self.race_time: datetime = None

        self.race_name: str = None
        self.race_class: RaceClass = None

        self.distance: int = None
        self.planned_distance: int = None
        self.run_up_distance: int = None
        self.rail_distance: int = None

        self.temp: float = None
        self.weather: str = None
        self.surface: str = None
        self.all_weather_surface: bool = None
        self.surface_condition: str = None
        self.surface_change: bool = None

        # Information about horses in race:
        # horse_in_race dict has format {post_position: HorseID}
        self.horses_in_race: Dict[int, HorseID] = dict()
        self.horses_scratched: List[HorseID] = list()
        self.num_horses = None

        # Information about race times:
        self.splits: TimeSplits = None

        # Finish information
        self.win: HorseID = None
        self.place: HorseID = None
        self.show: HorseID = None

        # Payout information
        self.payouts: Payouts = None

    def _generate_where_for_race(self, race_id: RaceID):
        return f'date="{race_id.date}" AND track="{race_id.track}" ' \
               f'AND race_num="{race_id.race_num}"'
