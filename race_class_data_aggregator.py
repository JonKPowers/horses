class HorseRace:
    def __init__(self):
        self.attribute_structure = {
                                       'track': {
                                           'race_general_results': 'track',
                                           'race_info': 'track',
                                           'horse_pps': 'track_code'  # I assume track_code always == track_code_BRIS
                                       },

                                       'date': {
                                           'race_general_results': 'date',
                                           'race_info': 'date',
                                           'horse_pps': 'race_date',
                                       },

                                       'race_num': {
                                           'race_general_results': 'race_num',
                                           'race_info': 'race_num',
                                           'horse_pps': 'race_num',
                                       },

                                       'time_local': {
                                           # *******TO DO **************
                                       },

                                       'temperature': {
                                           'horses_general_results': 'race_temp',
                                       },
                                       'weather': {
                                           'horses_general_results': 'weather',
                                       },

                                       'distance': {
                                           'horses_general_results': 'distance',
                                           'race_info': None,
                                           'horse_pps': None,
                                       },

                                       'run_up_distance': {
                                           'horses_general_results': 'run_up_dist',

                                       },

                                       'temp_rail_distance': {
                                           'horses_general_results': 'temp_rail_dist',

                                       },

                                       'about_distance_flag': {
                                           'horses_general_results': 'about_distance',
                                       },

                                       'surface': {
                                           'horses_general_results': 'surface_new',
                                       },

                                       'track_condition': {
                                           'horses_general_results': 'track_condition',
                                       },

                                       'chute_start': {
                                           'horses_general_results': 'chute_start',
                                       },

                                       'off_turf': {
                                           'horses_general_results': 'off_turf',
                                       },

                                       'off_turf_dist_change': {
                                           'horses_general_results': 'off_turf_distance_change',
                                       },

                                       'num_of_horses': {
                                           'horses_general_results': 'field_size',
                                       },

                                       'breed': {
                                           'horses_general_results': None,

                                       },
                                       'ages_allowed': {
                                           'two': {
                                               'horses_general_results': 'allowed_age_two',
                                               'race_info': 'allowed_age_two',
                                               'horse_pps': 'allowed_age_two',
                                           },
                                           'three': {
                                               'horses_general_results': 'allowed_age_three',
                                               'race_info': 'allowed_age_three',
                                               'horse_pps': 'allowed_age_three',
                                           },
                                           'four': {
                                               'horses_general_results': 'allowed_age_four',
                                               'race_info': 'allowed_age_four',
                                               'horse_pps': 'allowed_age_four',
                                           },
                                           'five': {
                                               'horses_general_results': 'allowed_age_five',
                                               'race_info': 'allowed_age_five',
                                               'horse_pps': 'allowed_age_five',
                                           },
                                           'older': {
                                               'horses_general_results': 'allowed_age_older',
                                               'race_info': 'allowed_age_older',
                                               'horse_pps': 'allowed_age_older',
                                           },
                                       },
                                       'sexes_allowed': {
                                           'fillies': {
                                               'horses_general_results': 'allowed_fillies',
                                               'race_info': 'allowed_fillies',
                                               'horse_pps': 'allowed_fillies',
                                           },
                                           'mares': {
                                               'horses_general_results': 'allowed_mares',
                                               'race_info': 'allowed_mares',
                                               'horse_pps': 'allowed_mares',
                                           },
                                           'colts_geldings': {
                                               'horses_general_results': 'allowed_colts_geldings',
                                               'race_info': 'allowed_colts_geldings',
                                               'horse_pps': 'allowed_colts_geldings',
                                           },
                                       },

                                       'statebred_race': {
                                           'race_general_results': 'statebred_race',
                                           'race_info': 'statebred_race',
                                           'horse_pps': 'statebred_race',
                                       },

                                       'race_conditions_1': {
                                           'claim_start_required_price': {
                                               'race_general_results': 'condition_1_start_required_price',
                                               'race_info': 'condition_1_start_required_price',
                                               'horse_pps': '',
                                           },
                                           'claim_start_time_limit': {
                                               'race_general_results': 'condition_1_start_required_months',
                                               'race_info': 'condition_1_start_required_months',
                                               'horse_pps': '',
                                           },

                                           'not_won_limit': {
                                               'race_general_results': 'condition_1_number_limit',
                                               'race_info': 'condition_1_number_limit',
                                               'horse_pps': '',
                                           },
                                           'money_limit': {
                                               'race_general_results': 'condition_1_money_limit',
                                               'race_info': 'condition_1_money_limit',
                                               'horse_pps': '',
                                           },
                                           'time_limit': {
                                               'race_general_results': 'condition_1_time_limit_months',
                                               'race_info': 'condition_1_time_limit_months',
                                               'horse_pps': '',
                                           },
                                           'excluded_races': {
                                               'claiming': {
                                                   'race_general_results': 'condition_1_excluded_claiming',
                                                   'race_info': 'condition_1_excluded_claiming',
                                                   'horse_pps': '',
                                               },
                                               'maiden': {
                                                   'race_general_results': 'condition_1_excluded_maiden',
                                                   'race_info': 'condition_1_excluded_maiden',
                                                   'horse_pps': '',
                                               },
                                               'optional': {
                                                   'race_general_results': 'condition_1_excluded_optional',
                                                   'race_info': 'condition_1_excluded_optional',
                                                   'horse_pps': '',
                                               },
                                               'restricted': {
                                                   'race_general_results': 'condition_1_excluded_restricted',
                                                   'race_info': 'condition_1_excluded_restricted',
                                                   'horse_pps': '',
                                               },
                                               'restricted_allowance': {
                                                   'race_general_results': 'condition_1_excluded_restricted_allowance',
                                                   'race_info': 'condition_1_excluded_restricted_allowance',
                                                   'horse_pps': '',
                                               },
                                               'starter': {
                                                   'race_general_results': 'condition_1_excluded_starter',
                                                   'race_info': 'condition_1_excluded_starter',
                                                   'horse_pps': '',
                                               },
                                               'state_sired': {
                                                   'race_general_results': 'condition_1_excluded_state_sired',
                                                   'race_info': 'condition_1_excluded_state_sired',
                                                   'horse_pps': '',
                                               },
                                               'state_sired_stakes': {
                                                   'race_general_results': 'condition_1_excluded_state_sired_stakes',
                                                   'race_info': 'condition_1_excluded_state_sired_stakes',
                                                   'horse_pps': '',
                                               },
                                               'statebred': {
                                                   'race_general_results': 'condition_1_excluded_statebred',
                                                   'race_info': 'condition_1_excluded_statebred',
                                                   'horse_pps': '',
                                               },
                                               'statebred_allowance': {
                                                   'race_general_results': 'condition_1_excluded_statebred_allowance',
                                                   'race_info': 'condition_1_excluded_statebred_allowance',
                                                   'horse_pps': '',
                                               },
                                               'statebred_stakes': {
                                                   'race_general_results': 'condition_1_excluded_statebred_stakes',
                                                   'race_info': 'condition_1_excluded_statebred_stakes',
                                                   'horse_pps': '',
                                               },
                                               'trial': {
                                                   'race_general_results': 'condition_1_excluded_trial',
                                                   'race_info': 'condition_1_excluded_trial',
                                                   'horse_pps': '',
                                               },
                                               'waiver': {
                                                   'race_general_results': 'condition_1_excluded_waiver',
                                                   'race_info': 'condition_1_excluded_waiver',
                                                   'horse_pps': '',
                                               },
                                               'waiver_claiming': {
                                                   'race_general_results': 'condition_1_excluded_waiver_claiming',
                                                   'race_info': 'condition_1_excluded_waiver_claiming',
                                                   'horse_pps': '',
                                               },
                                           },
                                       },

                                       'race_conditions_2': {
                                           'claim_start_required_price': {
                                               'race_general_results': 'condition_2_start_required_price',
                                               'race_info': 'condition_2_start_required_price',
                                               'horse_pps': '',
                                           },
                                           'claim_start_time_limit': {
                                               'race_general_results': 'condition_2_start_required_months',
                                               'race_info': 'condition_2_start_required_months',
                                               'horse_pps': '',
                                           },

                                           'not_won_limit': {
                                               'race_general_results': 'condition_2_number_limit',
                                               'race_info': 'condition_2_number_limit',
                                               'horse_pps': '',
                                           },
                                           'money_limit': {
                                               'race_general_results': 'condition_2_money_limit',
                                               'race_info': 'condition_2_money_limit',
                                               'horse_pps': '',
                                           },
                                           'time_limit': {
                                               'race_general_results': 'condition_2_time_limit_months',
                                               'race_info': 'condition_2_time_limit_months',
                                               'horse_pps': '',
                                           },
                                           'excluded_races': {
                                               'claiming': {
                                                   'race_general_results': 'condition_2_excluded_claiming',
                                                   'race_info': 'condition_2_excluded_claiming',
                                                   'horse_pps': '',
                                               },
                                               'maiden': {
                                                   'race_general_results': 'condition_2_excluded_maiden',
                                                   'race_info': 'condition_2_excluded_maiden',
                                                   'horse_pps': '',
                                               },
                                               'optional': {
                                                   'race_general_results': 'condition_2_excluded_optional',
                                                   'race_info': 'condition_2_excluded_optional',
                                                   'horse_pps': '',
                                               },
                                               'restricted': {
                                                   'race_general_results': 'condition_2_excluded_restricted',
                                                   'race_info': 'condition_2_excluded_restricted',
                                                   'horse_pps': '',
                                               },
                                               'restricted_allowance': {
                                                   'race_general_results': 'condition_2_excluded_restricted_allowance',
                                                   'race_info': 'condition_2_excluded_restricted_allowance',
                                                   'horse_pps': '',
                                               },
                                               'starter': {
                                                   'race_general_results': 'condition_2_excluded_starter',
                                                   'race_info': 'condition_2_excluded_starter',
                                                   'horse_pps': '',
                                               },
                                               'state_sired': {
                                                   'race_general_results': 'condition_2_excluded_state_sired',
                                                   'race_info': 'condition_2_excluded_state_sired',
                                                   'horse_pps': '',
                                               },
                                               'state_sired_stakes': {
                                                   'race_general_results': 'condition_2_excluded_state_sired_stakes',
                                                   'race_info': 'condition_2_excluded_state_sired_stakes',
                                                   'horse_pps': '',
                                               },
                                               'statebred': {
                                                   'race_general_results': 'condition_2_excluded_statebred',
                                                   'race_info': 'condition_2_excluded_statebred',
                                                   'horse_pps': '',
                                               },
                                               'statebred_allowance': {
                                                   'race_general_results': 'condition_2_excluded_statebred_allowance',
                                                   'race_info': 'condition_2_excluded_statebred_allowance',
                                                   'horse_pps': '',
                                               },
                                               'statebred_stakes': {
                                                   'race_general_results': 'condition_2_excluded_statebred_stakes',
                                                   'race_info': 'condition_2_excluded_statebred_stakes',
                                                   'horse_pps': '',
                                               },
                                               'trial': {
                                                   'race_general_results': 'condition_2_excluded_trial',
                                                   'race_info': 'condition_2_excluded_trial',
                                                   'horse_pps': '',
                                               },
                                               'waiver': {
                                                   'race_general_results': 'condition_2_excluded_waiver',
                                                   'race_info': 'condition_2_excluded_waiver',
                                                   'horse_pps': '',
                                               },
                                               'waiver_claiming': {
                                                   'race_general_results': 'condition_2_excluded_waiver_claiming',
                                                   'race_info': 'condition_2_excluded_waiver_claiming',
                                                   'horse_pps': '',
                                               },
                                           },
                                       },

                                       'race_conditions_3': {
                                           'claim_start_required_price': {
                                               'race_general_results': 'condition_3_start_required_price',
                                               'race_info': 'condition_3_start_required_price',
                                               'horse_pps': '',
                                           },
                                           'claim_start_time_limit': {
                                               'race_general_results': 'condition_3_start_required_months',
                                               'race_info': 'condition_3_start_required_months',
                                               'horse_pps': '',
                                           },
                                           'not_won_limit': {
                                               'race_general_results': 'condition_3_number_limit',
                                               'race_info': 'condition_3_number_limit',
                                               'horse_pps': '',
                                           },
                                           'money_limit': {
                                               'race_general_results': 'condition_3_money_limit',
                                               'race_info': 'condition_3_money_limit',
                                               'horse_pps': '',
                                           },
                                           'time_limit': {
                                               'race_general_results': 'condition_3_time_limit_months',
                                               'race_info': 'condition_3_time_limit_months',
                                               'horse_pps': '',
                                           },
                                           'excluded_races': {
                                               'claiming': {
                                                   'race_general_results': 'condition_3_excluded_claiming',
                                                   'race_info': 'condition_3_excluded_claiming',
                                                   'horse_pps': '',
                                               },
                                               'maiden': {
                                                   'race_general_results': 'condition_3_excluded_maiden',
                                                   'race_info': 'condition_3_excluded_maiden',
                                                   'horse_pps': '',
                                               },
                                               'optional': {
                                                   'race_general_results': 'condition_3_excluded_optional',
                                                   'race_info': 'condition_3_excluded_optional',
                                                   'horse_pps': '',
                                               },
                                               'restricted': {
                                                   'race_general_results': 'condition_3_excluded_restricted',
                                                   'race_info': 'condition_3_excluded_restricted',
                                                   'horse_pps': '',
                                               },
                                               'restricted_allowance': {
                                                   'race_general_results': 'condition_3_excluded_restricted_allowance',
                                                   'race_info': 'condition_3_excluded_restricted_allowance',
                                                   'horse_pps': '',
                                               },
                                               'starter': {
                                                   'race_general_results': 'condition_3_excluded_starter',
                                                   'race_info': 'condition_3_excluded_starter',
                                                   'horse_pps': '',
                                               },
                                               'state_sired': {
                                                   'race_general_results': 'condition_3_excluded_state_sired',
                                                   'race_info': 'condition_3_excluded_state_sired',
                                                   'horse_pps': '',
                                               },
                                               'state_sired_stakes': {
                                                   'race_general_results': 'condition_3_excluded_state_sired_stakes',
                                                   'race_info': 'condition_3_excluded_state_sired_stakes',
                                                   'horse_pps': '',
                                               },
                                               'statebred': {
                                                   'race_general_results': 'condition_3_excluded_statebred',
                                                   'race_info': 'condition_3_excluded_statebred',
                                                   'horse_pps': '',
                                               },
                                               'statebred_allowance': {
                                                   'race_general_results': 'condition_3_excluded_statebred_allowance',
                                                   'race_info': 'condition_3_excluded_statebred_allowance',
                                                   'horse_pps': '',
                                               },
                                               'statebred_stakes': {
                                                   'race_general_results': 'condition_3_excluded_statebred_stakes',
                                                   'race_info': 'condition_3_excluded_statebred_stakes',
                                                   'horse_pps': '',
                                               },
                                               'trial': {
                                                   'race_general_results': 'condition_3_excluded_trial',
                                                   'race_info': 'condition_3_excluded_trial',
                                                   'horse_pps': '',
                                               },
                                               'waiver': {
                                                   'race_general_results': 'condition_3_excluded_waiver',
                                                   'race_info': 'condition_3_excluded_waiver',
                                                   'horse_pps': '',
                                               },
                                               'waiver_claiming': {
                                                   'race_general_results': 'condition_3_excluded_waiver_claiming',
                                                   'race_info': 'condition_3_excluded_waiver_claiming',
                                                   'horse_pps': '',
                                               },
                                           },
                                       },

                                       'purse': {
                                           'race_general_results': 'purse',
                                           'race_info': 'purse',
                                           'horse_pps': 'race_purse',
                                       },

                                       'claiming_price_base': {
                                           'race_general_results': 'max_claim',
                                           'race_info': 'claiming_price',
                                           'horse_pps': 'highest_claim_price',
                                       },
                                       'optional_claiming_price': {
                                           'race_general_results': 'optional_claiming_price',
                                           'race_info': 'optional_claiming_price',
                                           'horse_pps': None,

                                       },

                                       'race_type': {
                                           'race_general_results': 'race_type_BRIS',
                                       # Could also use race_type_equibase
                                           'race_info': 'race_type',
                                           'horse_pps': 'race_type',

                                       },

                                       'race_conditions_text_1': {
                                           'race_general_results': 'race_cond_1',
                                           'race_info': 'race_conditions_1',
                                           'horse_pps': None,
                                       },
                                       'race_conditions_text_2': {
                                           'race_general_results': 'race_cond_2',
                                           'race_info': 'race_conditions_2',
                                           'horse_pps': None,
                                       },
                                       'race_conditions_text_3': {
                                           'race_general_results': 'race_cond_3',
                                           'race_info': 'race_conditions_3',
                                           'horse_pps': None,
                                       },
                                       'race_conditions_text_4': {
                                           'race_general_results': 'race_cond_4',
                                           'race_info': 'race_conditions_4',
                                           'horse_pps': None,
                                       },
                                       'race_conditions_text_5': {
                                           'race_general_results': 'race_cond_5',
                                           'race_info': 'race_conditions_5',
                                           'horse_pps': None,
                                       },
                                       'race_conditions_text_6': {
                                           'race_general_results': 'race_cond_6',
                                           'race_info': None,
                                           'horse_pps': None,
                                       },

                                       'race_notes': {
                                           'race_general_results': None,
                                           'race_info': None,
                                           'horse_pps': None,
                                       },
                                   }







