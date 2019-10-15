import unittest
from unittest.mock import Mock

from BaseObjects.Horse import Horse
from BaseObjects.RaceID import RaceID
from BaseObjects.HorsePerformance import HorsePerformance
from BaseObjects.PeopleInfo import JockeyID, TrainerID

from Exceptions.exceptions import HorseNotFoundException, PerformanceNotFoundException

from typing import List

from datetime import date
from random import random, choice


class TestHorseBio(unittest.TestCase):
    def setUp(self) -> None:
        """
        All tests here are done on a blank Horse object. A mock DBHandler is used to
        satisfy the __init__() requirements of the Horse Object but is not used for
        the tests.

        """
        self.db_handler: Mock = Mock()
        self.horse: Horse = Horse(horse_name='Drip Brew', db_handler=self.db_handler)

    def test_bio_atttributes(self):
        """
        Checks that the db field mappings in horse_db_mappings match up to attributes on the
        Horse object.
        :return:
        """

        # Check that all fields in db_mappings_bio has corresponding Horse attribute
        for key in self.horse.db_mappings_bio:
            self.assertTrue(hasattr(self.horse, self.horse.db_mappings_bio[key]), f'Missing attribute: {key}')

    def test_sets_bio_attributes(self):
        # Check that Horse attributes are set correctly from db data
        return_values = ([('DRIP BREW', 14, 3, 'NC', "YES IT'S TRUE", 'SONOROUS')],
                         ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        self.horse.get_bio()

        for control_value, column in zip(return_values[0][0], return_values[1]):
            attribute_value = getattr(self.horse, self.horse.db_mappings_bio[column])
            self.assertEqual(attribute_value, control_value, f'Attribute: {attribute_value}. Control:{control_value}')

    def test_bio_attributes_no_data(self):
        return_values = ([], ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        with self.assertRaises(HorseNotFoundException):
            self.horse.get_bio()

    # todo Test for partial missing data

    def test_sets_birthday(self):
        """
        Make sure that a date object is set for the Horse's birthday attribute.

        :return:
        """
        return_values = ([('DRIP BREW', 14, 3, 'NC', "YES IT'S TRUE", 'SONOROUS')],
                         ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        self.horse.get_bio()

        self.assertTrue(isinstance(self.horse.birthday, date), 'Birthday not set')

    def test_sets_birth_century_2000s(self):
        """
        Two-digit years < 80 should be interpreted as 20xx--in the 21st century.

        Returns:

        """
        return_values = ([('DRIP BREW', 1, 3, 'NC', "YES IT'S TRUE", 'SONOROUS')],
                         ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        self.horse.get_bio()

        self.assertTrue(self.horse.birthday.year >= 2000)

    def test_sets_birth_century_1900s(self):
        """
        Two-digit years >= 80 should be interpreted as 19xx--in the 20th century.
        WILL NEED TO UPDATE IF THIS PROGRAM APPROACHES 22ND CENTURY!
        Returns:

        """
        return_values = ([('DRIP BREW', 80, 3, 'NC', "YES IT'S TRUE", 'SONOROUS')],
                         ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        self.horse.get_bio()

        self.assertTrue(self.horse.birthday.year >= 1800)
        self.assertTrue(self.horse.birthday.year <= 2000)

    def test_four_digit_birth_years_not_changed(self):
        """
        Four-digit years from the horse bio db should not be altered.

        Returns:

        """
        return_values = ([('DRIP BREW', 2005, 3, 'NC', "YES IT'S TRUE", 'SONOROUS')],
                         ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        self.horse.get_bio()

        self.assertTrue(self.horse.birthday.year == 2005)


class TestHorseRaceInfo(unittest.TestCase):
    def setUp(self) -> None:
        """
        All tests here are done on a blank Horse object. A mock DBHandler is used to
        satisfy the __init__() requirements of the Horse Object but is not used for
        the tests.

        """
        self.db_handler: Mock = Mock()
        self.horse: Horse = Horse(horse_name='Drip Brew', db_handler=self.db_handler)
        self.fields = ['position_0', 'position_330', 'position_440', 'position_660',
                     'position_880', 'position_990', 'position_1100', 'position_1210',
                     'position_1320', 'position_1430', 'position_1540', 'position_1610',
                     'position_1650', 'position_1760', 'position_1830', 'position_1870',
                     'position_1980',
                     'lead_or_beaten_0', 'lead_or_beaten_330', 'lead_or_beaten_440',
                     'lead_or_beaten_660', 'lead_or_beaten_880', 'lead_or_beaten_990',
                     'lead_or_beaten_1100', 'lead_or_beaten_1210', 'lead_or_beaten_1320',
                     'lead_or_beaten_1430', 'lead_or_beaten_1540', 'lead_or_beaten_1610',
                     'lead_or_beaten_1650', 'lead_or_beaten_1760', 'lead_or_beaten_1830',
                     'lead_or_beaten_1870', 'lead_or_beaten_1980']

    def get_fake_performance(self, performance_not_found_frequency: float = 0.0) -> tuple:
        if performance_not_found_frequency > 0.0 and random() <= performance_not_found_frequency:
            return ([], self.fields)

        return ([(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                  # start lead_or_beaten
                  -6.1, -5.2, -4.3, -3.4, -2.5, -1.6, -0.7, 1.8, 2.9,
                  3.0, 4.1, 5.2, 6.3, 7.4, 8.5, 9.6, 10.7)], self.fields)

    def get_fake_races(self, num_races: int = 1) -> List[RaceID]:
        races = list()
        for i in range(num_races):
            races.append(RaceID(date(2019, 9, 1), 'CD', i+1))
        return races

    def get_fake_weight(self) -> int:
        """Generates fake horse weight in the range of 116-126"""
        return [(int((random() * 10) + 116),)]

    def get_fake_jockey(self):
        """Returns fake jockey info, randomly selected from the list below"""
        jockeys = [['DIEGO I V', 102309], ['VALDEZ - JIMINEZ ERNESTO', 144056], ['ARELLANO IVAN', 130638],
                   ['RISENHOOVER SASHA', 140163], ['CABRERA DAVID', 150833], ['RAMOS A B', 98853],
                   ['STILLION BROOKE', 157166], ['DIEGO I V', 102309], ['PIVARAL GERBER', 156600],
                   ['DIEGO I V', 102309], ['GONDRON T D', 738], ['CABRERA DAVID', 150833],
                   ['WADE LYNDIE', 126441], ['PARKER D L', 1432], ['ARELLANO IVAN', 130638],
                   ['NAUPAC CASSANDRA', 156139], ['PEREZ FRANCISCO ESCALERA', 149905], ['SINGH R R', 2772],
                   ['MCNEIL BRYAN', 111515], ['URIETA VICTOR MANUEL JR', 157033]]

        return choice(jockeys)

    def get_fake_trainer(self):
        """Returns fake trainer info, randomly selected from the list below"""
        trainers = [['TORREZ JERENESTO', 33116], ['AFLEUR RENEE', 226868], ['ASMUSSEN STEVEN M', 5621],
                    ['DAVIDSON M BRENT', 11716], ['PISH DANNY', 45129], ['STROOPE LARRY', 30431],
                    ['WILLIS MINDY', 5395], ['SHORT THOMAS', 20152], ['DAVIDSON M BRENT', 11716],
                    ['HATCHER NATHAN D', 16018], ['GONZALEZ ISAI V', 242887], ['COURTEMANCHE CANDY R', 235231],
                    ['WHITELAW MICHAEL R', 16003], ['CHACALTANA DOMINGO', 257551], ['BRYANT GEORGE', 12416],
                    ['HATCHER NATHAN D', '16018'], ['NOLEN KENNETH', 7783], ['BARTON AMANDA', 255349],
                    ['OFFOLTER JOE S', 25395], ['SALISBURY JOYCE', 232128], ['GRIMALDO JOSE', 208946],
                    ['MCANALLY JOE', 260833], ['JACKS KAREN E', 280419], ['LOVE ALAN', 2437]]

        return choice(trainers)

    def test_race_list_populated(self):
        """ Make sure that Horse.races is filled with RaceID objects from db data. """
        races = [(date(2016, 6, 19), 'AP', 6), (date(2016, 8, 4), 'AP', 8),
                 (date(2016, 8, 28), 'AP', 7), (date(2016, 10, 14), 'HAW', 9),
                 (date(2016, 11, 11), 'HAW', 3), (date(2016, 11, 26), 'HAW', 5),
                 (date(2016, 12, 22), 'HAW', 2), (date(2016, 12, 29), 'HAW', 1),
                 (date(2017, 3, 17), 'HAW', 4), (date(2018, 4, 13), 'HAW', 4),
                 (date(2018, 4, 28), 'HAW', 1), (date(2018, 5, 18), 'AP', 1),
                 (date(2018, 6, 8), 'AP', 1), (date(2018, 6, 29), 'AP', 2),
                 (date(2018, 7, 20), 'AP', 2), (date(2018, 8, 10), 'AP', 7),
                 (date(2018, 9, 6), 'AP', 1), (date(2018, 9, 21), 'AP', 4),
                 (date(2018, 10, 20), 'HAW', 8)]

        self.db_handler.generate_query.return_value = "This is an SQL query"
        self.db_handler.query_db.return_value = races
        self.horse._get_races()

        self.assertTrue(len(self.horse.races) > 0, 'horse.races not populated')
        self.assertTrue(isinstance(self.horse.races[0], RaceID))

    def test_empty_race_list_for_first_timer(self):
        """
        Make sure Horse.races is an empty list for a horse that has not run any previous races.

        Returns:

        """

        races = []

        self.db_handler.generate_query.return_value = "This is an SQL query"
        self.db_handler.query_db.return_value = races
        self.horse._get_races()

        self.assertTrue(isinstance(self.horse.races, list), 'horse.races is not a list but should be')
        self.assertTrue(len(self.horse.races) == 0, 'horse.races is not an empty list for first-timer horse')

    def test_performances_list_populated(self):
        # Set up races in Horse object
        self.horse.races = self.get_fake_races(num_races=10)

        # Set up db_handler responses:
        self.db_handler.generate_query.return_value = 'This is an SQL query'
        self.db_handler.query_db.return_value = self.get_fake_performance(performance_not_found_frequency=0.3)
        self.horse._get_race_performances()

        races_accounted_for = len(self.horse.performances) + len(self.horse.performance_not_found_list)

        self.assertTrue(races_accounted_for != 0,
                        f'Performances are not populating: looked for{len(self.horse.races)}, found {races_accounted_for}')
        self.assertEqual(len(self.horse.performances) + len(self.horse.performance_not_found_list),
                         len(self.horse.races), 'Some performances are being lost')

    def test_get_race_performance_returns_horse_performance_object(self):
        position_not_set: str = 'Position attribute not set correctly'
        lead_beaten_not_set: str = 'lead_or_beaten_not_set'
        self.db_handler.generate_query.return_value = "This is an SQL query"
        self.db_handler.query_db.return_value = self.get_fake_performance()

        horse_performance = self.horse._get_race_performance(RaceID(date(2019, 1, 1, ), 'CD', 1), ['some fields'])
        self.assertTrue(isinstance(horse_performance, HorsePerformance))

        self.assertTrue(horse_performance.position[0] == 1, position_not_set)
        self.assertTrue(horse_performance.position[330] == 2, position_not_set)
        self.assertTrue(horse_performance.position[440] == 3, position_not_set)
        self.assertTrue(horse_performance.position[660] == 4, position_not_set)
        self.assertTrue(horse_performance.position[880] == 5, position_not_set)
        self.assertTrue(horse_performance.position[990] == 6, position_not_set)
        self.assertTrue(horse_performance.position[1100] == 7, position_not_set)
        self.assertTrue(horse_performance.position[1210] == 8, position_not_set)
        self.assertTrue(horse_performance.position[1320] == 9, position_not_set)
        self.assertTrue(horse_performance.position[1430] == 10, position_not_set)
        self.assertTrue(horse_performance.position[1540] == 11, position_not_set)
        self.assertTrue(horse_performance.position[1610] == 12, position_not_set)
        self.assertTrue(horse_performance.position[1650] == 13, position_not_set)
        self.assertTrue(horse_performance.position[1760] == 14, position_not_set)
        self.assertTrue(horse_performance.position[1830] == 15, position_not_set)
        self.assertTrue(horse_performance.position[1870] == 16, position_not_set)
        self.assertTrue(horse_performance.position[1980] == 17, position_not_set)

        self.assertTrue(horse_performance.lead_or_beaten[0] == -6.1, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[330] == -5.2, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[440] == -4.3, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[660] == -3.4, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[880] == -2.5, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[990] == -1.6, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1100] == -0.7, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1210] == 1.8, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1320] == 2.9, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1430] == 3.0, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1540] == 4.1, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1610] == 5.2, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1650] == 6.3, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1760] == 7.4, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1830] == 8.5, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1870] == 9.6, lead_beaten_not_set)
        self.assertTrue(horse_performance.lead_or_beaten[1980] == 10.7, lead_beaten_not_set)

    def test_get_race_performance_raises_exception_if_performance_not_found(self):
        self.db_handler.generate_query.return_value = "This is an SQL query"
        self.db_handler.query_db.return_value = ([],
                                                 ['position_0', 'position_330', 'position_440', 'position_660',
                                                  'position_880', 'position_990', 'position_1100', 'position_1210',
                                                  'position_1320', 'position_1430', 'position_1540', 'position_1610',
                                                  'position_1650', 'position_1760', 'position_1830', 'position_1870',
                                                  'position_1980',
                                                  'lead_or_beaten_0', 'lead_or_beaten_330', 'lead_or_beaten_440',
                                                  'lead_or_beaten_660', 'lead_or_beaten_880', 'lead_or_beaten_990',
                                                  'lead_or_beaten_1100', 'lead_or_beaten_1210', 'lead_or_beaten_1320',
                                                  'lead_or_beaten_1430', 'lead_or_beaten_1540', 'lead_or_beaten_1610',
                                                  'lead_or_beaten_1650', 'lead_or_beaten_1760', 'lead_or_beaten_1830',
                                                  'lead_or_beaten_1870', 'lead_or_beaten_1980'])

        with self.assertRaises(PerformanceNotFoundException) as exception_catcher:
            horse_performance = self.horse._get_race_performance(RaceID(date(2019, 1, 1, ), 'CD', 1), ['some fields'])

    def test_gets_weights(self):
        # Set up db_handler responses
        self.horse.races = self.get_fake_races(num_races=10)
        self.db_handler.generate_query.return_value = 'This is a SQL query'
        self.db_handler.query_db.return_value = self.get_fake_weight()

        # Run method being tested
        self.horse._get_weights()

        # See if it worked
        self.assertTrue(len(self.horse.races) != 0, 'Horse.races not populated for test_gets_weights')
        self.assertEqual(len(self.horse.weights), len(self.horse.races), 'Weights not being populated correctly')
        for race in self.horse.weights:
            self.assertTrue(isinstance(self.horse.weights[race], int), 'Weight is not stored as an int')

    def test_gets_jockeys(self):
        # Set up db_handler responses
        self.db_handler.generate_query.return_value = 'This is an SQL query'
        self.db_handler.query_db.return_value = [self.get_fake_jockey()]
        self.horse.races = self.get_fake_races(num_races=10)

        # Run the method being tested
        self.horse._get_jockeys()

        # See if it works
        self.assertTrue(len(self.horse.races) != 0, 'Races not populated for test_gets_jockeys')
        self.assertEqual(len(self.horse.jockeys), len(self.horse.races), 'Horse.jockeys not being populated')
        for race in self.horse.jockeys:
            self.assertTrue(isinstance(self.horse.jockeys[race], JockeyID), 'Horse.jockeys has non-JockeyID content')

    def test_gets_trainers(self):
        # Set up db_handler responses
        self.horse.races = self.get_fake_races(num_races=10)
        self.db_handler.generate_query.return_value = 'This is an SQL query'
        self.db_handler.query_db.return_value = self.get_fake_trainer()

        # Run the method being tested
        self.horse._get_trainers()

        # See if it works
        self.assertTrue(len(self.horse.races) != 0, 'Races not populating for test_gets_trainers')
        self.assertTrue(len(self.horse.trainers) == len(self.horse.races), 'Horse.trainers not populating correctly')
        for race in self.horse.trainers:
            self.assertTrue(isinstance(self.horse.trainers[race], TrainerID), 'Horse.trainers has non-TrainerID content')

class TestDynamicFunctions(unittest.TestCase):
    def setUp(self):
        self.db = Mock()

    def test_days_old_calculation_basic(self):
        sut = Horse('Test Horse', self.db, test_mode=True)
        sut.birthday = date(2019, 1, 1)

        reference_date = date(2019, 2, 1)
        control_days_between = 31

        # Run SUT
        test_days_between = sut.get_days_old(reference_date)

        # Check the output
        self.assertEqual(control_days_between, test_days_between,
                         f'Days not being calculated correctly. Returned {test_days_between} between Jan 1 and Feb 1')

    def test_days_old_calculation_too_early(self):
        # Set up initial state
        sut = Horse('Test Horse', self.db, test_mode=True)
        sut.birthday = date(2019, 1, 1)

        reference_date = date(2018, 12, 1)

        # Run SUT
        test_days_between = sut.get_days_old(reference_date)

        # Check the output: If reference date if before birthday, it should return 0
        self.assertEqual(0, test_days_between,
                         f'Not returning 0 when reference date is before Horse.birthday')

    def test_days_since_last_race_basic(self):
        # Set up SUT: Horse with races on 1/1/2019, 2/1/2019, and 3/1/2019
        sut = Horse('Test horse', self.db, test_mode=True)
        sut.races.append(RaceID(date(2019, 1, 1), 'CD', 1))
        sut.races.append(RaceID(date(2019, 2, 1), 'CD', 2))
        sut.races.append(RaceID(date(2019, 3, 1), 'CD', 3))
        sut.races.sort(key=lambda x: x.date)

        # Run SUT and check output
        self.assertEqual(sut.get_days_since_last_race(date(2019, 1, 15)), 14)
        self.assertEqual(sut.get_days_since_last_race(date(2019, 2, 15)), 14)
        self.assertEqual(sut.get_days_since_last_race(date(2019, 3, 15)), 14)
        self.assertEqual(sut.get_days_since_last_race(date(2018, 12, 1)), 0)


    def test_days_since_last_race_first_race(self):
        # Set up SUT: Horse with no previous races
        sut = Horse('Test horse', self.db, test_mode=True)

        # Run SUT and check output; should be zero when horse has no race history
        self.assertEqual(sut.get_days_since_last_race(date(2019, 1, 1)), 0)

    def test_get_weight_as_of_particular_date(self):
        self.fail('Write the test')
        # Might be able to refactor code to separate out the search function and apply it to both
        # weight and days_since_last_race search

if __name__ == '__main__':
    unittest.main()
