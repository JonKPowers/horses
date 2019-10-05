from BaseObjects.RaceID import RaceID
from BaseObjects.HorseID import HorseID
from BaseObjects.RaceClass import RaceClass
from BaseObjects.TimeSplits import TimeSplits
from BaseObjects.Payouts import Payouts

from Exceptions.exceptions import RaceNotFoundException, DuplicateHorseException

from typing import List, Dict
from DBHandler.DBHandler import DBHandler

from constants.db_info import consolidated_races_db, consolidated_races_table, consolidated_performances_table


from BaseObjects.race_db_mappings import consolidated_races_attribute_map, time_split_mappings

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
        self.post_position_missing: List[HorseID] = list()

        # Information about race times:
        self.splits: TimeSplits = None

        # Finish information
        self.win: HorseID = None
        self.place: HorseID = None
        self.show: HorseID = None
        self.fourth_place: HorseID = None
        self.fifth_place: HorseID = None

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

    def _get_horses_in_race(self) -> None:
        """Populates Race.horses_in_race, Race.horses_scratched, and Race.post_positions from db data"""

        # Get data from db
        sql = self.db.generate_query('horses_consolidated_performances',
                                     ['horse_name', 'horse_id', 'post_position'],
                                     where=self._generate_where_for_race())
        self.db.set_db(consolidated_races_db)
        horses = self.db.query_db(sql)

        for horse in horses:
            horse_id = HorseID(horse[0], horse[1])
            # Populate Race.horses_in_race
            self.horses_in_race.append(horse_id)

            # Populate post positions. Send to scratches if 99, and send to post_position_missing if no info
            if horse[2] == 99:
                self.horses_scratched.append(horse_id)
            elif horse[2] is None:
                self.post_position_missing.append(horse_id)
            else:
                self.post_positions[horse[2]] = horse_id

    def _get_time_splits(self) -> TimeSplits:
        self.db.set_db(consolidated_races_db)
        sql = self.db.generate_query(consolidated_races_db, time_split_mappings.keys(),
                                     where=self._generate_where_for_race())
        times, columns = self.db.query_db(sql, return_col_names=True)

        splits = TimeSplits(self.race_id)
        for time, column in zip(times[0], columns):
            splits.time[time_split_mappings[column]] = time

        return splits

    def _get_placed_horses(self):
        place_spots: Dict = {
            1: 'win',
            2: 'place',
            3: 'show',
            4: 'fourth_place',
            5: 'fifth_place',
        }

        # Set to use consolidated races db
        self.db.set_db(consolidated_races_db)
        sql = self.db.generate_query(consolidated_performances_table,
                                     ['horse_name', 'horse_id', f'position_{self.distance}'],
                                     where=self._generate_where_for_race(),
                                     other=f'AND position_{self.distance} IN (1, 2, 3, 4, 5)')
        horses = self.db.query_db(sql)

        # Set win/place/show/4th/5th attributes based on horse's finish position
        for horse in horses:
            # Check if there's a horse already found for that finish position
            if getattr(self, place_spots[horse[2]]) is not None:
                raise DuplicateHorseException(getattr(self, place_spots[horse[2]]), HorseID(horse[0], horse[1]))

            setattr(self, place_spots[horse[2]], HorseID(horse[0], horse[1]))

        # After going through horses, check if any of win/place/etc. are empty
        # If so, put generic unknown horse in there

        for place in place_spots.keys():
            if getattr(self, place_spots[place]) is None:
                setattr(self, place_spots[place], HorseID.unknown_horse())






    def _get_race_time_pacific(self) -> int:
        sql = self.db.generate_query('race_info', ['post_time_pacific'], where=self._generate_where_for_race())
        return int(self.db.query_db(sql)[0][0])

    def _generate_where_for_race(self):
        return f'date="{self.race_date}" AND track="{self.track}" AND race_num="{self.race_num}"'
