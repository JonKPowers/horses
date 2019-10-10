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

    def test_sets_exotic_bets_allowed_basic(self):
        # Set up initial state for system under test
        payouts = [(None, 0.2, 399.54, '0', '10-2-3-7-9'), ('Daily Double', 2.0, 13.0, '0', '7-10'),
                   ('Exacta', 2.0, 25.8, '0', '10-2'), ('Pick Four', 2.0, 300.0, '4', '7-9-7-10'),
                   ('Pick Nine', 1.0, 997.5, '9', '2-1-4-6-5-7-9-7-10'),
                   ('Pick Six', 2.0, 2855.4, '6', '6-5-7-9-7-10'), ('Pick Three', 2.0, 74.0, '3', '9-7-10'),
                   ('Superfecta', 1.0, 421.8, '0', '10-2-3-7'), ('Trifecta', 2.0, 135.2, '0', '10-2-3')]
        exotics = ['Daily Double', 'Exacta', 'Pick Nine', 'Pick Six', 'Pick Three', 'Superfecta', 'Trifecta']
        self.db.generate_query.return_value = 'This is a SQL query'
        self.db.query_db.return_value = payouts

        race_id: RaceID = RaceID(date(2011, 1, 1), 'CD', 5)
        sut: Payouts = Payouts(race_id, self.db)

        # Run the SUT
        sut._get_exotic_payout_info()

        # Check the output state: each type of exotic wager should be in Payouts.exotics_allowed
        # except that the None entry isn't to be added without additional processing
        for exotic in exotics:
            self.assertTrue(exotic in sut.exotics_allowed,
                            f'Exotic wager type not added to Payouts.exotics_allowed: {exotic}')
        self.assertTrue(None not in sut.exotics_allowed)

    def test_sets_exotic_bet_dicts(self):
        # Set up initial state for system under test
        payouts = [('Daily Double', 2.0, 13.0, '0', '7-10'),
                   ('Exacta', 2.0, 25.8, '0', '10-2'),
                   ('Pick Four', 2.0, 300.0, '4', '7-9/8-7-10'),
                   ('Superfecta', 1.0, 421.8, '0', '10-2-3-7'),
                   ('Trifecta', 2.0, 135.2, '0', '10-2-3')
                   ]
        self.db.generate_query.return_value = 'This is a SQL query string'
        self.db.query_db.return_value = payouts

        race_id: RaceID = RaceID(date(2011, 1, 1), 'CD', 5)
        sut: Payouts = Payouts(race_id, self.db)

        # Run the SUT
        sut._get_exotic_payout_info()

        # Check the output state:
        # Daily Double
        self.assertTrue(sut.daily_double['wager_type'] == 'Daily Double')
        self.assertTrue(sut.daily_double['bet_amt'] == 2.0)
        self.assertTrue(sut.daily_double['payout_amt'] == 13.0)
        self.assertTrue(sut.daily_double['number_correct'] == 0)
        self.assertTrue(sut.daily_double['consolation_winners'] is False)
        self.assertTrue(sut.daily_double['winning_nums'] == [7, 10])

        self.assertTrue(sut.exacta['wager_type'] == 'Exacta')
        self.assertTrue(sut.exacta['bet_amt'] == 2.0)
        self.assertTrue(sut.exacta['payout_amt'] == 25.8)
        self.assertTrue(sut.exacta['number_correct'] == 0)
        self.assertTrue(sut.exacta['consolation_winners'] is False)
        self.assertTrue(sut.exacta['winning_nums'] == [10, 2])

        self.assertTrue(sut.pick_four['wager_type'] == 'Pick Four')
        self.assertTrue(sut.pick_four['bet_amt'] == 2.0)
        self.assertTrue(sut.pick_four['payout_amt'] == 300)
        self.assertTrue(sut.pick_four['number_correct'] == 4)
        self.assertTrue(sut.pick_four['consolation_winners'] is True)
        self.assertTrue(sut.pick_four['winning_nums'] == [[7], [9, 8], [7], [10]])

        self.assertTrue(sut.superfecta['wager_type'] == 'Superfecta')
        self.assertTrue(sut.superfecta['bet_amt'] == 1.0)
        self.assertTrue(sut.superfecta['payout_amt'] == 421.8)
        self.assertTrue(sut.superfecta['number_correct'] == 0)
        self.assertTrue(sut.superfecta['consolation_winners'] is False)
        self.assertTrue(sut.superfecta['winning_nums'] == [10, 2, 3, 7])

        self.assertTrue(sut.trifecta['wager_type'] == 'Trifecta')
        self.assertTrue(sut.trifecta['bet_amt'] == 2.0)
        self.assertTrue(sut.trifecta['payout_amt'] == 135.2)
        self.assertTrue(sut.trifecta['number_correct'] == 0)
        self.assertTrue(sut.trifecta['consolation_winners'] is False)
        self.assertTrue(sut.trifecta['winning_nums'] == [10, 2, 3])

    def test_gets_winning_numbers_from_string_with_consolations(self):
        test_cases = [('5/7-4/5-2/3-9', [[5, 7], [4, 5], [2, 3], [9]]),
                      ('6-5/7-4/5-2/3-9', [[6], [5, 7], [4, 5], [2, 3], [9]]),
                      ('9-1-1/2/8-5/9-11-12/14', [[9], [1], [1, 2, 8], [5, 9], [11], [12, 14]]),
                      ('1/2/8-5/9-11-12/14', [[1, 2, 8], [5, 9], [11], [12, 14]]),
                      ('1-1/2/8-5/9-11-12/14', [[1], [1, 2, 8], [5, 9], [11], [12, 14]]),
                      ('9-1-1/2/8-5/9-11-12/14', [[9], [1], [1, 2, 8], [5, 9], [11], [12, 14]]),
                      ('7-3/6-7-3-2/10', [[7], [3, 6], [7], [3], [2, 10]]),
                      ('7-3-2/10-2/6/9', [[7], [3], [2, 10], [2, 6, 9]]),
                      ('7-3/11/13/14-3/10/13/14-10', [[7], [3, 11, 13, 14], [3, 10, 13, 14], [10]]),
                      ('5-7-3/5-7', [[5], [7], [3, 5], [7]]),
                      ('3-5-7-3/5-7', [[3], [5], [7], [3, 5], [7]]),
                      ('1-5/7-4', [[1], [5, 7], [4]]),
                      ('1-1-5/7-4', [[1], [1], [5, 7], [4]]),
                      ('6-1-1/2', [[6], [1], [1, 2]]),
                      ]

        race_id: RaceID = RaceID(date(2011, 1, 1), 'CD', 5)
        sut: Payouts = Payouts(race_id, self.db)

        for winner_string, expected_output in test_cases:
            self.assertEqual(sut._get_winning_nums(winner_string), expected_output)

    def test_exotic_naming_dict_has_all_names(self):
        wagers = ['Trifecta', 'Exacta', 'Superfecta', 'Daily Double', 'Pick Three', 'Pick Four', 'Quinella',
                  'Pick Five', 'Super High Five', 'Exactor', 'Triactor', 'Consolation Double', 'Consolation Pick Three',
                  'Pick 6 Jackpot', 'Z-5 Super Hi-5', 'Pick Six', 'Perfecta', 'X-5 Super High Five',
                  'Grand Slam', 'Place Pick All', 'Tri Super', 'Win Four', 'Pick Seven', 'Pick 9 Jackpot',
                  'Pick 7 Jackpot', '123 racing', 'Twin Trifecta', 'Pick Nine', 'Classix', 'Jockey Challenge',
                  'Head To Head', 'Pick Ten', 'Future Wager',
                  ]

        race_id: RaceID = RaceID(date(2011, 1, 1), 'CD', 5)
        sut: Payouts = Payouts(race_id, self.db)

        for wager in wagers:
            try:
                sut.exotic_names[wager]
            except KeyError:
                self.fail(f'{wager} not found in Payouts.exotic_names')

if __name__ == '__main__':
    unittest.main()
