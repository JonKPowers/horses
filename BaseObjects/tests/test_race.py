import unittest
from unittest.mock import Mock, patch

from DBHandler.DBHandler import DBHandler

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race

from constants.db_info import consolidated_races_db

from datetime import date, datetime, time

class TestRaceInit(unittest.TestCase):
    def setUp(self) -> None:
        self.db_handler = Mock()

        self.year = 2019
        self.month = 1
        self.day = 1

        self.track: str = 'HOU'
        self.race_num: int = 5

        self.race_id = RaceID(date(self.year, self.month, self.day), self.track, self.race_num)
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

    def test_gets_right_time_for_datetime_basic(self):
        input_times: List[int] = ['4:15/(3:15)/2:15/1:15', '4:44/(3:44)/2:44/1:44',
                                  '5:17/(4:17)/3:17/2:17', '5:50/(4:50)/3:50/2:50']
        correct_times: List[datetime] = [datetime(self.year, self.month, self.day, 15, 15),
                                         datetime(self.year, self.month, self.day, 15, 44),
                                         datetime(self.year, self.month, self.day, 16, 17),
                                         datetime(self.year, self.month, self.day, 16, 50)]
        self.db_handler.generate_query.return_value = 'This is a SQL query string'

        # For each testing time, call the method we're testing
        for test_time, control_time in zip(input_times, correct_times):
            result: datetime = self.race._generate_race_datetime(test_time)
            self.assertEqual(result, control_time,
                             f'Incorrectly gave {result} for input {test_time}. Should have been {control_time}.')

    @patch.object(Race, '_get_race_time_pacific')
    def test_gets_right_time_night_times(self, mock_pacific_time):
        pairs = [('9:22/8:22/(7:22)/6:22', 1822, time(19, 22)),
                 # Not sure if this is realistic ('9:22/8:22/(7:22)/6:22', 622, time(7, 22)),
                 ('(8:06)/7:06/6:06/5:06', 1706, time(20, 6)), ('(8:06)/7:06/6:06/5:06', 506, time(8, 6)),
                 ('9:00/(8:00)/7:00/6:00', 1800, time(20, 0)), ('9:00/(8:00)/7:00/6:00', 600, time(8, 0)),
                 ('(10:06)/9:06/8:06/7:06', 1906, time(22, 6)), ('(10:06)/9:06/8:06/7:06', 706, time(10, 6)),
                 ('12:34/(11:34)/10:34/9:34', 2134, time(23, 34)), ('12:34/(11:34)/10:34/9:34', 1134, time(11, 34)),
                 ('(12:56)/11:56/10:56/9:56', 956, time(12, 56))]

        # Set up Race
        race_id = RaceID(date(self.year, self.month, self.day), self.track, self.race_num)
        race = Race(race_id, self.db_handler)
        race_date = date(self.year, self.month, self.day)

        for time_str, pacific_time, correct_time in pairs:
            self.db_handler.query_db.return_value = time_str
            mock_pacific_time.return_value = pacific_time

            correct_datetime: datetime = datetime.combine(race_date, correct_time)
            self.assertEqual(self.race._generate_race_datetime(time_str), correct_datetime,
                             f'Night race time not converted correctly: {correct_datetime}')

    def test_sets_distance_change_attribute(self):
        self.fail('Finish the test--distance change')

if __name__ == '__main__':
    unittest.main()
