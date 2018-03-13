race_general_results_table = {
    'table_name': 'race_general_results',
    'extension' : '1',

    'db_fields': {
        'track': 'track_code',
        'date': 'date',
        'race_num': 'race_num',
        'race_name': 'race_name',
        'off_time': 'off_time',
        'day_evening_flag': 'day_evening_flag',
        'country': 'country_code',

        'field_size': 'field_size',

        'purse': 'purse',
        'race_value': 'total_race_value',
        'max_claim': 'max_claim_price',
        'WPS_pool': 'WPS_show_pool',

        'breed': 'breed_of_race',
        'race_grade': 'race_grade',
        'race_class': 'abbrev_race_class',
        'race_type_BRIS': 'BRIS_race_type',
        'race_type_equibase': 'equibase_race_type',
        'race_restrictions': 'race_restrict_code',

        'conditions_slug': 'full_condition_slug',
        'conditions_slug_left_to_parse': 'left_to_parse',
        'optional_claiming_price': 'optional_claiming_price',

        'condition_1_claim_start_required_price': 'claim_start_req_price',
        'condition_1_claim_start_required_time': 'claim_start_req_time_limit',
        'condition_1_claim_start_required_months': 'claim_start_req_time_limit_months',
        'condition_1_number_limit': 'number_limit',
        'condition_1_money_limit': 'money_limit',
        'condition_1_time_limit': 'time_limit',
        'condition_1_time_limit_months': 'time_limit_months',
        'condition_1_excluded_races': 'excluded_races',
        'condition_1_unrecognized_races': 'unrecognized_races',
        'condition_1_excluded_claiming': 'CLAIMING',
        'condition_1_excluded_maiden': 'MAIDEN',
        'condition_1_excluded_optional': 'OPTIONAL',
        'condition_1_excluded_restricted': 'RESTRICTED',
        'condition_1_excluded_restricted_allowance': 'RESTRICTED ALLOWANCE',
        'condition_1_excluded_starter': 'STARTER',
        'condition_1_excluded_state_sired': 'STATE SIRED',
        'condition_1_excluded_state_sired_stakes': 'STATE SIRED STAKES',
        'condition_1_excluded_statebred': 'STATEBRED',
        'condition_1_excluded_statebred_allowance': 'STATEBRED ALLOWANCE',
        'condition_1_excluded_statebred_stakes': 'STATEBRED STAKES',
        'condition_1_excluded_trial': 'TRIAL',
        'condition_1_excluded_waiver': 'WAIVER',
        'condition_1_excluded_waiver_claiming': 'WAIVER CLAIMING',

        'condition_2_claim_start_required_price': 'excepted_1_claim_start_req_price',
        'condition_2_claim_start_required_time': 'excepted_1_claim_start_req_time_limit',
        'condition_2_claim_start_required_months': 'excepted_1_claim_start_req_time_limit_months',
        'condition_2_number_limit': 'excepted_1_number_limit',
        'condition_2_money_limit': 'excepted_1_money_limit',
        'condition_2_time_limit': 'excepted_1_time_limit',
        'condition_2_time_limit_months': 'excepted_1_time_limit_months',
        'condition_2_excluded_races': 'excepted_1_excluded_races',
        'condition_2_unrecognized_races': 'excepted_1_unrecognized_races',
        'condition_2_excluded_claiming': 'excepted_1_CLAIMING',
        'condition_2_excluded_maiden': 'excepted_1_MAIDEN',
        'condition_2_excluded_optional': 'excepted_1_OPTIONAL',
        'condition_2_excluded_restricted': 'excepted_1_RESTRICTED',
        'condition_2_excluded_restricted_allowance': 'excepted_1_RESTRICTED ALLOWANCE',
        'condition_2_excluded_starter': 'excepted_1_STARTER',
        'condition_2_excluded_state_sired': 'excepted_1_STATE SIRED',
        'condition_2_excluded_state_sired_stakes': 'excepted_1_STATE SIRED STAKES',
        'condition_2_excluded_statebred': 'excepted_1_STATEBRED',
        'condition_2_excluded_statebred_allowance': 'excepted_1_STATEBRED ALLOWANCE',
        'condition_2_excluded_statebred_stakes': 'excepted_1_STATEBRED STAKES',
        'condition_2_excluded_trial': 'excepted_1_TRIAL',
        'condition_2_excluded_waiver': 'excepted_1_WAIVER',
        'condition_2_excluded_waiver_claiming': 'excepted_1_WAIVER CLAIMING',

        'condition_3_claim_start_required_price': 'excepted_2_claim_start_req_price',
        'condition_3_claim_start_required_time': 'excepted_2_claim_start_req_time_limit',
        'condition_3_claim_start_required_months': 'excepted_2_claim_start_req_time_limit_months',
        'condition_3_number_limit': 'excepted_2_number_limit',
        'condition_3_money_limit': 'excepted_2_money_limit',
        'condition_3_time_limit': 'excepted_2_time_limit',
        'condition_3_time_limit_months': 'excepted_2_time_limit_months',
        'condition_3_excluded_races': 'excepted_2_excluded_races',
        'condition_3_unrecognized_races': 'excepted_2_unrecognized_races',
        'condition_3_excluded_claiming': 'excepted_2_CLAIMING',
        'condition_3_excluded_maiden': 'excepted_2_MAIDEN',
        'condition_3_excluded_optional': 'excepted_2_OPTIONAL',
        'condition_3_excluded_restricted': 'excepted_2_RESTRICTED',
        'condition_3_excluded_restricted_allowance': 'excepted_2_RESTRICTED ALLOWANCE',
        'condition_3_excluded_starter': 'excepted_2_STARTER',
        'condition_3_excluded_state_sired': 'excepted_2_STATE SIRED',
        'condition_3_excluded_state_sired_stakes': 'excepted_2_STATE SIRED STAKES',
        'condition_3_excluded_statebred': 'excepted_2_STATEBRED',
        'condition_3_excluded_statebred_allowance': 'excepted_2_STATEBRED ALLOWANCE',
        'condition_3_excluded_statebred_stakes': 'excepted_2_STATEBRED STAKES',
        'condition_3_excluded_trial': 'excepted_2_TRIAL',
        'condition_3_excluded_waiver': 'excepted_2_WAIVER',
        'condition_3_excluded_waiver_claiming': 'excepted_2_WAIVER CLAIMING',

        'race_conditions_1': 'race_conditions_1',
        'race_conditions_2': 'race_conditions_2',
        'race_conditions_3': 'race_conditions_3',
        'race_conditions_4': 'race_conditions_4',
        'race_conditions_5': 'race_conditions_5',

        'age_sex_restrictions': 'age_sex_restrictions',
        'allowed_age_two': 'allowed_age_two',
        'allowed_age_three': 'allowed_age_three',
        'allowed_age_four': 'allowed_age_four',
        'allowed_age_five': 'allowed_age_five',
        'allowed_age_older': 'allowed_age_older',
        'allowed_fillies': 'allowed_fillies',
        'allowed_mares': 'allowed_mares',
        'allowed_colts_geldings': 'allowed_colts_geldings',

        'statebred_race': 'state_bred_flag',

        'distance': 'distance',
        'distance_units': 'distance_units',
        'about_distance': 'about_dist_flag',
        'run_up_dist': 'run_up_dist',
        'temp_rail_dist': 'temp_rail_dist',
        'track_condition': 'track_condition',
        'weather': 'weather',
        'race_temp': 'race_temp',

        'off_turf': 'off_turf_flag',
        'off_turf_distance_change': 'off_turf_dist_change',

        'surface_old': 'surface_old_style',
        'surface_new': 'surface_new_style',
        'all_weather': 'all_weather_flag',

        'chute_start': 'chute_start_flag',

        'time_fraction_1': 'fraction_1_time',
        'time_fraction_2': 'fraction_2_time',
        'time_fraction_3': 'fraction_3_time',
        'time_fraction_4': 'fraction_4_time',
        'time_fraction_5': 'fraction_5_time',
        'time_final': 'final_time',

        'distance_fraction_1': 'fraction_1_dist',
        'distance_fraction_2': 'fraction_2_dist',
        'distance_fraction_3': 'fraction_3_dist',
        'distance_fraction_4': 'fraction_4_dist',
        'distance_fraction_5': 'fraction_5_dist',

        'distance_start_call': 'start_call_dist',
        'distance_first_call': 'call_dist_first',
        'distance_second_call': 'call_dist_second',
        'distance_third_call': 'call_dist_third',

        'start_description': 'start_description',
    },

    'unique_key': [
        'track',
        'date',
        'race_num',
    ],

    'foreign_key':  [],

    'not_null': [],
}

race_notes_table = {
    'table_name': 'race_notes',
    'extension' : '6',

    'db_fields' : {
        'track': 'track_code',
        'date': 'date',
        'race_num': 'race_num',
        'day_evening_flag': 'day_evening_flag',

        'note_seq': 'footnote_sequence',
        'note': 'footnote_text',
    },

    'unique_key': [
        'track',
        'date',
        'race_num',
        'note_seq',
    ],

    'foreign_key':  [],

    'not_null': [],
}

race_horse_info_table = {
    'table_name': 'race_horse_info',
    'extension' : '2',

    'db_fields': {
        'track': 'track_code',
        'date': 'date',
        'race_num': 'race_num',
        'day_evening_flag': 'day_evening_flag',

        'horse_name': 'horse_name',
        'horse_id': 'horse_reg_id',
        'program_number': 'program_number',
        'post_position': 'post_position',
        'coupled_entry': 'coupled_flag',
        'nonbetting': 'nonbetting_flag',

        'birth_year': 'birth_year',
        'foreign_bred': 'foreign_bred_code',

        'state_bred': 'state_bred_code',
        'race_breed': 'breed',

        'earnings': 'earnings',

        'claimed': 'claimed_flag',
        'claimed_price': 'claiming_price',
        'claimed_owner': 'claimed_owner',
        'claimed_owner_id': 'claimed_owner_id',
        'claimed_owner_first': 'claimed_owner_first',
        'claimed_owner_middle': 'claimed_owner_middle',
        'claimed_owner_last': 'claimed_owner_last',
        'claimed_trainer': 'claimed_trainer',
        'claimed_trainer_id': 'claimed_trainer_id',
        'claimed_trainer_first': 'claimed_trainer_first',
        'claimed_trainer_middle': 'claimed_trainer_middle',
        'claimed_trainer_last': 'claimed_trainer_last',

        'odds': 'odds',
        'favorite': 'favorite_flag',
        'payout_win': 'win_payout',
        'payout_place': 'place_payout',
        'payout_show': 'show_payout',

        'disqualified': 'disqualified_flag',
        'disqualified_placing': 'disqualified_placing',

        'weight': 'weight',
        'weight_corrected': 'corrected_weight',
        'weight_overweight_amt': 'overweight_amt',

        'medication': 'medication_codes',
        'adjunct_bleeder_meds': 'meds_adjunct_bleeder',
        'bute': 'meds_bute',
        'lasix': 'meds_lasix',

        'equipment': 'equipment_code',
        'equip_running_ws': 'running_ws',
        'equip_screens': 'screens',
        'equip_shields': 'shields',
        'equip_aluminum_pads': 'aluminum_pads',
        'equip_blinkers': 'blinkers',
        'equip_mud_calks': 'mud_calks',
        'equip_glued_shoes': 'glued_shoes',
        'equip_inner_rims': 'inner_rims',
        'equip_front_bandages': 'front_bandages',
        'equip_goggles': 'goggles',
        'equip_outer_rims': 'outer_rims',
        'equip_inserts': 'inserts',
        'equip_aluminum_pad': 'aluminum_pad',
        'equip_flipping_halter': 'flipping_halter',
        'equip_bar_shoes': 'bar_shoes',
        'equip_blocks': 'blocks',
        'equip_no_whip': 'no_whip',
        'equip_blinkers_off': 'blinkers_off',
        'equip_pads': 'pads',
        'equip_nasal_strip_off': 'nasal_strip_off',
        'equip_bar_shoe': 'bar_shoe',
        'equip_nasal_strip': 'nasal_strip',
        'equip_turndowns': 'turndowns',
        'equip_spurs': 'spurs',
        'equip_cheek_piece': 'cheek_piece',
        'equip_queens_plates': 'queens_plates',
        'equip_cheek_piece_off': 'cheek_piece_off',
        'equip_no_shoes': 'no_shoes',
        'equip_tongue_tie': 'tongue_tie',

        'jockey_id': 'jockey_id',
        'jockey': 'jockey_name',
        'jockey_first': 'jockey_first_name',
        'jockey_middle': 'jockey_middle_name',
        'jockey_last': 'jockey_last_name',

        'trainer_id': 'trainer_id',
        'trainer_name': 'trainer_name',
        'trainer_first': 'trainer_first_name',
        'trainer_middle': 'trainer_middle_name',
        'trainer_last': 'trainer_last_name',

        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'owner_first': 'owner_first_name',
        'owner_middle': 'owner_middle_name',
        
        'trip_comment': 'trip_comment',

        'position_start_call': 'start_call_pos',
        'position_1st_call': '1st_call_pos',
        'position_2d_call': '2d_call_pos',
        'position_3d_call': '3d_call_pos',
        'position_stretch_call': 'stretch_call_pos',
        'position_finish_unofficial': 'finish_pos',
        'position_finish_official': 'official_finish_pos',
        'dead_heat_finish': 'dead_heat_flag',

        'lead_or_beaten_lengths_start_call': 'lead_or_beaten_lengths_start',
        'lead_or_beaten_lengths_1st_call': 'lead_or_beaten_lengths_1st_call',
        'lead_or_beaten_lengths_2d_call': 'lead_or_beaten_lengths_2d_call',
        'lead_or_beaten_lengths_3d_call': 'lead_or_beaten_lengths_3d_call',
        'lead_or_beaten_lengths_stretch_call': 'lead_or_beaten_lengths_stretch_call',
        'lead_or_beaten_lengths_finish': 'lead_or_beaten_lengths_finish',

        'margin_start_call': 'start_margin',
        'margin_1st_call': '1st_call_margin',
        'margin_2d_call': '3d_call_margin',
        'margin_3d_call': '2d_call_margin',
        'margin_stretch_call': 'stretch_call_margin',
        'margin_finish_call': 'finish_margin'

    },

    'unique_key': [
        'track',
        'date',
        'race_num',
        'horse_name',
    ],

    'foreign_key':  [],

    'not_null': [],
}

horse_breeding_info_table = {
    'table_name': 'horse_breeding',
    'extension': '5',

    'db_fields': {
        'track': 'track_code',
        'date': 'date',
        'race_num': 'race_num',

        'horse_name': 'horse_name',
        'foreign_bred': 'foreignbred_code',
        'state_bred': 'statebred_code',

        'breeder': 'breeder',
        'color': 'color',
        'foal_date': 'foal_date',
        'age': 'age',
        'sex': 'sex',
        'sire': 'sire',
        'dam': 'dam',
        'broodmare_sire': 'broodmare_sire',

    },

    'unique_key': [
        'track',
        'date',
        'race_num',
        'horse_name',
    ],

    'foreign_key':  [],

    'not_null': [],
}

race_payoffs_itm_table = {
    'table_name': 'race_payoffs_itm',
    'extension' : '3',

    'db_fields' : {
        'track': 'track_code',
        'date': 'date',
        'race_num': 'race_num',
        'day_evening_flag': 'day_evening_flag',

        'horse_name': 'horse_name',
        'program_num': 'program_number',
        'foreign_bred': 'foreign_bred_code',
        'state_bred': 'statebred_code',

        'payout_win': 'win_payout',
        'payout_place': 'place_payout',
        'payout_show': 'show_payout',

    },

    'unique_key': [
        'track',
        'date',
        'race_num',
        'horse_name',
    ],

    'foreign_key':  [],

    'not_null': [],
}

race_payoffs_exotic_table = {
    'table_name': 'race_payoffs_exotic',
    'extension': '4',

    'db_fields': {
        'track': 'track_code',
        'date': 'date',
        'race_num': 'race_num',
        'day_evening_flag': 'day_evening_flag',

        'wager_type': 'wager_type',
        'bet_amt': 'bet_amount',
        'payout_amt': 'payout_amount',

        'number_correct': 'number_correct',
        'winning_nums': 'winning_numbers',

        'wager_pool': 'wager_pool',
        'carryover': 'carryover_amount',
    },

    'unique_key': [
        'track',
        'date',
        'race_num',
        'wager_type',
    ],

    'foreign_key':  [],

    'not_null': [],
}