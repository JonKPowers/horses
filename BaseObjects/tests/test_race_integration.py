import unittest

from BaseObjects.RaceID import RaceID
from BaseObjects.Race import Race
from DBHandler.DBHandler import DBHandler

from datetime import date

class TestRaceIntegration(unittest.TestCase):
    def test_spins_up_and_initializes(self):
        db = DBHandler('horses_test')
        race_date = date(2017, 5, 6)
        race_id = RaceID(race_date, 'CD', 12)

        sut = Race(race_id, db)

        self.fail('Why is the 2017 KY Derby showing up as a race not found?')

if __name__ == '__main__':
    unittest.main()
