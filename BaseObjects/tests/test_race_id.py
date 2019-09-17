import unittest
from BaseObjects.RaceID import RaceID


from datetime import date

class TestRaceID(unittest.TestCase):
    def setUp(self):
        self.races = [(date(2016, 6, 19), 'AP', 6), (date(2016, 8, 4), 'AP', 8),
                 (date(2016, 8, 28), 'AP', 7), (date(2016, 10, 14), 'HAW', 9),
                 (date(2016, 11, 11), 'HAW', 3), (date(2016, 11, 26), 'HAW', 5),
                 (date(2016, 12, 22), 'HAW', 2), (date(2016, 12, 29), 'HAW', 1),
                 (date(2017, 3, 17), 'HAW', 4), (date(2018, 4, 13), 'HAW', 4),
                 (date(2018, 4, 28), 'HAW', 1), (date(2018, 5, 18), 'AP', 1),
                 (date(2018, 6, 8), 'AP', 1), (date(2018, 6, 29), 'AP', 2),
                 (date(2018, 7, 20), 'AP', 2), (date(2018, 8, 10), 'AP', 7),
                 (date(2018, 9, 6), 'AP', 1), (date(2018, 9, 21), 'AP', 4),
                 (date(2018, 10, 20), 'HAW', 8)]

    def test_race_id_equal(self):
        test_race = RaceID(date(2016, 6, 19), 'CD', 5)
        same_race = RaceID(date(2016, 6, 19), 'CD', 5)

        self.assertEqual(test_race, same_race)

    def test_race_id_not_equal(self):
        test_race = RaceID(date(2019, 1, 1), 'AP', 1)
        different_race = RaceID(date(2019, 1, 1), 'AP', 2)

        self.assertNotEqual(test_race, different_race)

    def test_race_id_as_dict_key(self):
        race_dict = dict()

        test_race = RaceID(date(2014, 2, 24), 'HOU', 3)
        test_race2 = RaceID(date(2015, 9, 25), 'HOU', 4)
        race_dict[test_race] = 'Some race data'
        race_dict[test_race2] = 'Some other race data'

        self.assertTrue(test_race in race_dict)
        self.assertTrue(test_race2 in race_dict)
        self.assertIsNotNone(race_dict[test_race])
        self.assertIsNotNone(race_dict[test_race2])


