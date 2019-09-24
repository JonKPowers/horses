import unittest

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race

from datetime import date

class TestSpinUp(unittest.TestCase):
    def setUp(self) -> None:
        self.race_id = RaceID(date(2019, 1, 1), 'HOU', 5)

        self.race = Race(self.race_id)

    def test_sets_race_info_from_RaceID(self):
        self.assertTrue(self.race.track == 'HOU')
        self.assertTrue(self.race.race_num == 5)
        self.assertEqual(date(2019, 1, 1), self.race.race_date)

    def test_sets_race_time(self):
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()
