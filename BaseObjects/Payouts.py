from typing import Dict
from DBHandler.DBHandler import DBHandler

from constants.db_info import payouts_db, payouts_wps_table

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



