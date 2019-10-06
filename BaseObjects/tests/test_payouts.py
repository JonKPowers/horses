import unittest
from unittest import TestCase
from unittest.mock import Mock

from datetime import date

from BaseObjects.Race import RaceID
from BaseObjects.HorseID import HorseID
from BaseObjects.Payouts import Payouts

class TestPayouts(TestCase):
    def setUp(self) -> None:
        self.db = Mock()

    def test_sets_itm_payoffs_and_program_numbers_basic(self):
        payouts = [('Bella Fabiela', '4', None, None, 2.1), ('Kendini', '2', None, 3.2, 2.1),
                   ('Latitudefortytwo', '5', 3.4, 2.4, 2.1)]
        self.db.generate_query.return_value = 'This is a SQL query string'
        self.db.query_db.return_value = payouts

        winner: HorseID = HorseID('Latitudefortytwo')
        placer: HorseID = HorseID('Kendini')
        shower: HorseID = HorseID('Bella Fabiela')

        race_id: RaceID = RaceID(date(2018, 1, 1), 'CD', 2)
        sut: Payouts = Payouts(race_id, self.db)

        # Run the method under test
        sut._get_payout_info()

        # Check the output state: W/P/S dicts should have entries for each horse
        self.assertTrue(sut.win_payouts[winner] == 3.4)
        self.assertTrue(sut.win_payouts[shower] == 0)
        self.assertTrue(sut.win_payouts[placer] == 0)
        self.assertTrue(sut.place_payouts[winner] == 2.4)
        self.assertTrue(sut.place_payouts[placer] == 3.2)
        self.assertTrue(sut.place_payouts[shower] == 0)
        self.assertTrue(sut.show_payouts[winner] == 2.1)
        self.assertTrue(sut.show_payouts[placer] == 2.1)
        self.assertTrue(sut.show_payouts[shower] == 2.1)
        # Check the output state: program_num dict should have entries mapping program numbers to HorseIDs
        self.assertTrue(sut.program_num_to_horse_id[2] == placer)
        self.assertTrue(sut.program_num_to_horse_id[4] == shower)
        self.assertTrue(sut.program_num_to_horse_id[5] == winner)

    def sets_exotic_bets_allowed(self):
        self.fail('Write the test')




if __name__ == '__main__':
    unittest.main()
