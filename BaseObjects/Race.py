from BaseObjects.RaceID import RaceID
from BaseObjects.HorseID import HorseID
from BaseObjects.RaceClass import RaceClass
from BaseObjects.TimeSplits import TimeSplits
from BaseObjects.Payouts import Payouts

from Exceptions.exceptions import RaceNotFoundException

from typing import List, Dict
from DBHandler.DBHandler import DBHandler

from constants.db_info import consolidated_races_db, consolidated_races_table

from BaseObjects.race_db_mappings import consolidated_races_attribute_map

from datetime import date
from datetime import datetime
import re


class Race:
    def __init__(self, race_id: RaceID, db_handler: DBHandler):
        self.db = db_handler

        # Mappings between db fields and Race attributes
        self.consolidated_races_mappings = consolidated_races_attribute_map
        self.consolidated_races_table = consolidated_races_table

        self.race_id = race_id
        self.track: str = race_id.track
        self.race_num: int = race_id.race_num
        self.race_date : date = race_id.date
        self.race_time: datetime = None

        self.race_name: str = None
        self.race_class: RaceClass = None

        self.distance: int = None
        self.planned_distance: int = None
        self.distance_change: int = None
        self.run_up_distance: int = None
        self.rail_distance: int = None

        self.temp: float = None
        self.weather: str = None
        self.surface: str = None
        self.surface_condition: str = None
        self.surface_change: bool = None

        # Information about horses in race:
        self.horses_in_race: List[HorseID] = list()
        self.horses_scratched: List[HorseID] = list()
        self.num_horses = None
        self.post_positions: Dict[int, HorseID] = dict()

        # Information about race times:
        self.splits: TimeSplits = None

        # Finish information
        self.win: HorseID = None
        self.place: HorseID = None
        self.show: HorseID = None

        # Payout information
        self.payouts: Payouts = None

    def _get_consolidated_races_data(self):
        self.db.set_db(consolidated_races_db)

        fields = list(consolidated_races_attribute_map.keys())
        sql = self.db.generate_query(self.consolidated_races_table, fields,
                                     where=self._generate_where_for_race())
        results, columns = self.db.query_db(sql)

        try:
            for result, column in zip(results[0], columns):
                setattr(self, self.consolidated_races_mappings[column], result)
        except IndexError as e:
            print(f'Race not found: {self.race_id}')
            raise RaceNotFoundException

    def _generate_race_datetime(self, time_str: str) -> datetime:
        """Takes in string in format 4:15/(3:15)/2:15/1:15 and generates datetime from time in parentheses

            Times are stored in local time with respect to the race location.

            When the post time is higher than 8, there's ambiguity as to whether that's 8PM or 8AM. To resolve this,
            we look at the Pacific post time (post_time_pacific in the race_info table). A race starting at 8PM or
            later Eastern time will have a Pacific time post-time of 1700 or later. Thus, for times with an hour of
            8, we pull the Pacific post time for the race to determine whether it is a morning race or afternoon race.
        """
        time: re.match = re.search(r'\((\d{,2}):(\d{,2})\)', time_str)
        hour: int = int(time.group(1))
        minute: int = int(time.group(2))

        # For morning/afternoon races, convert to 24-hour time
        # For potential night races, check pacific time to confirm whether morning or night (e.g., 8:30 or 9:00)
        # Note: any race that happens to be in 24-hour time should be left alone
        if hour < 8:
            hour += 12
        elif hour < 12 and self._get_race_time_pacific() >= 1700:
            hour += 12

        return datetime(self.race_date.year, self.race_date.month, self.race_date.day, hour, minute)

    def _set_distance_change(self):
        self.distance_change = self.distance - self.planned_distance

    def _get_horses_in_race(self):
        pass

    def _get_race_time_pacific(self) -> int:
        sql = self.db.generate_query('race_info', ['post_time_pacific'], where=self._generate_where_for_race())
        return int(self.db.query_db(sql)[0][0])

    def _generate_where_for_race(self):
        return f'date="{self.race_date}" AND track="{self.track}" AND race_num="{self.race_num}"'
