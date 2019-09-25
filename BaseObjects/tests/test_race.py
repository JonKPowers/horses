import unittest

from DBHandler.DBHandler import DBHandler

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race

from constants.db_info import consolidated_races_db

from datetime import date

class TestSpinUp(unittest.TestCase):
    def setUp(self) -> None:
        self.db_handler = Mock()

        self.race_id = RaceID(date(2019, 1, 1), 'HOU', 5)
        self.race = Race(self.race_id, self.db_handler)

    def test_sets_race_info_from_RaceID(self):
        self.assertTrue(self.race.track == 'HOU')
        self.assertTrue(self.race.race_num == 5)
        self.assertEqual(date(2019, 1, 1), self.race.race_date)

    def test_sets_attributes_from_consolidated_races_table(self):
        return_values = ()
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values

        for control_value, column in zip(return_values[0][0], return_values[1]):
            attribute_value = getattr(horse, self.race.consolidated_races_attribute_map[column])
            self.assertEqual(attribute_value, control_value, f'Attribute: {attribute_value}. '
                                                             f'Control value: {control_value}')

if __name__ == '__main__':
    unittest.main()
