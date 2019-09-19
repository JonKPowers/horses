import unittest
from unittest.mock import Mock

from BaseObjects.Horse import Horse
from BaseObjects.RaceID import RaceID
from BaseObjects.HorsePerformance import HorsePerformance

from Exceptions.exceptions import HorseNotFoundException

from datetime import date


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

        self. assertTrue(self.horse.birthday.year >= 1800)
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


class TestHorseRaces(unittest.TestCase):
    def setUp(self) -> None:
        """
        All tests here are done on a blank Horse object. A mock DBHandler is used to
        satisfy the __init__() requirements of the Horse Object but is not used for
        the tests.

        """
        self.db_handler: Mock = Mock()
        self.horse: Horse = Horse(horse_name='Drip Brew', db_handler=self.db_handler)

    def test_race_list_populated(self):
        """
        Make sure that Horse.races is filled with RaceID objects from db data.

        Returns:

        """
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

        self.horse.races = [RaceID(race[0], race[1], race[2]) for race in races]
        self.horse._get_race_performances()

        races_accounted_for = len(self.horse.performances) + len(self.horse.performance_not_found_list)

        self.assertTrue(races_accounted_for != 0, 'Performances are not populating')
        self.assertEqual(len(self.horse.performances) + len(self.horse.performance_not_found_list),
                         len(self.horse.races), 'Some performances are being lost')

    def test_get_race_performance_returns_horse_performance_object(self):

        self.db_handler.generate_query.return_value = "This is an SQL query"
        self.db_handler.query_db.return_value = ([(3, None, 1, None, 3, None, None, None, 3, None, None, None, 8,
                                                   None, None, 6, None, None, None, 0.13, None, -0.6, None, None,
                                                   None, -1.1, None, None, None, -2.0, None, None, -6.75, None)],
                                                 ['position_0', 'position_330', 'position_440', 'position_660',
                                                  'position_880', 'position_990', 'position_1100', 'position_1210',
                                                  'position_1320', 'position_1430', 'position_1540', 'position_1610',
                                                  'position_1650', 'position_1760', 'position_1830', 'position_1870',
                                                  'position_1980', 'lead_or_beaten_0', 'lead_or_beaten_330',
                                                  'lead_or_beaten_440', 'lead_or_beaten_660', 'lead_or_beaten_880',
                                                  'lead_or_beaten_990', 'lead_or_beaten_1100', 'lead_or_beaten_1210',
                                                  'lead_or_beaten_1320', 'lead_or_beaten_1430', 'lead_or_beaten_1540',
                                                  'lead_or_beaten_1610', 'lead_or_beaten_1650', 'lead_or_beaten_1760',
                                                  'lead_or_beaten_1830', 'lead_or_beaten_1870', 'lead_or_beaten_1980'])

        horse_performance = self.horse._get_race_performance(RaceID(date(2019, 1, 1,), 'CD', 1), ['some fields'])
        self.assertTrue(isinstance(horse_performance, HorsePerformance))

if __name__ == '__main__':
    unittest.main()