import unittest
from unittest.mock import Mock

from DBHandler.DBHandler import DBHandler

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race

from constants.db_info import consolidated_races_db

from datetime import date, datetime

class TestRaceInit(unittest.TestCase):
    def setUp(self) -> None:
        self.db_handler = Mock()

        self.year = 2019
        self.month = 1
        self.day = 1

        self.race_id = RaceID(date(self.year, self.month, self.day), 'HOU', 5)
        self.race = Race(self.race_id, self.db_handler)

    def test_sets_race_info_from_RaceID(self):
        self.assertTrue(self.race.track == 'HOU')
        self.assertTrue(self.race.race_num == 5)
        self.assertEqual(date(2019, 1, 1), self.race.race_date)

    def test_sets_attributes_from_consolidated_races_table(self):
        return_values = ([(None, 1320, 1320, 29, 0, 66, 'Showery', 'A', 'FT', 0, 7)],
                         ['race_name', 'distance', 'planned_distance', 'run_up_distance', 'temp_rail_distance',
                          'temperature', 'weather', 'surface', 'track_condition', 'off_turf', 'field_size'])
        self.db_handler.generate_query.return_value = 'This is a SQL query string'
        self.db_handler.query_db.return_value = return_values

        # Run the method we're testing
        self.race._get_consolidated_races_data()

        # Check for the results we're expecting
        for control_value, column in zip(return_values[0][0], return_values[1]):
            attribute_value = getattr(self.race, self.race.consolidated_races_mappings[column])
            self.assertEqual(attribute_value, control_value, f'Column: {column}. '
                                                             f'Attribute: {attribute_value}. '
                                                             f'Control value: {control_value}.')

    def test_gets_right_time_for_datetime(self):
        input_times: List[int] = [900, 1500]
        correct_times: List[datetime] = [datetime(self.year, self.month, self.day, 9, 00),
                                         datetime(self.year, self.month, self.day, 15, 00)]
        self.db_handler.generate_query.return_value = 'This is a SQL query string'

        # For each testing time, call the method we're testing
        for test_time, control_time in zip(input_times, correct_times):
            result: datetime = self.race._generate_race_datetime(test_time)
            self.assertEqual(control_time, result,
                             f'Incorrectly gave {result} for input {test_time}. Should have been {control_time}.')




if __name__ == '__main__':
    unittest.main()
