horses_info_table = {
    'table_name': 'horses_info',
    'extension': 'DRF',

    'db_fields': {
        'horse_name': 'horse_name',
        'birth_year': 'birth_year',
        'foaling_month': 'foaling_month',
        'sex': 'sex',
        'color': 'color',
        'sire': 'sire',
        'sires_sire': 'sires_sire',
        'dam': 'dam',
        'dams_sire': 'dams_sire',
        'breeder': 'breeder',
        'where_bred': 'where_bred',
    },

    'unique_key': [
        'horse_name',
        'birth_year',
        'foaling_month',
    ],

    'foreign_key': [],

    'not_null': [],
}

trainers_info_table = {
    'table_name': 'trainers_info',
    'extension': 'DRF',

    'db_fields': {
        'trainer_name': 'trainer',
    },

    'unique_key': [
        'trainer_name',
    ],

    'foreign_key': [],

    'not_null': [],

}

jockey_info_table = {
    'table_name': 'jockey_info',
    'extension': 'DRF',

    'db_fields': {
        'jockey_name': 'jockey',
    },

    'unique_key': [
        'jockey_name',
    ],

    'foreign_key': [],

    'not_null': [],
}

owner_info_table = {
    'table_name': 'owner_info',
    'extension': 'DRF',

    'db_fields': {
        'owner_name': 'todays_owner',
    },

    'unique_key': {
        'owner_name',
    },

    'foreign_key': [],

    'not_null': [],
}

workouts_table = {
    'table_name': 'workouts',
    'extension': 'DRF',

    'db_fields': {
        'horse_name': 'horse_name',
        'birth_year': 'birth_year',
        'foaling_month': 'foaling_month',
        'date': 'workout_date_{}',
        'track': 'workout_track_{}',
        'distance': 'workout_distance_{}',
        'time': 'workout_time_{}',
        'bullet': 'workout_time_{}_bullet',
        'run_description': 'workout_description_{}',
        'track_type': 'workout_track_type_{}',
        'track_condition': 'workout_condition_{}',
        'rank_of_same_works': 'rank_same_workout_{}',
        'number_of_same_works': 'same_workouts_all_day_{}',
    },

    'unique_key': [
        'horse_name',
        'date',
        'track',
    ],

    'foreign_key': [
        ('horse_name', 'horses_info(horse_name)'),
    ],

    'not_null': [
        'workout_date_{}',
        'workout_track_{}',
    ],
}

race_info_table = {
    'table_name': 'race_info',
    'extension': 'DRF',

    'db_fields': {
        'track': 'track',
        'date': 'date',
        'post_times_regions': 'post_times_by_region',
        'post_time_pacific': 'post_time_pacific_military',
        'race_num': 'race',
        'distance': 'distance',
        'about_distance_flag': 'past_distance_{}_about_flag',
        'off_turf_dist_change': 'past_{}_off_turf_dist_change',
        'surface': 'surface',
        'all_weather_surface': 'allweather_surface',
        'rail_distance': 'cond_rail_distance',
        'breed': 'breed_type',

        'race_description': 'race_conditions',
        'race_description_equibase': 'equibase_race_conditions',
        'race_classification': 'today_race_class',
        'cond_race_class': 'cond_race_class',
        'race_type': 'race_type',
        'statebred_race': 'statebread_flag',
        'age_sex_restrictions': 'age_sex_restricts',
        'allowed_age_two': 'allowed_age_two',
        'allowed_age_three': 'allowed_age_three',
        'allowed_age_four': 'allowed_age_four',
        'allowed_age_five': 'allowed_age_five',
        'allowed_age_older': 'allowed_age_older',
        'allowed_fillies': 'allowed_fillies',
        'allowed_mares': 'allowed_mares',
        'allowed_colts_geldings': 'allowed_colts_geldings',
        
        'purse': 'purse',
        'claiming_price': 'claiming_price',
        'claiming_price_lowest': 'low_claiming_price',

        'standard_weight': 'standard_weight',
        'three_year_old_weight': 'three_yo_weight',
        'weight_allowance_0_amt': 'weight_allowance_0_amt',
        'weight_allowance_0_condition': 'weight_allowance_0_condition',
        'weight_allowance_1_amt': 'weight_allowance_1_amt',
        'weight_allowance_1_condition': 'weight_allowance_1_condition',
        'weight_allowance_2_amt': 'weight_allowance_2_amt',
        'weight_allowance_2_condition': 'weight_allowance_2_condition',
        'weight_allowance_3_amt': 'weight_allowance_3_amt',
        'weight_allowance_3_condition': 'weight_allowance_3_condition',

        'track_record': 'track_record_pace',
        'BRIS_speed_par': 'bris_speed_par',
        'BRIS_par_pace_2f': '2f_bris_pace_par',
        'BRIS_par_pace_4f': '4f_bris_pace_par',
        'BRIS_par_pace_6f': '6f_bris_pace_par',
        'BRIS_par_pace_late': 'bris_late_pace_par',

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




        'race_cond_1': 'race_conditions_1',
        'race_cond_2': 'race_conditions_2',
        'race_cond_3': 'race_conditions_3',
        'race_cond_4': 'race_conditions_4',
        'race_cond_5': 'race_conditions_5',
        'race_cond_6': 'race_conditions_6',

        # 'cond_left_on_string': 'cond_left_on_string',

        'wager_types_1': 'wager_type_1',
        'wager_types_2': 'wager_type_2',
        'wager_types_3': 'wager_type_3',
        'wager_types_4': 'wager_type_4',
        'wager_types_5': 'wager_type_5',
        'wager_types_6': 'wager_type_6',
        'wager_types_7': 'wager_type_7',
        'wager_types_8': 'wager_type_8',
        'wager_types_9': 'wager_type_9',

        'simulcast_track': 'simulcast_track_code',
        'simulcast_race': 'simulcast_track_race',
    },

    'unique_key': [
        'track',
        'date',
        'race_num',
    ],

    'foreign_key': [],

    'not_null': [],
}

horses_race_table = {
    'table_name': 'horses_race',
    'extension': 'DRF',

    'db_fields': {
        'track': 'track',
        'date': 'date',
        'race_num': 'race',
        'horse_name': 'horse_name',
        'program_num': 'program_number',
        'coupled_entry': 'entry',

        'morning_line': 'morning_line',
        'post_position': 'post_position',
        'program_post_position': 'program_post_pos',

        'weight': 'weight',
        'weight_allowance': 'apprentice_wgt_alw',

        'MTO_AE_entry': 'main_track_only_AE',
        'claimed_price': 'horse_claiming_price',

        'nasal_strip_change': 'today_nasal_strip_chg',
        'equipment_change': 'equipment_change',
        'medications_new_style': 'todays_meds_new',
        'medications_old_style': 'todays_meds_old',

        'BRIS_run_style': 'bris_run_style',
        'BRIS_prime_power': 'bris_prime_power',
        'quirin_speed_points': 'quirin_speed_points',

        'days_since_last_race': 'days_since_last_race',
    },

    'unique_key': [
        'track',
        'date',
        'race_num',
        'horse_name',
    ],

    'foreign_key': [
        ('horse_name', 'horses_info(horse_name)'),
    ],

    'not_null': [],
}

horses_pp_table = {
    'table_name': 'horse_pps',
    'extension': 'DRF',

    'db_fields': {
        'horse_name': 'horse_name',

        'race_date': 'past_race_date_{}',

        'track_code': 'past_track_code_{}',
        'track_code_BRIS': 'past_BRIS_track_code_{}',
        'race_num': 'past_race_number_{}',
        'race_name': 'past_race_name_{}',

        'race_class': 'past_race_class_{}',
        'race_type': 'past_race_type_{}',
        'equibase_race_conditions': 'past_equibase_race_conditions_{}',

        'age_sex_restrictions': 'past_age_sex_restrictions_{}',
        'allowed_age_two': 'past_allowed_age_two_{}',
        'allowed_age_three': 'past_allowed_age_three_{}',
        'allowed_age_four': 'past_allowed_age_four_{}',
        'allowed_age_five': 'past_allowed_age_five_{}',
        'allowed_age_older': 'past_allowed_age_older_{}',
        'allowed_fillies': 'past_allowed_fillies_{}',
        'allowed_mares': 'past_allowed_mares_{}',
        'allowed_colts_geldings': 'past_allowed_colts_geldings_{}',

        'statebred_race': 'past_statebred_flag_{}',
        'restricted_qualified_claimer': 'past_restricted_or_qualified_{}',
        'race_purse': 'past_purse_{}',

        'track_condition': 'past_track_cond_{}',
        'distance': 'past_distance_{}',
        'surface': 'past_surface_{}',
        'sealed_track': 'past_sealed_track_indicator_{}',
        'all_weather_track': 'past_all_weather_flag_{}',

        'trainer': 'past_trainer_{}',
        'jockey': 'past_jockey_{}',

        'special_chute': 'past_special_chute_{}',
        'nasal_strip': 'past_{}_nasal_strip',
        'blinkers': 'past_equipment_{}',
        'medication': 'past_medication_{}',
        'medication_lasix': 'past_medication_{}_lasix',
        'medication_bute': 'past_medication_{}_bute',
        'front_wraps': 'past_front_wraps_{}',
        'bar_shoe': 'past_bar_shoe_{}',
        'start_code': 'past_start_code_{}',

        'weight': 'past_weight_{}',
        'weight_allowance': 'past_weight_allowance_{}',
        'days_since_last_race': 'past_days_since_last_{}',

        'num_of_horses': 'past_entrants_{}',
        'post_position': 'past_post_{}',
        'odds': 'past_odds_{}',
        'favorite': 'past_favorite_flag_{}',
        'claimed_flag': 'past_claimed_code_{}',
        'claimed_price': 'past_claim_price_{}',
        'lowest_claim_price': 'past_low_claiming_price_{}',
        'highest_claim_price': 'past_high_claiming_price_{}',

        'trip_comment': 'past_trip_comment_{}',
        'trip_comment_extra': 'past_extra_comment_{}',
        'extended_start_comment': 'past_extended_start_comment_{}',
        'BRIS_par': 'past_bris_par_for_class_{}',
        'BRIS_speed_rating': 'past_bris_speed_rating_{}',
        'speed_rating': 'past_speed_rating_{}',

        'final_time': 'past_final_time_{}',
        'track_variant': 'past_track_variant_{}',
        'company_line': 'past_company_line_{}',

        '2f_fraction': 'past_fraction_2f_{}',
        '3f_fraction': 'past_fraction_3f_{}',
        '4f_fraction': 'past_fraction_4f_{}',
        '5f_fraction': 'past_fraction_5f_{}',
        '6f_fraction': 'past_fraction_6f_{}',
        '7f_fraction': 'past_fraction_7f_{}',
        '8f_fraction': 'past_fraction_8f_{}',
        '10f_fraction': 'past_fraction_10f_{}',
        '12f_fraction': 'past_fraction_12f_{}',
        '14f_fraction': 'past_fraction_14f_{}',
        '16f_fraction': 'past_fraction_16f_{}',

        '1st_call_fraction': 'past_fraction_first_{}',
        '2d_call_fraction': 'past_fraction_second_{}',
        '3d_call_fraction': 'past_fraction_third_{}',

        'win_horse': 'past_win_{}',
        'win_weight': 'past_win_weight_{}',
        'win_margin': 'past_win_margin_{}',

        'place_horse': 'past_place_{}',
        'place_weight': 'past_place_weight_{}',
        'place_margin': 'past_place_margin_{}',

        'show_horse': 'past_show_{}',
        'show_weight': 'past_show_weight_{}',
        'show_margin': 'past_show_margin_{}',

        'start_call_position': 'past_call_pos_start_{}',
        '1st_call_position': 'past_call_pos_first_{}',
        '2d_call_position': 'past_call_pos_second_{}',
        'gate_call_position': 'past_call_pos_gate_{}',
        'stretch_call_position': 'past_call_pos_stretch_{}',
        'finish_call_position': 'past_call_pos_finish_{}',

        'start_call_lead_or_beaten_lengths': 'past_lead_or_beaten_lengths_start_{}',
        '1st_call_lead_or_beaten_lengths': 'past_lead_or_beaten_lengths_first_call_{}',
        '2d_call_lead_or_beaten_lengths': 'past_lead_or_beaten_lengths_second_call_{}',
        'stretch_call_lead_or_beaten_lengths': 'past_lead_or_beaten_lengths_stretch_call_{}',
        'finish_call_lead_or_beaten_lengths': 'past_lead_or_beaten_lengths_finish_{}',

        'money_position': 'past_money_pos_{}',

        'BRIS_race_shape_1st_call': 'past_bris_shape_first_call_{}',
        'BRIS_race_shape_2d_call': 'past_bris_shape_second_call_{}',

        'BRIS_pace_2f': 'past_bris_pace_2f_{}',
        'BRIS_pace_4f': 'past_bris_pace_4f_{}',
        'BRIS_pace_6f': 'past_bris_pace_6f_{}',
        'BRIS_pace_8f': 'past_bris_pace_8f_{}',
        'BRIS_pace_10f': 'past_bris_pace_10f_{}',
        'BRIS_pace_late': 'past_bris_pace_late_{}',
    },

    'unique_key': [
        'horse_name',
        'race_date',
        'track_code',
        'race_num',
    ],

    'foreign_key': [
        ('horse_name', 'horses_info(horse_name)'),
    ],

    'not_null': [
        'past_race_date_{}',
        'past_track_code_{}',
    ],
}

horses_stats_table = {
    'table_name': 'horses_stats',
    'extension': 'DRF',

    'db_fields': {
        'date': 'date',
        'horse_name': 'horse_name',

        'weight': 'weight',
        'weight_allowance': 'apprentice_wgt_alw',

        'sire_stud_fee': 'sire_stud_fee_current',

        'days_since_last_race': 'days_since_last_race',

        'BRIS_run_style': 'bris_run_style',
        'BRIS_prime_power': 'bris_prime_power',
        'quirin_speed_points': 'quirin_speed_points',

        'best_BRIS_speed_lifetime': 'best_bris_speed_life',
        'best_BRIS_speed_track': 'best_bris_speed_todays_track',
        'best_BRIS_speed_current_year': 'best_bris_speed_recent_year',
        'best_BRIS_speed_prior_year': 'best_bris_speed_2d_recent_year',

        'best_BRIS_speed_all_weather': 'best_bris_speed_alw',
        'best_BRIS_speed_fast': 'best_bris_speed_fast',
        'best_BRIS_speed_on_turf': 'best_bris_speed_turf',
        'best_BRIS_speed_off_track': 'best_bris_speed_off_track',
        'best_BRIS_speed_at_distance': 'best_bris_speed_at_distance',


        'record_current_year_year': 'current_year_year',
        'record_current_year_starts': 'current_year_starts',
        'record_current_year_wins': 'current_year_wins',
        'record_current_year_places': 'current_year_places',
        'record_current_year_shows': 'current_year_shows',
        'record_current_year_earned': 'current_year_earned',

        'record_prior_year_year': 'past_year_year',
        'record_prior_year_starts': 'past_year_starts',
        'record_prior_year_wins': 'past_year_wins',
        'record_prior_year_places': 'past_year_places',
        'record_prior_year_shows': 'past_year_shows',
        'record_prior_year_earnings': 'past_year_earned',

        'record_life_starts': 'lifetime_starts',
        'record_life_wins': 'lifetime_wins',
        'record_life_places': 'lifetime_places',
        'record_life_shows': 'lifetime_shows',
        'record_life_earnings': 'lifetime_earned',

        'life_at_dist_starts': 'life_distance_starts',
        'life_at_dist_wins': 'life_distance_wins',
        'life_at_dist_places': 'life_distance_places',
        'life_at_dist_shows': 'life_distance_shows',
        'life_at_dist_earnings': 'life_distance_earned',

        'life_at_track_starts': 'life_track_starts',
        'life_at_track_wins': 'life_track_wins',
        'life_at_track_places': 'life_track_places',
        'life_at_track_shows': 'life_track_shows',
        'life_at_track_earnings': 'life_track_earned',

        'life_on_fast_dirt_starts': 'fast_dirt_starts',
        'life_on_fast_dirt_wins': 'fast_dirt_wins',
        'life_on_fast_dirt_places': 'fast_dirt_places',
        'life_on_fast_dirt_shows': 'fast_dirt_shows',
        'life_on_fast_dirt_earnings': 'fast_dirt_shows',

        'life_on_turf_starts': 'life_turf_starts',
        'life_on_turf_wins': 'life_turf_wins',
        'life_on_turf_places': 'life_turf_places',
        'life_on_turf_shows': 'life_turf_shows',
        'life_on_turf_earnings': 'life_turf_earned',

        'life_on_all_weather_starts': 'life_starts_alw',
        'life_on_all_weather_wins': 'life_wins_alw',
        'life_on_all_weather_places': 'life_places_alw',
        'life_on_all_weather_shows': 'life_shows_alw',
        'life_on_all_weather_earnings': 'life_earnings_alw',

        'life_on_wet_starts': 'life_wet_starts',
        'life_on_wet_wins': 'life_wet_wins',
        'life_on_wet_places': 'life_wet_places',
        'life_on_wet_shows': 'life_wet_shows',
        'life_on_wet_earnings': 'life_wet_earned',
    },

    'unique_key': [
        'date',
        'horse_name',
    ],

    'foreign_key': [
        ('horse_name', 'horses_info(horse_name)')
    ],

    'not_null': [],
}

switches_table = {
    'table_name': 'switches',
    'extension': 'DRF',

    'db_fields': {
        'date': 'date',
        'horse_name': 'horse_name',

        'claim_trainer_switch_date': 'past_claim_trainer_switch_date_{}',
        'claim_trainer_switch_info_1': 'past_claim_trainer_switch_1_{}',
        'claim_trainer_switch_info_2': 'past_claim_trainer_switch_2_{}',
        'claim_trainer_switch_info_3': 'past_claim_trainer_switch_3_{}',
        'claim_trainer_switch_info_4': 'past_claim_trainer_switch_4_{}',
        'claim_trainer_switch_info_5': 'past_claim_trainer_switch_5_{}',

    },

    'unique_key': [],

    'foreign_key': [
        ('horse_name', 'horses_info(horse_name)'),
    ],

    'not_null': [],
}

trainer_stats_table = {
    'table_name': 'trainer_stats',
    'extension': 'DRF',

    'db_fields': {
        'date': 'date',
        'trainer': 'trainer',
        'current_meet_starts': 'trainer_starts',
        'current_meet_wins': 'trainer_wins',
        'current_meet_places': 'trainer_places',
        'current_meet_shows': 'trainer_shows',

        'current_year_starts': 'trainer_current_year_starts',
        'current_year_wins': 'trainer_current_year_wins',
        'current_year_places': 'trainer_current_year_places',
        'current_year_shows': 'trainer_current_year_shows',
        'current_year_roi': 'trainer_current_year_roi',

        'prior_year_starts': 'trainer_past_year_starts',
        'prior_year_wins': 'trainer_past_year_wins',
        'prior_year_places': 'trainer_past_year_places',
        'prior_year_shows': 'trainer_past_year_shows',
        'prior_year_roi': 'trainer_past_year_roi',

    },

    'unique_key': [
        'date',
        'trainer',
    ],

    'foreign_key': [],

    'not_null': [],
}

jockey_stats_table = {
    'table_name': 'jockey_stats',
    'extension': 'DRF',

    'db_fields': {
        'date': 'date',
        'jockey': 'jockey',
        'current_meet_starts': 'jockey_starts',
        'current_meet_wins': 'jockey_wins',
        'current_meet_places': 'jockey_places',
        'current_meet_shows': 'jockey_shows',

        'current_year_starts': 'jockey_current_year_starts',
        'current_year_wins': 'jockey_current_year_wins',
        'current_year_places': 'jockey_current_year_places',
        'current_year_shows': 'jockey_current_year_shows',
        'current_year_roi': 'jockey_current_year_roi',

        'prior_year_starts': 'jockey_past_year_starts',
        'prior_year_wins': 'jockey_past_year_wins',
        'prior_year_places': 'jockey_past_year_places',
        'prior_year_shows': 'jockey_past_year_shows',
        'prior_year_roi': 'jockey_past_year_roi',

        'jockey_at_distance_on_turf_label': 'jockey_at_distance_on_turf_label',
        'jockey_at_distance_on_turf_starts': 'jockey_at_distance_on_turf_starts',
        'jockey_at_distance_on_turf_wins': 'jockey_at_distance_on_turf_wins',
        'jockey_at_distance_on_turf_places': 'jockey_at_distance_on_turf_places',
        'jockey_at_distance_on_turf_shows': 'jockey_at_distance_on_turf_shows',
        'jockey_at_distance_on_turf_roi': 'jockey_at_distance_on_turf_roi',
        'jockey_at_distance_on_turf_earnings': 'jockey_at_distance_on_turf_earnings',


    },

    'unique_key': [
        'date',
        'jockey',
    ],

    'foreign_key': [],

    'not_null': [],
}

tj_combo_stats_table = {
    'table_name': 'tj_combo_stats',
    'extension': 'DRF',

    'db_fields': {
        'date': 'date',
        'trainer': 'trainer',
        'jockey': 'jockey',

        'current_meet_starts': 'TJ_combo_starts',
        'current_meet_wins': 'TJ_combo_wins',
        'current_meet_places': 'TJ_combo_places',
        'current_meet_shows': 'TJ_combo_shows',
        'current_meet_roi': 'TJ_combo_roi',


        'past_year_starts': 'TJ_starts',
        'past_year_wins': 'TJ_wins',
        'past_year_places': 'TJ_places',
        'past_year_shows': 'TJ_shows',
        'past_year_roi': 'TJ_roi',
    },

    'unique_key': [
        'date',
        'trainer',
        'jockey',
    ],

    'foreign_key': [],

    'not_null': [],
}

owner_stats_table = {
    'table_name': 'owner_stats',
    'extension': 'DRF',

    'db_fields': {
        'date': 'date',
        'owner': 'todays_owner',
        'silks': 'owners_silks',
    },

    'unique_key': [
        'owner',
        'silks'
    ],

    'foreign_key': [],

    'not_null': [],
}