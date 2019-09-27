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

    def _generate_race_datetime(self, time: int) -> datetime:
        pass

    def _generate_where_for_race(self):
        return f'date="{self.race_date}" AND track="{self.track}" AND race_num="{self.race_num}"'
