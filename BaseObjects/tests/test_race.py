import unittest
from unittest.mock import Mock, patch

from DBHandler.DBHandler import DBHandler

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race
from BaseObjects.HorseID import HorseID

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
        race = Race(self.race_id, self.db_handler)
        race_date = date(self.year, self.month, self.day)

        for time_str, pacific_time, correct_time in pairs:
            self.db_handler.query_db.return_value = time_str
            mock_pacific_time.return_value = pacific_time

            correct_datetime: datetime = datetime.combine(race_date, correct_time)
            self.assertEqual(race._generate_race_datetime(time_str), correct_datetime,
                             f'Night race time not converted correctly: {correct_datetime}')

    def test_sets_distance_change_attribute(self):
        race = Race(self.race_id, self.db_handler)
        plan_v_actual_sets = [(1560, 1560, 0), (1560, 1610, 50), (1560, 1320, -240)]

        for planned, actual, distance_change in plan_v_actual_sets:
            race.planned_distance = planned
            race.distance = actual

            race._set_distance_change()

            self.assertEqual(race.distance_change, distance_change, 'Race.distance_change not set correctly')

    def test_gets_horses_in_race(self):
        """Checks that horses from DB are pulled and placed into Race.horses_in_race. Doesn't check that all horses
        are accounted for. Doesn't check for no results.
        """
        races = [
            [("Emery's Visualizer", '11010448', 1), ('Gotta B Quick', '13011522', 99), ('Louie Move', '13008915', 4),
             ('Maslow', '12018527', 7), ('Nineties Nieto', '12018033', 99), ('O Sole Mio', '13001233', 99),
             ('Perfect Summer', '13020069', 6), ('Pure Bingo', '13003414', 8), ('Sands of Time', '13024400', 3),
             ('U S S Hawk', '12022887', 5)],
            [('Kenzie Carolina', '9000648', 4), ('Lasting Rose', '10009231', 99), ("Maggie's Special", '7044751', 5),
             ('Seventyprcentcocoa', '8035306', 3), ("Smokin' Grey", '9006008', 2), ('Whiskey Miner', '9006184', 1)],
            [('Blue Chip Prospect', '15003296', 1), ('Candymankando', '15005700', 6), ('Disruptor', '14004085', 99),
             ('Enasoit', '14009674', 99), ('Hidalgo', '13007539', 2), ('Majestic Dunhill', '15014431', 5),
             ('McErin', '15004611', 7),
             ("New York's Finest", '14001917', 8), ('Psychoanalyze', '15021630', 4),
             ('Snake Oil Charlie', '12025664', 10), ('Spirit Special', '14002244', 99), ('Versed', '13013186', 3),
             ('Vital', '15018113', 9)],
            [('Boxwood', '16014866', None), ('Comic Kitten', '16001537', 1), ('Fun Paddy', '16022433', 2),
             ('Hard Legacy', '16000160', 3), ('Irish Willow', '16020681', 4), ("Julia's Ready", '16006089', 5),
             ('Lancelots Lady', '16005088', None), ('No Mo Temper', '16011079', 7), ('Silent Surprise', '16000453', 8),
             ('Speedy Solution', '16001377', 9), ('Support', '16003308', 10), ("The Beauty's Tale", '16014057', 11),
             ('Unapologetic Me', '16005275', 12)]
        ]

        for race in races:
            self.db_handler.generate_query.return_value = 'This is a SQL query string'
            self.db_handler.query_db.return_value = race

            self.race._get_horses_in_race()

            for horse in race:
                horse_id = HorseID(horse[0], horse[1])
                post_position = horse[2]

                # Make sure horse is populating in Race.horses_in_race
                self.assertTrue(horse_id in self.race.horses_in_race, f'Not populating horses in race (Horse {horse_id})')

                # Make sure that each Horse's post position is populating or it is assigned to Race.horses_scratched
                # or it's assigned to Race.post_position_missing if we don't have any info for it.
                if horse[2] == 99:
                    self.assertTrue(horse_id in self.race.horses_scratched,
                                    f'Scratched horse ({horse_id}) not put into Race.horses_scratched')
                elif horse[2] is None:
                    self.assertTrue(horse_id in self.race.post_position_missing,
                                    f'Horse ({horse_id}) with missing post position not assigned to post position 0')
                else:
                    if post_position not in self.race.post_positions:
                        self.fail(f'No post position in Race.post_positions--should have been populated for {horse_id}')
                    self.assertTrue(self.race.post_positions[post_position] == horse_id,
                                    f'Horse ({horse_id}) not assigned correct post position.')

    def test_gets_time_splits(self):
        self.fail('Write test to get time splits from db')

if __name__ == '__main__':
    unittest.main()
