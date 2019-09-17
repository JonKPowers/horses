from BaseObjects.race_types import RaceIDList, PerformanceDict
from BaseObjects.RaceID import RaceID
from BaseObjects.PeopleInfo import JockeyID, TrainerID, OwnerID

from DBHandler.DBHandler import DBHandler
from BaseObjects.horse_db_mappings import bio_fields

from constants.db_info import bio_table
from constants.db_info import horse_race_tables

from Exceptions.exceptions import HorseNotFoundException, RaceNotFoundException, PerformanceNotFoundException

from typing import Dict, List

from datetime import date


class Horse:
    def __init__(self, horse_name: str, db_handler: DBHandler, initalize_data=True):
        self.races: RaceIDList = []
        self.race_performances = []

        # Uses a passed-in DBHandler to fetch data
        self.db = db_handler

        # Mappings between db fields and our Horse attributes
        self.db_mappings_bio = bio_fields
        self.db_bio_table: str = bio_table

        # Biographical Information
        self.horse_name: str = horse_name
        self.id: int = None
        self.birth_year: int = None
        self.birth_month: int = None
        self.birthday: date = None
        self.birth_state: str = None
        self.sire: str = None
        self.dam: str = None

        # Race History Info
        self.races: RaceIDList = list()
        self.performances: PerformanceDict = dict()
        self.performance_not_found_list: List[PerformanceNotFoundException] = list()
        self.weights: Dict[RaceID, int] = dict()
        self.jockeys: Dict[RaceID, JockeyID] = dict()
        self.trainers: Dict[RaceID, TrainerID] = dict()
        self.owners: Dict[RaceID, OwnerID] = dict()

        # Populate Horse attributes
        # if initialize_data"
        #   self._get_bio()

    def get_bio(self):

        # Pull info from db and set attributes
        query = self.db.generate_query(self.db_bio_table, self.db_mappings_bio.keys(),
                                       where=f'horse_name = "{self.horse_name}"')
        results, columns = self.db.query_db(query, return_col_names=True)
        try:
            for value, column in zip(results[0], columns):
                setattr(self, self.db_mappings_bio[column], value)
        except IndexError as e:
            print(f'Horse not found: {self.horse_name}')
            raise HorseNotFoundException

        # Use birthday data to set birthday; assume born 1st day of month
        self.birthday = date(self._fix_birth_year(), self.birth_month, 1)

    def _get_races(self):
        queries = list()
        for table in horse_race_tables:
            queries.append(self.db.generate_query(table, horse_race_tables[table],
                                                  where=f'horse_name="{self.horse_name}"'))
        races = self.db.query_db(" UNION ".join(queries))

        # Generate list of RaceIDs and sort them in chronological order
        self.races = [RaceID(race[0], race[1], race[2]) for race in races]
        self.races.sort(key=lambda x: x.date)

    def _get_race_performances(self):
        pass

    def _generate_where_for_race(self, race_id: RaceID):
        return f'date="{race_id.date}" AND track="{race_id.track}" ' \
               f'AND race_num="{race_id.race_num}" AND horse_name="{self.horse_name}"'

    def _fix_birth_year(self) -> int:
        if self.birth_year > 1000:
            return self.birth_year
        if self.birth_year >= 80:
            return self.birth_year + 1900
        else:
            return self.birth_year + 2000
