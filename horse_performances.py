import logging
import db_handler_persistent as dbh

import numpy as np
import pandas as pd
import datetime
import re
from progress.bar import Bar


class AddHorsePerformances:
    def __init__(self):
        self.db_consolidated_races = dbh.QueryDB(db='horses_consolidated_races', initialize_db=True)
        self.db_horses_data = dbh.QueryDB(db='horses_data')
        self.db_errata = dbh.QueryDB(db='horses_errata', initialize_db=True)
        self.db_handlers = [
            self.db_consolidated_races,
            self.db_horses_data,
            self.db_errata,
        ]

        self.consolidated_table = 'horses_consolidated_performances'
        self.consolidated_table_structure = {
            # Format 'sql_col_name': ('sql_datatype', 'horses_consolidated_performances_col', 'race_horse_info_col', 'horse_pps col')
            'source_file': ('VARCHAR(255)', 'source_file', 'source_file', 'source_file'),
            'track': ('VARCHAR(255)', 'track', 'track', 'track_code'),
            'date': ('DATE', 'date', 'date', 'race_date',),
            'race_num': ('TINYINT', 'race_num', 'race_num', 'race_num'),
            'distance': ('INT', 'distance', None, 'distance'),

            'horse_name': ('VARCHAR(255)', 'horse_name', 'horse_name', 'horse_name'),
            'horse_id': ('VARCHAR(255)', 'horse_id', 'horse_id', None),
            'post_position':('TINYINT', 'post_position', 'post_position', 'post_position'),
            'coupled_entry': ('VARCHAR(255)', 'coupled_entry', 'coupled_entry', None),
            'days_old': ('INT', 'days_old', None, None),
            'state_bred': ('VARCHAR(255)', 'state_bred', 'state_bred', None),

            'days_since_last_race': ('INT', 'days_since_last_race', None, 'days_since_last_race'),
            'favorite': ('INT', 'favorite', 'favorite', 'favorite'),

            'weight':('SMALLINT', 'weight', 'weight', 'weight'),


            'dead_heat_finish': ('TINYINT', 'dead_heat_finish', 'dead_heat_finish', None),

            'position_0': ('TINYINT', 'position_0', None, None),
            'position_330': ('TINYINT', 'position_330', None, None),
            'position_440': ('TINYINT', 'position_440', None, None),
            'position_660': ('TINYINT', 'position_660', None, None),
            'position_880': ('TINYINT', 'position_880', None, None),
            'position_990': ('TINYINT', 'position_990', None, None),
            'position_1100': ('TINYINT', 'position_1100', None, None),
            'position_1210': ('TINYINT', 'position_1210', None, None),
            'position_1320': ('TINYINT', 'position_1320', None, None),
            'position_1430': ('TINYINT', 'position_1430', None, None),
            'position_1540': ('TINYINT', 'position_1540', None, None),
            'position_1610': ('TINYINT', 'position_1610', None, None),
            'position_1650': ('TINYINT', 'position_1650', None, None),
            'position_1760': ('TINYINT', 'position_1760', None, None),
            'position_1830': ('TINYINT', 'position_1830', None, None),
            'position_1870': ('TINYINT', 'position_1870', None, None),
            'position_1980': ('TINYINT', 'position_1980', None, None),

            'lead_or_beaten_0': ('SMALLINT', 'lead_or_beaten_0', None, None),
            'lead_or_beaten_330': ('SMALLINT', 'lead_or_beaten_330', None, None),
            'lead_or_beaten_440': ('SMALLINT', 'lead_or_beaten_440', None, None),
            'lead_or_beaten_660': ('SMALLINT', 'lead_or_beaten_660', None, None),
            'lead_or_beaten_880': ('SMALLINT', 'lead_or_beaten_880', None, None),
            'lead_or_beaten_990': ('SMALLINT', 'lead_or_beaten_990', None, None),
            'lead_or_beaten_1100': ('SMALLINT', 'lead_or_beaten_1100', None, None),
            'lead_or_beaten_1210': ('SMALLINT', 'lead_or_beaten_1210', None, None),
            'lead_or_beaten_1320': ('SMALLINT', 'lead_or_beaten_1320', None, None),
            'lead_or_beaten_1430': ('SMALLINT', 'lead_or_beaten_1430', None, None),
            'lead_or_beaten_1540': ('SMALLINT', 'lead_or_beaten_1540', None, None),
            'lead_or_beaten_1610': ('SMALLINT', 'lead_or_beaten_1610', None, None),
            'lead_or_beaten_1650': ('SMALLINT', 'lead_or_beaten_1650', None, None),
            'lead_or_beaten_1760': ('SMALLINT', 'lead_or_beaten_1760', None, None),
            'lead_or_beaten_1830': ('SMALLINT', 'lead_or_beaten_1830', None, None),
            'lead_or_beaten_1870': ('SMALLINT', 'lead_or_beaten_1870', None, None),
            'lead_or_beaten_1980': ('SMALLINT', 'lead_or_beaten_1980', None, None),

            'meds_adjunct_bleeder': ('TINYINT', 'meds_adjunct_bleeder', 'adjunct_bleeder_meds', None),
            'meds_bute': ('TINYINT', 'meds_bute', 'bute', 'medication_bute'),
            'meds_lasix': ('TINYINT', 'meds_lasix', 'lasix', 'medication_lasix'),

            'equip_running_ws': ('TINYINT', 'equip_running_ws', 'equip_running_ws', None),
            'equip_screens': ('TINYINT', 'equip_screens', 'equip_screens', None),
            'equip_shields': ('TINYINT', 'equip_shields', 'equip_shields', None),
            'equip_aluminum_pads': ('TINYINT', 'equip_aluminum_pads', 'equip_aluminum_pads', None),
            'equip_blinkers': ('TINYINT', 'equip_blinkers','equip_blinkers', 'blinkers'),
            'equip_mud_calks': ('TINYINT', 'equip_mud_calks', 'equip_mud_calks', None),
            'equip_glued_shoes': ('TINYINT', 'equip_glued_shoes', 'equip_glued_shoes', None),
            'equip_inner_rims': ('TINYINT', 'equip_inner_rims', 'equip_inner_rims', None),
            'equip_front_bandages': ('TINYINT', 'equip_front_bandages', 'equip_front_bandages', 'front_wraps'),
            'equip_goggles': ('TINYINT', 'equip_goggles', 'equip_goggles', None),
            'equip_outer_rims': ('TINYINT', 'equip_outer_rims', 'equip_outer_rims', None),
            'equip_inserts': ('TINYINT', 'equip_inserts', 'equip_inserts', None),
            'equip_aluminum_pad': ('TINYINT', 'equip_aluminum_pad', 'equip_aluminum_pad', None),
            'equip_flipping_halter': ('TINYINT', 'equip_flipping_halter', 'equip_flipping_halter', None),
            'equip_bar_shoes': ('TINYINT', 'equip_bar_shoes', 'equip_bar_shoes', None),
            'equip_blocks': ('TINYINT', 'equip_blocks', 'equip_blocks', None),
            'equip_no_whip': ('TINYINT', 'equip_no_whip', 'equip_no_whip', None),
            'equip_blinkers_off': ('TINYINT', 'equip_blinkers_off', 'equip_blinkers_off', None),
            'equip_pads': ('TINYINT', 'equip_pads', 'equip_pads', None),
            'equip_nasal_strip_off': ('TINYINT', 'equip_nasal_strip_off', 'equip_nasal_strip_off', None),
            'equip_bar_shoe': ('TINYINT', 'equip_bar_shoe', 'equip_bar_shoe', 'bar_shoe'),
            'equip_nasal_strip': ('TINYINT', 'equip_nasal_strip', 'equip_nasal_strip', None),
            'equip_turndowns': ('TINYINT', 'equip_turndowns', 'equip_turndowns', None),
            'equip_spurs': ('TINYINT', 'equip_spurs', 'equip_spurs', None),
            'equip_cheek_piece': ('TINYINT', 'equip_cheek_piece', 'equip_cheek_piece', None),
            'equip_queens_plates': ('TINYINT', 'equip_queens_plates', 'equip_queens_plates', None),
            'equip_cheek_piece_off': ('TINYINT', 'equip_cheek_piece_off', 'equip_cheek_piece_off', None),
            'equip_no_shoes': ('TINYINT', 'equip_no_shoes', 'equip_no_shoes', None),
            'equip_tongue_tie': ('TINYINT', 'equip_tongue_tie', 'equip_tongue_tie', None),

            'jockey_id': ('VARCHAR(255)', 'jockey_id', 'jockey_id', None),
            'jockey': ('VARCHAR(255)', 'jockey', 'jockey', 'jockey'),
            'trainer_id': ('VARCHAR(255)', 'trainer_id', 'trainer_id', None),
            'trainer': ('VARCHAR(255)', 'trainer', 'trainer_name', 'trainer'),
}

        self.additional_fields = {
            'position_gate_call': [None, None, None, 'gate_call_position'],
            'position_start_call': [None, None, 'position_start_call', 'start_call_position'],
            'position_1st_call': [None, None, 'position_1st_call', '1st_call_position'],
            'position_2d_call': [None, None, 'position_2d_call', '2d_call_position'],
            'position_3d_call': [None, None, 'position_3d_call', None],
            'position_stretch_call': [None, None, 'position_stretch_call', 'stretch_call_position'],
            'position_finish': [None, None, 'position_finish_unofficial', 'finish_call_position'],

            'lead_or_beaten_lengths_start_call': [None, None, 'lead_or_beaten_lengths_start_call', 'start_call_lead_or_beaten_lengths'],
            'lead_or_beaten_lengths_1st_call': [None, None, 'lead_or_beaten_lengths_1st_call', '1st_call_lead_or_beaten_lengths'],
            'lead_or_beaten_lengths_2d_call': [None, None, 'lead_or_beaten_lengths_2d_call', '2d_call_lead_or_beaten_lengths'],
            'lead_or_beaten_lengths_3d_call': [None, None, 'lead_or_beaten_lengths_3d_call', None],
            'lead_or_beaten_lengths_stretch_call': [None, None, 'lead_or_beaten_lengths_stretch_call', 'stretch_call_lead_or_beaten_lengths'],
            'lead_or_beaten_lengths_finish': [None, None, 'lead_or_beaten_lengths_finish', 'finish_call_lead_or_beaten_lengths'],
        }

        self.distances_to_process = [1100, 1210, 1320, 1430, 1540, 1650, 1760, 1830, 1870, 1980]

        self.position_distance_mappings = {
            # Format: distance(int): {'consolidated_col_1': [None, None, 'race_horse_info_col', 'horse_pps_col'] ...}
            #       - Position out of the gate
            #       - Position at first call
            #       - Position at second call
            #       - Position at third call (if any)
            #       - Position at stretch call (1 furlong from finish)
            #       - Position at finish (unofficial--we don't care about disqualification for purposes of model training)
            1100: {
                'position_0': [None, None, 'position_start_call', 'position_start_call'],
                'position_330': [None, None, 'position_1st_call', 'position_1st_call'],
                'position_660': [None, None, 'position_2d_call', 'position_2d_call'],
                'position_880': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1100': [None, None, 'position_finish', 'position_finish'],
            },
            1210: {
                'position_0': [None, None, 'position_start_call', 'position_start_call'],
                'position_440': [None, None, 'position_1st_call', 'position_1st_call'],
                'position_660': [None, None, 'position_2d_call', 'position_2d_call'],
                'position_990': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1210': [None, None, 'position_finish', 'position_finish_call'],
            },
            1320: {
                'position_0': [None, None, 'position_start_call', 'position_start_call'],
                'position_440': [None, None, 'position_1st_call', 'position_1st_call'],
                'position_880': [None, None, 'position_2d_call', 'position_2d_call'],
                'position_1100': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1320': [None, None, 'position_finish', 'position_finish'],
            },
            1430: {
                'position_0': [None, None, 'position_start_call', 'position_start_call'],
                'position_440': [None, None, 'position_1st_call', 'position_1st_call'],
                'position_880': [None, None, 'position_2d_call', 'position_2d_call'],
                'position_1210': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1430': [None, None, 'position_finish', 'position_finish'],
            },
            1540: {
                'position_0': [None, None, 'position_start_call', 'position_start_call'],
                'position_440': [None, None, 'position_1st_call', 'position_1st_call'],
                'position_880': [None, None, 'position_2d_call', 'position_2d_call'],
                'position_1320': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1540': [None, None, 'position_finish', 'position_finish_call'],
            },
            1650: {
                'position_0': [None, None, 'position_start_call', 'position_start_call'],
                'position_440': [None, None, 'position_1st_call', 'position_1st_call'],
                'position_880': [None, None, 'position_2d_call', 'position_2d_call'],
                'position_1430': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1650': [None, None, 'position_finish', 'position_finish'],
            },
            1760: {
                'position_0': [None, None, 'position_start_call', 'position_gate_call'],
                'position_440': [None, None, 'position_1st_call', 'position_start_call'],
                'position_880': [None, None, 'position_2d_call', 'position_1st_call'],
                'position_1320': [None, None, 'position_3d_call', 'position_2d_call'],
                'position_1540': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1760': [None, None, 'position_finish', 'position_finish'],
            },
            1830: {
                'position_0': [None, None, 'position_start_call', 'position_gate_call'],
                'position_440': [None, None, 'position_1st_call', 'start_call'],
                'position_880': [None, None, 'position_2d_call', 'position_1st_call'],
                'position_1320': [None, None, 'position_3d_call', 'position_2d_call'],
                'position_1610': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1830': [None, None, 'position_finish', 'position_finish_call'],
            },
            1870: {
                'position_0': [None, None, 'position_start_call', 'position_gate_call'],
                'position_440': [None, None, 'position_1st_call', 'position_start_call'],
                'position_880': [None, None, 'position_2d_call', 'position_1st_call'],
                'position_1320': [None, None, 'position_3d_call', 'position_2d_call'],
                'position_1650': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1870': [None, None, 'position_finish', 'position_finish'],
            },
            1980: {
                'position_0': [None, None, 'position_start_call', 'position_gate_call'],
                'position_440': [None, None, 'position_1st_call', 'position_start_call'],
                'position_880': [None, None, 'position_2d_call', 'position_1st_call'],
                'position_1320': [None, None, 'position_3d_call', 'position_2d_call'],
                'position_1760': [None, None, 'position_stretch_call', 'position_stretch_call'],
                'position_1980': [None, None, 'position_finish_unofficial', 'position_finish'],
            },
        }
        self.lead_or_beaten_distance_mappings = {
            # Format: distance(int): {'consolidated_col_1': [None, None, 'race_horse_info_col', 'horse_pps_col'] ...}
            #       - Margin out of the gate
            #       - Margin at first call
            #       - Margin at second call
            #       - Margin at third call (if any)
            #       - Margin at stretch call (1 furlong from finish)
            #       - Margin at finish (unofficial--we don't care about disqualification for purposes of model training)
            1100: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_330': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_660': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1100': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1210: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_660': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_990': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1210': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1320: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1100': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1320': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1430: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1210': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1430': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1540: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1320': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1540': [None, None, 'lead_or_beaten_lengths_position_finish', 'lead_or_beaten_lengths_position_finish'],
            },
            1650: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1430': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1650': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1760: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', None],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_1320': [None, None, 'lead_or_beaten_lengths_3d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1540': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1760': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1830: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', None],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_1320': [None, None, 'lead_or_beaten_lengths_3d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1610': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1830': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1870: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', None],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_1320': [None, None, 'lead_or_beaten_lengths_3d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1650': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1870': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
            1980: {
                'lead_or_beaten_0': [None, None, 'lead_or_beaten_lengths_start_call', None],
                'lead_or_beaten_440': [None, None, 'lead_or_beaten_lengths_1st_call', 'lead_or_beaten_lengths_start_call'],
                'lead_or_beaten_880': [None, None, 'lead_or_beaten_lengths_2d_call', 'lead_or_beaten_lengths_1st_call'],
                'lead_or_beaten_1320': [None, None, 'lead_or_beaten_lengths_3d_call', 'lead_or_beaten_lengths_2d_call'],
                'lead_or_beaten_1760': [None, None, 'lead_or_beaten_lengths_stretch_call', 'lead_or_beaten_lengths_stretch_call'],
                'lead_or_beaten_1980': [None, None, 'lead_or_beaten_lengths_finish', 'lead_or_beaten_lengths_finish'],
            },
        }

        self.errata_table = 'aggregation_notes'
        # self.errata_table_structure = {
        #     'notes_on_data': ('TEXT',),
        #     'looks_like_bad_data': ('TINYINT',),
        # }
        # self.errata_table_structure.update(self.consolidated_table_structure)

        self.table_to_index_mappings = {
            'horses_consolidated_performances': 1,
            'race_horse_info' : 2,
            'horse_pps': 3,
        }
        self.table_to_db_mappings = {
            'race_horse_info': self.db_horses_data,
            'horse_pps': self.db_horses_data,
            'horses_consolidated_performances': self.db_consolidated_races,
            'horses_consolidated_races': self.db_consolidated_races,
            self.errata_table: self.db_errata,
        }
        self.column_mappings = {
            'track': (None, 'track', 'track', 'track_code',),
            'date': (None, 'date', 'date', 'race_date',),
            'race_num': (None, 'race_num', 'race_num', 'race_num',),
            'distance': (None, 'distance', 'distance', 'distance'),
        }

        # Processing variables
        self.tables_to_process = [
            'race_horse_info',
            'horse_pps',
        ]
        self.tables_to_attach = [
            'race_horse_info',
            'horse_pps',
            'horses_consolidated_performances',
            'horses_consolidated_races',
            # 'horses_errata',
        ]

        # State variables
        self.current_date = None
        self.current_track = None
        self.current_race_num = None
        self.current_horse = None

        self.df = {
            'race_horse_info': None,
            'horse_pps': None,
            'horses_consolidated_performances': None,

        }

        # Initialize tables
        unique = ['track', 'date', 'race_num', 'horse_name']

        consolidated_races_dtypes = {key: value[0] for key, value in self.consolidated_table_structure.items()}
        self.db_consolidated_races.initialize_table(self.consolidated_table, consolidated_races_dtypes,
                                                    unique_key=unique, foreign_key=None)

    def query_table(self, db_handler, table_name, fields, where='', other='', return_col_names=False):
        sql = f'SELECT {", ".join(fields)}'
        sql += f' FROM {table_name}'
        if where: sql += f' WHERE {where}'
        if other: sql += f' {other}'
        # print(sql)
        return db_handler.query_db(sql, return_col_names)

    def add_horse_race_entry(self, db_handler, table):
        db_handler.add_to_table(table,
                                [[self.current_track, self.current_date, self.current_race_num, self.current_horse]],
                                ['track', 'date', 'race_num', 'horse_name'])

    def where_for_current_race_and_horse(self, table_index=None, no_table_mapping=False):
        if no_table_mapping:
            return f'track = "{self.current_track}" ' \
                   f'AND date = "{self.current_date}" ' \
                   f'AND race_num = "{self.current_race_num}" ' \
                   f'AND horse_name = "{self.current_horse}"'

        else:
            return f'{self.column_mappings["track"][table_index]}="{self.current_track}" ' \
                   f'AND {self.column_mappings["date"][table_index]}="{self.current_date}" ' \
                   f'AND {self.column_mappings["race_num"][table_index]}="{self.current_race_num}" ' \
                   f'AND {self.column_mappings["horse_name"][table_index]}="{self.current_horse}"'

    def get_single_race_value(self, db_handler, table, field, no_table_mapping=False):
        table_index = self.table_to_index_mappings[table]
        sql = f'SELECT {field} from {table}' + self.where_for_current_race_and_horse(table_index=table_index,
                                                                                     no_table_mapping=no_table_mapping)
        print(sql)
        return db_handler.query_db(sql)[0][0]

    def set_current_info(self, source_df, i):
        date_col = source_df.columns.get_loc('date')
        track_col = source_df.columns.get_loc('track')
        race_num_col = source_df.columns.get_loc('race_num')
        horse_name_col = source_df.columns.get_loc('horse_name')

        self.current_date = source_df.iloc[i, date_col]
        self.current_track = source_df.iloc[i, track_col]
        self.current_race_num = source_df.iloc[i, race_num_col]
        self.current_horse = source_df.iloc[i, horse_name_col]

    def update_single_race_value(self, db_handler, table, field, value):
        sql = f'UPDATE {table} ' \
              f'SET {field}="{value}" ' \
              f'WHERE track="{self.current_track}" ' \
              f'AND date="{self.current_date}" ' \
              f'AND race_num="{self.current_race_num}" ' \
              f'AND horse_name="{self.current_horse}"'
        # print(sql)
        db_handler.update_db(sql)

    def update_race_values(self, db_handler, table, field_list, value_list, new_entry=False):
        sql = f'UPDATE {table} SET {self.concatenate_field_value_pairs(field_list, value_list)} ' \
              f'WHERE track="{self.current_track}" ' \
              f'AND date="{self.current_date}" ' \
              f'AND race_num="{self.current_race_num}" ' \
              f'AND horse_name="{self.current_horse}"'

        if new_entry: self.add_horse_race_entry(db_handler, table)
        # print(sql)
        db_handler.update_db(sql)

    def dict_values_match(self, dict_key, dict_1, dict_2):
        keys_to_ignore= ['source_file', 'race_conditions_text_1', 'race_conditions_text_2', 'race_conditions_text_3',
                         'race_conditions_text_4', 'race_conditions_text_5', 'race_conditions_text_6',]
        if dict_key in keys_to_ignore:
            return True
        elif dict_1[dict_key] == dict_2[dict_key]:
            return True
        else:
            return False

    def fix_race_type(self, db_handler, race_info_type, race_general_results_type, mismatch_category, track, date, race_num):
        fix_it_dict = {
            # Format: fix_name: race_general_results_type, race_info_type, equibase_race_type, replacement_value
            'SOC_fix': ['N', 'CO', 'SOC', 'SOC'],
            'WCL_fix': ['N', 'C', 'WCL', 'WCL'],
            'MDT_fix': ['S', 'N', 'MDT', 'MDT'],
            'STR_fix': ['R', 'N', 'STR', 'STR'],
            'HCP_fix': ['A', 'N', 'HCP', 'HCP'],
        }

        # Dict for items to ignore b/c they've already been fixed
        already_fixed_dict = {key: [value[2], value[1]] for key, value in fix_it_dict.items()}

        equibase_race_type = self.get_single_race_value(self.db_horses_data, 'race_general_results', 'race_type_equibase',
                                                   track, date,race_num)
        print(f'race_general_results data: {race_general_results_type}')
        print(f'race_info data: {race_info_type}')
        print(f'equibase_race_type: {equibase_race_type}')

        for fix in fix_it_dict:
            values = fix_it_dict[fix]
            if race_general_results_type == values[0] and race_info_type == values[1] and equibase_race_type == values[2]:
                self.update_single_race_value(db_handler, 'horses_consolidated_races', mismatch_category,
                                         values[3], track, date, race_num)
                self.add_blank_race_entry(self.db_errata, 'aggregation_notes', track, date, race_num)
                self. update_single_race_value(self.db_errata, 'aggregation_notes', mismatch_category,
                                         values[3], track, date, race_num)
                return 1

        for fixed in already_fixed_dict:
            values = already_fixed_dict[fixed]
            if race_general_results_type == values[0] and race_info_type == values[1]:
                print('No change needed--already processed')
                return 1

        return 0

    def prompt_for_user_correction_input(self, key, race):
        print('Unable to fix this issue.')
        user_input = input('(s)kip this mismatch category/mark as (b)ad/'
                           'add (n)ote/(e)nter new value/(q)uit/(C)ontinue: ').lower()
        if user_input == 'q':
            return user_input
        elif user_input == 's':
            return user_input
        elif user_input == 'b':
            self.add_blank_race_entry(self.db_errata, 'aggregation_notes', *race)
            self.update_single_race_value(self.db_errata,
                                     'aggregation_notes',
                                     'looks_like_bad_data',
                                     '1',
                                     *race)
        elif user_input == 'n':
            note = input('Enter note: ')
            self.add_blank_race_entry(self.db_errata, 'aggregation_notes', *race)
            old_note = self.get_single_race_value(self.db_errata,
                                             'aggregation_notes',
                                             'notes_on_data',
                                             *race,
                                             no_table_mapping=True)
            self.update_single_race_value(self.db_errata,
                                     'aggregation_notes',
                                     'notes_on_data',
                                     (str(old_note) + ' NEW NOTE: ' + note).strip(),
                                     *race)
        elif user_input == 'e':
            new_value = input('Enter new value: ')
            self.add_blank_race_entry(self.db_errata, 'aggregation_notes', *race)
            self.update_single_race_value(self.db_consolidated_races,
                                     'horses_consolidated_races',
                                     key,
                                     new_value,
                                     *race)
            self.update_single_race_value(self.db_errata, 'aggregation_notes', key, new_value, *race)

    def get_race_data(self, db_handler, table):
        if table == self.errata_table:
            source_fields = self.errata_table_structure.keys()
            consolidated_fields = self.errata_table_structure.keys()
        elif table == 'horses_consolidated_races':
            source_fields = ['date', 'track', 'race_num', 'distance']
            consolidated_fields = ['date', 'track', 'race_num', 'distance']
        else:
            table_index = self.table_to_index_mappings[table]
            field_dict = {key: value[table_index] for key, value in self.consolidated_table_structure.items()
                          if value[table_index]}
            additional_fields = {key: value[table_index] for key, value in self.additional_fields.items()
                                 if value[table_index]}
            field_dict.update(additional_fields)
            fields = [(key, value) for key, value in field_dict.items()]
            source_fields = [item for _, item in fields]
            consolidated_fields = [item for item, _ in fields]
        data = self.query_table(db_handler, table, source_fields)
        return pd.DataFrame(data, columns=consolidated_fields)

    def attach_dfs(self, tables_to_attach=None):
        tables_to_attach = tables_to_attach or self.tables_to_attach
        # Pull each table and put data into a df located at self.df[table]
        for table in tables_to_attach:
            print(f'Attaching {table}...')
            self.df[table] = self.get_race_data(self.table_to_db_mappings[table], table)
        self.df['horses_consolidated_races'] = self.get_race_data(self.db_consolidated_races,
                                                                  'horses_consolidated_races')

    def current_race_id(self, include_horse=False):
        race_id = str(self.current_date) + str(self.current_track) + str(self.current_race_num)
        if include_horse: race_id += str(self.current_horse).upper()
        return race_id

    def add_race_ids(self):
        for table in self.tables_to_attach:
            # Gather some processing variables
            df = self.df[table]

            # Zip up date, track, and race_num for races in the df being processed.
            # For horses_consolidated_data, don't include a horse name (because there isn't one in that table)
            race_id_data = zip(df['date'], df['track'], df['race_num'], df['horse_name']) if \
                table != 'horses_consolidated_races' else zip(df['date'], df['track'], df['race_num'])

            print(f'Adding race ids to {table}')
            self.current_race_id_data = race_id_data

            # Concatenate them, add them as a column to the df, and set that as the df's index
            if table == 'horses_consolidated_races':
                race_ids = [str(item[0]) + str(item[1]) + str(item[2]) for item in race_id_data]
            else:
                race_ids = [str(item[0]) + str(item[1]) + str(item[2]) + str(item[3]).upper() for item in race_id_data]
            df['race_id'] = race_ids
            df.set_index('race_id', inplace=True)

    def all_consolidated_fields_blank(self,  race_id, fields):
        data = self.df[self.consolidated_table].loc[race_id, fields]
        if all([item == None or (type(item) != str and not isinstance(item, datetime.date) and np.isnan(item)) for item in data]):
            return True
        else:
            return False

    def any_consolidated_fields_blank(self,  race_id, fields):
        data = self.df[self.consolidated_table].loc[race_id, fields]
        missing_data = [item == None or (type(item) != str and not isinstance(item, datetime.date) and np.isnan(item)) for item in data]
        if any(missing_data):
            return True
        else:
            return False

    def consolidated_field_blank(self, race_id, field):
        data = self.df['consolidated'].loc[race_id, field]
        if (type(data) != str and not isinstance(data, datetime.date) and np.isnan(data)) or data == None:
            return True
        else:
            return False

    def escape_and_clean(self, item):
        escaped_item = re.sub(r"(['\\])", r'\\\1', str(item))   # Escape textual backslashes and tick marks
        cleaned_item = re.sub(u"\uFFFD", "", escaped_item)      # Fix oddball <?> character
        return cleaned_item.strip()                             # Strip off any leading or trailing whitespace

    def concatenate_field_value_pairs(self, field_list, value_list):
        value_list = [self.escape_and_clean(item) for item in value_list]
        pairs = [f'{field} = \'{value}\'' for field, value in zip(field_list, value_list)]
        return ', '.join(pairs)

    def connect_dbs(self):
        for db in self.db_handlers:
            db.connect()

    def close_dbs(self):
        for db in self.db_handlers:
            db.close()

    def get_position_mapping(self, table, distance):
        table_index = self.table_to_index_mappings[table]
        map = {value[table_index]: key for key, value in self.position_distance_mappings[distance].items()}
        return map

    def get_margin_mapping(self, table, distance):
        table_index = self.table_to_index_mappings[table]
        map = {value[table_index]: key for key, value in self.lead_or_beaten_distance_mappings[distance].items()}
        return map

    def process_dfs(self, table=None):
        # Allow processing of a single table if passed as an argument
        tables = table or self.tables_to_process
        print(tables)

        # Iterate through the tables to process
        for source_table in tables:
            print(f'Processing {source_table}')
            df = self.df[source_table]
            bar = Bar('Processing existing data', max=len(df))
            consolidated_df = self.df[self.consolidated_table]
            for i in range(len(df)):
                bar.next()

                # Set state
                self.set_current_info(df, i)

                # Set distance state and continue if we don't have coverage for the distance
                try:
                    distance = self.df['horses_consolidated_races'].loc[self.current_race_id(), 'distance']
                except KeyError:
                    continue
                if distance not in self.distances_to_process: continue

                # Work out position/margin columns to drop after mapping
                table_index = self.table_to_index_mappings[source_table]
                additional_cols = [key for key in self.additional_fields if self.additional_fields[key][table_index] is not None]
                position_cols = [key for key in self.get_position_mapping(source_table, distance).keys()]
                margin_cols = [key for key in self.get_margin_mapping(source_table, distance).keys()]
                drop_columns = [col for col in additional_cols if col not in position_cols and col not in margin_cols]
                # print('Additional_cols:', additional_cols)
                # print('Position_cols:', position_cols)
                # print('Margin_cols:', margin_cols)
                # print('Drop cols:', drop_columns)

                # Get the race_id from the current row (which is the row index)
                race_id = df.iloc[i].name

                # Pull row data and set appropriate position/margin column names for distance
                row_data = df.iloc[i]
                    # Position column names
                row_data = row_data.rename(self.get_position_mapping(source_table, distance))
                    # Margin column names
                row_data = row_data.rename(self.get_margin_mapping(source_table, distance))

                    # Drop unused columns that conflict with consolidated table schema
                self.current_row_data = row_data
                row_data = row_data.drop(drop_columns)
                columns = row_data.index.tolist()
                self.current_columns = columns

                try:
                    consolidated_df.loc[race_id]    # Will fail if race_id isn't in consolidated df,
                                                    #  so triggers exception handling

                    # If race is in the consolidated db, check to make sure entries are not blank.
                    if self.all_consolidated_fields_blank(race_id, columns):
                        print(f'Race entry found in consolidated_df. Race id :{race_id}')
                        print(f'All fields found blank. Race id: {race_id}')
                        self.update_race_values(self.db_consolidated_races, self.consolidated_table,
                                                columns, row_data.tolist())


                    elif self.any_consolidated_fields_blank(race_id, columns):
                        print(f'Some fields blank ({race_id})')
                        consolidated_data = self.df[self.consolidated_table].loc[race_id, columns]
                        missing_consolidated_data = [item == None or (type(item) != str and not isinstance(item, datetime.date) and np.isnan(item)) for item in consolidated_data]
                        column_data = consolidated_df.loc[race_id, columns]
                        missing_column_data = [item == None or (type(item) != str and not isinstance(item, datetime.date) and np.isnan(item)) for item in column_data]

                        # Generate boolean list showing whether there is data missing in consolidated_data that isn't missing in column_data
                        fix_it_list = [item[0] == True and item[1] == False for item in zip(missing_consolidated_data, missing_column_data)]

                        if any(fix_it_list):
                            print(f'Mismatch: column_data: {column_data}')
                            for column in columns:
                                self.current_col_data = column_data
                                self.current_col = column
                                # If the consolidated table is missing data, try to fill it in
                                if column_data == None or (type(column_data) != str and not isinstance(column_data, datetime.date) and np.isnan(column_data)):
                                    source_data = row_data[column]
                                    self.current_source_data = source_data
                                    # Only replace the data if the source table has data to stick in there
                                    if source_data is not None and not (type(source_data) != str and not isinstance(source_data, datetime.date) and np.isnan(source_data)):
                                        print(f'Race entry found in consolidated_df. Race id :{race_id}')
                                        print(f'Updating {race_id} b/c column was empty.\n\tColumn: {column}\n\tOld Data: {column_data}. New data: {source_data}')
                                        self.update_single_race_value(self.db_consolidated_races, self.consolidated_table,
                                                                      column, source_data)
                except KeyError:
                    # print(f'i: {i}--Race not in consolidated races ({race_id})')

                    # Pull row data and set column names to match consolidated data column names
                    self.update_race_values(self.db_consolidated_races, self.consolidated_table,
                                            columns, row_data.tolist(), new_entry=True)
        bar.finish()

    def add_to_consolidated_table(self, table=None):
        table = table or None
        self.connect_dbs()
        print('Attaching dfs to AddRacesInfo instance ...')
        self.attach_dfs()
        self.add_race_ids()
        print('Processing source tables ...')
        self.process_dfs(table=table)
        self.close_dbs()
        print('Done')
