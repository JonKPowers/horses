from BaseObjects.race_types import RaceIDList, PerformanceDict
from BaseObjects.RaceID import RaceID
from BaseObjects.HorseID import HorseID
from BaseObjects.PeopleInfo import JockeyID, TrainerID, OwnerID
from BaseObjects.HorsePerformance import HorsePerformance

from DBHandler.DBHandler import DBHandler
from BaseObjects.horse_db_mappings import bio_fields, horse_performance_fields

from constants.db_info import bio_db, horse_races_db, horse_performance_db
from constants.db_info import bio_table, horse_races_tables, horse_performance_table
from constants.db_info import horse_performance_attribute_map as attribute_map

from Exceptions.exceptions import HorseNotFoundException, PerformanceNotFoundException

from typing import Dict, List

from datetime import date


class Horse:
    def __init__(self, horse_name: str, db_handler: DBHandler, test_mode=False):

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
        # todo _get_owners still needs to be implemented
        self.owners: Dict[RaceID, OwnerID] = dict()

        # Populate Horse attributes
        # if initialize_data"
        #   self._get_bio()

    def get_bio(self):

        # Pull info from db and set attributes
        query = self.db.generate_query(self.db_bio_table, self.db_mappings_bio.keys(),
                                       where=f'horse_name = "{self.horse_name}"')
        self.db.set_db(bio_db)
        results, columns = self.db.query_db(query, return_col_names=True)
        try:
            for value, column in zip(results[0], columns):
                setattr(self, self.db_mappings_bio[column], value)
        except IndexError as e:
            print(f'Horse not found: {self.horse_name}')
            raise HorseNotFoundException

        # Use birthday data to set birthday; assume born 1st day of month
        self.birthday = date(self._fix_birth_year(), self.birth_month, 1)

    def get_days_old(self, reference_date: date) -> int:
        days_old = (reference_date - self.birthday).days
        return 0 if days_old < 0 else days_old

    def get_days_since_last_race(self, reference_date:date) -> int:
        """Determines how many days have elapsed between horse's last race and the reference date.
        Returns 0 if this is its first race."""

        len_races = len(self.races)

        # Base case 1: No previous races -> return 0
        if len_races == 0:
            return 0

        # Base case 2: reference_date is before the earliest race on record:
        if reference_date < self.races[0].date:
            return 0

        # The general case: linear search of self.races
        for i in range(len(self.races)):
            try:
                if self.races[i].date < reference_date < self.races[i + 1].date:
                    return (reference_date - self.races[i].date).days
            except IndexError:
                if i == len_races - 1 and self.races[i].date < reference_date:
                    return (reference_date - self.races[i].date).days

    def get_weight(self, reference_date: date) -> int:
        pass

    def _get_races(self):
        queries = list()
        for table in horse_races_tables:
            queries.append(self.db.generate_query(table, horse_races_tables[table],
                                                  where=f'horse_name="{self.horse_name}"'))
        self.db.set_db(horse_races_db)
        races = self.db.query_db(" UNION ".join(queries))

        # Generate list of RaceIDs and sort them in chronological order
        self.races = [RaceID(race[0], race[1], race[2]) for race in races]
        self.races.sort(key=lambda x: x.date)

    def _get_race_performances(self):
        # Generate list of db fields
        db_fields = list()
        for topic in horse_performance_fields:
            db_fields.extend(horse_performance_fields[topic].keys())

        # Make sure we're using the consolidated performances db
        self.db.set_db(horse_performance_db)

        for race in self.races:
            try:
                self.performances[race] = self._get_race_performance(race, db_fields)
            except PerformanceNotFoundException as e:
                self.performance_not_found_list.append(e)

    def _get_race_performance(self, race_id: RaceID, fields: list) -> HorsePerformance:
        # Get performance data from db
        sql = self.db.generate_query(horse_performance_table, fields, where=self._generate_where_for_race(race_id))
        results, columns = self.db.query_db(sql, return_col_names=True)

        # Raise PerformanceNotFoundException if no race data in db--these are tracked in self.performance_not_found_list
        if len(results) == 0:
            raise PerformanceNotFoundException(race_id, HorseID(self.horse_name))

        horse_performance = HorsePerformance(race_id)
        for value, column in zip(results[0], columns):
            key = attribute_map[column][0]
            distance = attribute_map[column][1]
            if key == 'position':
                horse_performance.position[distance] = value
            elif key == 'lead_or_beaten':
                horse_performance.lead_or_beaten[distance] = value
            else: raise Exception   #todo better error handling
        return horse_performance

    def _get_weights(self):
        self.db.set_db(horse_performance_db)

        for race in self.races:
            sql = self.db.generate_query(horse_performance_table, ['weight'], where=self._generate_where_for_race(race))
            weight = self.db.query_db(sql)[0][0]
            self.weights[race] = weight

    def _get_jockeys(self):
        self.db.set_db(horse_performance_db)

        for race in self.races:
            sql = self.db.generate_query(horse_performance_table, ['jockey', 'jockey_id'],
                                         where=self._generate_where_for_race(race))
            jockey_info = self.db.query_db(sql)[0]

            self.jockeys[race] = JockeyID(jockey_info[0], jockey_info[1])

    def _get_trainers(self):
        self.db.set_db(horse_performance_db)

        for race in self.races:
            sql = self.db.generate_query(horse_performance_table, ['trainer', 'trainerID'],
                                         where=self._generate_where_for_race(race))
            trainer_info = self.db.query_db(sql)
            self.trainers[race] = TrainerID(trainer_info[0], trainer_info[1])

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
