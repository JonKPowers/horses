import unittest
from unittest import TestCase
from unittest.mock import Mock

from BaseObjects.Horse import Horse

from Exceptions.exceptions import HorseNotFoundException

from datetime import date

class TestHorseObject(unittest.TestCase):
    def setUp(self) -> None:
        """
        All tests here are done on a blank Horse object. A mock DBHandler is used to
        satisfy the __init__() requirements of the Horse Object but is not used for
        the tests.

        :return:
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
        return_values = ([('DRIP BREW', 14, 3, 'NC', "YES IT'S TRUE", 'SONOROUS')],
                         ['horse_name', 'birth_year', 'foaling_month', 'where_bred', 'sire', 'dam'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values
        self.horse.get_bio()

        self.assertTrue(isinstance(self.horse.birthday, date), 'Birthday not set')




if __name__ == '__main__':
    unittest.main()
