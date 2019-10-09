from typing import Dict, List
from DBHandler.DBHandler import DBHandler

from constants.db_info import payouts_db, payouts_wps_table, payouts_exotics_table

from BaseObjects.Race import RaceID
from BaseObjects.HorseID import HorseID


class Payouts:
    def __init__(self, race_id: RaceID, db_handler: DBHandler):
        self.race_id: RaceID = race_id
        self.db = db_handler

        # dict to map from program number to a HorseID to be used for payout lookup
        self.program_num_to_horse_id: Dict[int, HorseID] = dict()

        # W/P/S payout lists:
        self.win_payouts: Dict[HorseID, float] = dict()
        self.place_payouts: Dict[HorseID, float] = dict()
        self.show_payouts: Dict[HorseID, float] = dict()

        # Exotic bet info
        self.exotics_allowed: List[str] = list()

        # Exotic bet naming map
        self.exotic_names: Dict[str, str] = {
            'Exacta': 'exacta',
            'Exactor': 'exacta',
            'Trifecta': 'trifecta',
            'Trifector': 'trifecta',
            'Superfecta': 'superfecta',
            'Daily Double': 'daily_double',
            'Pick Three': 'pick_three',
            'Pick Four': 'pick_four',
            'Pick Five': 'pick_five',
            'Pick Six': 'pick_six',
            'Pick Seven': 'pick_seven',
            'Pick Nine': 'pick_nine',
            'Quinella': 'quinella',
            'Super High Five': 'super_high_five',
        }

    def _get_payout_info(self):
        self.db.set_db(payouts_db)
        sql = self.db.generate_query(payouts_wps_table, ['horse_name', 'program_num', 'payout_win',
                                                         'payout_place', 'payout_show'],
                                     where=self.race_id.generate_sql_where())
        itm_horses = self.db.query_db(sql)

        for horse in itm_horses:
            horse_id = HorseID(horse[0])
            self.program_num_to_horse_id[int(horse[1])] = horse_id
            self.win_payouts[horse_id] = horse[2] if horse[2] is not None else 0
            self.place_payouts[horse_id] = horse[3] if horse[3] is not None else 0
            self.show_payouts[horse_id] = horse[4] if horse[4] is not None else 0

    def _get_exotic_payout_info(self):
        self.db.set_db(payouts_db)
        sql = self.db.generate_query(payouts_exotics_table, ['wager_type', 'bet_amt', 'payout_amt', 'number_correct',
                                                             'winning_nums'])
        exotic_payouts = self.db.query_db(sql)

        for payout_info in exotic_payouts:
            if payout_info[0] is not None:
                self.exotics_allowed.append(payout_info[0])
                setattr(self, self.exotic_names[payout_info[0]], self._generate_exotic_dict(payout_info))
            else:  # Handling for unspecified exotics
                assert(False, 'Finish the method')

    def _generate_exotic_dict(self, payout_info: List):
        exotic_dict: dict = dict()
        exotic_dict['wager_type'] = payout_info[0]
        exotic_dict['bet_amt']: float = payout_info[1]
        exotic_dict['payout_amt']: float = payout_info[2]
        exotic_dict['number_correct']: int = int(payout_info[3])
        exotic_dict['consolation_winners'] = '-' in payout_info[4] and '/' in payout_info[4]
        exotic_dict['winning_nums']: list = self._get_winning_nums(payout_info[4])
        return exotic_dict

    def _get_winning_nums(self, num_string: str) -> List:
        # Case 1 (most common): numbers are separated only by hyphens
        if '-' in num_string and '/' not in num_string:
            return [int(item) for item in num_string.split('-')]
        # Case 2: numbers are separated only by forward slashes:
        elif '/' in num_string and '-' not in num_string:
            return [int(item) for item in num_string.split('/')]
        # Case 3: numbers are separated by both hyphens and forward slashes:
        elif '-' in num_string and '/' in num_string:
            race_winners = num_string.split('-')
            return [[int(item) for item in place.split('/')] for place in race_winners]
        # The rest: need to figure it out
        else:
            assert(False, 'Finish the method')



