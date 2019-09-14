from BaseObjects.race_types import RaceIDList, PerformanceDict
from BaseObjects.RaceID import RaceID
from BaseObjects.PeopleInfo import JockeyID, TrainerID, OwnerID

from DBHandler.DBHandler import DBHandler
from BaseObjects.horse_db_mappings import bio_fields

from constants.db_info import bio_table

from Exceptions.exceptions import HorseNotFoundException

from typing import Dict

from datetime import date


class Horse:
    def __init__(self, horse_name: str, db_handler: DBHandler):
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
        self.races: RaceIDList = None
        self.performances: PerformanceDict = dict()
        self.weights: Dict[RaceID, int] = dict()
        self.jockeys: Dict[RaceID, JockeyID] = dict()
        self.trainers: Dict[RaceID, TrainerID] = dict()
        self.owners: Dict[RaceID, OwnerID] = dict()

    def get_bio(self):
        query = self.db.generate_query(self.db_bio_table, self.db_mappings_bio.keys(),
                                       where=f'horse_name = "{self.horse_name}"')
        results, columns = self.db.query_db(query, return_col_names=True)
        try:
            for value, column in zip(results[0], columns):
                setattr(self, self.db_mappings_bio[column], value)
        except IndexError as e:
            print(f'Horse not found: {self.horse_name}')
            raise HorseNotFoundException

    def _get_races(self):
        pass

    def _get_race_performance(self, ):
        pass
