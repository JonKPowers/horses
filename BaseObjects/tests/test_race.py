import unittest

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race

from datetime import date

class TestSpinUp(unittest.TestCase):
    def setUp(self) -> None:
        self.race_id = RaceID(date(2019,1 ,1), 'HOU', 5)

        self.race = Race(self.race_id)

    def test_init_sets_attributes(self):
        self.assertTrue(self.race._id == self.race_id)

    def test_gets_race_horses(self):
        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()
