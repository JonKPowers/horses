col_1_dtypes = {
    'track_code': 'VARCHAR(255)',
    'date': 'INT',
    'race_num': 'INT',
    'day_evening_flag': 'VARCHAR(255)',
    'distance': 'FLOAT',
    'distance_units': 'VARCHAR(255)',
    'about_dist_flag': 'INT',
    'surface_old_style': 'VARCHAR(255)',
    'surface_new_style': 'VARCHAR(255)',
    'all_weather_flag': 'INT',
    'chute_start_flag': 'INT',
    'BRIS_race_type': 'VARCHAR(255)',
    'equibase_race_type': 'VARCHAR(255)',
    'race_grade': 'INT',
    'age_sex_restrictions': 'VARCHAR(255)',
    'race_restrict_code': 'VARCHAR(255)',
    'state_bred_flag': 'VARCHAR(255)',
    'abbrev_race_class': 'VARCHAR(255)',
    'breed_of_race': 'VARCHAR(255)',
    'country_code': 'VARCHAR(255)',
    'purse': 'INT',
    'total_race_value': 'INT',
    'max_claim_price': 'INT',
    'race_conditions_1': 'VARCHAR(255)',
    'race_conditions_2': 'VARCHAR(255)',
    'race_conditions_3': 'VARCHAR(255)',
    'race_conditions_4': 'VARCHAR(255)',
    'race_conditions_5': 'VARCHAR(255)',
    'field_size': 'INT',
    'track_condition': 'VARCHAR(255)',
    'fraction_1_time': 'FLOAT',
    'fraction_2_time': 'FLOAT',
    'fraction_3_time': 'FLOAT',
    'fraction_4_time': 'FLOAT',
    'fraction_5_time': 'FLOAT',
    'final_time': 'FLOAT',
    'fraction_1_dist': 'INT',
    'fraction_2_dist': 'INT',
    'fraction_3_dist': 'INT',
    'fraction_4_dist': 'INT',
    'fraction_5_dist': 'INT',
    'off_time': 'INT',
    'start_call_dist': 'INT',
    'call_dist_first': 'INT',
    'call_dist_second': 'INT',
    'call_dist_third': 'INT',
    'race_name': 'VARCHAR(255)',
    'start_description': 'VARCHAR(255)',
    'temp_rail_dist': 'INT',
    'off_turf_flag': 'INT',
    'off_turf_dist_change': 'INT',
    'weather': 'VARCHAR(255)',
    'race_temp': 'INT',
    'WPS_show_pool': 'FLOAT',
    'run_up_dist': 'INT',
}

col_2_dtypes = {
    'track_code': 'VARCHAR(255)',
    'date': 'INT',
    'race_num': 'INT',
    'day_evening_flag': 'VARCHAR(255)',
    'horse_name': 'VARCHAR(255)',
    'foreign_bred_code': 'VARCHAR(255)',
    'state_bred_code': 'VARCHAR(255)',
    'post_position': 'INT',
    'program_number': 'VARCHAR(255)',
    'birth_year': 'INT',
    'breed': 'VARCHAR(255)',
    'coupled_flag': 'VARCHAR(255)',
    'jockey_name': 'VARCHAR(255)',
    'jockey_last_name': 'VARCHAR(255)',
    'jockey_first_name': 'VARCHAR(255)',
    'jockey_middle_name': 'VARCHAR(255)',
    'trainer_name': 'VARCHAR(255)',
    'trainer__last_name': 'VARCHAR(255)',
    'trainer_first_name': 'VARCHAR(255)',
    'trainer_middle_name': 'VARCHAR(255)',
    'trip_comment': 'VARCHAR(255)',
    'owner_name': 'VARCHAR(255)',
    'owner_first_name': 'VARCHAR(255)',
    'owner_middle_name': 'VARCHAR(255)',
    'claiming_price': 'INT',
    'medication_codes': 'VARCHAR(255)',
    'equipment_code': 'VARCHAR(255)',
    'earnings': 'INT',
    'odds': 'FLOAT',
    'nonbetting_flag': 'VARCHAR(255)',
    'favorite_flag': 'INT',
    'disqualified_flag': 'INT',
    'disqualified_placing': 'INT',
    'weight': 'INT',
    'corrected_weight': 'INT',
    'overweight_amt': 'INT',
    'claimed_flag': 'INT',
    'claimed_trainer': 'VARCHAR(255)',
    'claimed_trainer_last': 'VARCHAR(255)',
    'claimed_trainer_first': 'VARCHAR(255)',
    'claimed_trainer_middle': 'VARCHAR(255)',
    'claimed_owner': 'VARCHAR(255)',
    'claimed_owner_last': 'VARCHAR(255)',
    'claimed_owner_first': 'VARCHAR(255)',
    'claimed_owner_middle': 'VARCHAR(255)',
    'win_payout': 'FLOAT',
    'place_payout': 'FLOAT',
    'show_payout': 'FLOAT',
    'start_call_pos': 'INT',
    '1st_call_pos': 'INT',
    '2d_call_pos': 'INT',
    '3d_call_pos': 'INT',
    'stretch_call_pos': 'INT',
    'finish_pos': 'INT',
    'official_finish_pos': 'INT',
    'start_lead': 'FLOAT',
    '1st_call_lead': 'FLOAT',
    '2d_call_lead': 'FLOAT',
    '3d_call_lead': 'FLOAT',
    'stretch_lead': 'FLOAT',
    'finish_lead': 'FLOAT',
    'start_beaten': 'FLOAT',
    '1st_call_beaten': 'FLOAT',
    '2d_call_beaten': 'FLOAT',
    '3d_call_beaten': 'FLOAT',
    'stretch_call_beaten': 'FLOAT',
    'finish_beaten': 'FLOAT',
    'start_margin': 'FLOAT',
    '1st_call_margin': 'FLOAT',
    '2d_call_margin': 'FLOAT',
    '3d_call_margin': 'FLOAT',
    'stretch_call_margin': 'FLOAT',
    'finish_margin': 'FLOAT',
    'dead_heat_flag': 'INT',
    'horse_reg_id': 'VARCHAR(255)',
    'jockey_id': 'INT',
    'trainer_id': 'INT',
    'owner_id': 'INT',
    'claimed_trainer_id': 'INT',
    'claimed_owner_id': 'INT',
}

col_3_dtypes = {
    'track_code': 'VARCHAR(255)',
    'date': 'INT',
    'race_num': 'INT',
    'day_evening_flag': 'VARCHAR(255)',
    'horse_name': 'VARCHAR(255)',
    'foreign_bred_code': 'VARCHAR(255)',
    'statebred_code': 'VARCHAR(255)',
    'program_number': 'VARCHAR(255)',
    'win_payout': 'FLOAT',
    'place_payout': 'FLOAT',
    'show_payout': 'FLOAT',
}

col_4_dtypes = {
    'track_code': 'VARCHAR(255)',
    'date': 'INT',
    'race_num': 'INT',
    'day_evening_flag': 'VARCHAR(255)',
    'wager_type': 'VARCHAR(255)',
    'bet_amount': 'FLOAT',
    'payout_amount': 'FLOAT',
    'number_correct': 'VARCHAR(255)',
    'winning_numbers': 'VARCHAR(255)',
    'wager_pool': 'FLOAT',
    'carryover_amount': 'FLOAT'
}

col_5_dtypes = {
    'track_code': 'VARCHAR(255)',
    'date': 'INT',
    'race_num': 'INT',
    'day_evening_flag': 'VARCHAR(255)',
    'horse_name': 'VARCHAR(255)',
    'foreignbred_code': 'VARCHAR(255)',
    'statebred_code': 'VARCHAR(255)',
    'program_number': 'VARCHAR(255)',
    'breeder': 'VARCHAR(255)',
    'color': 'VARCHAR(255)',
    'foal_date': 'INT',
    'age': 'INT',
    'sex': 'VARCHAR(255)',
    'sire': 'VARCHAR(255)',
    'dam': 'VARCHAR(255)',
    'broodmare_sire': 'VARCHAR(255)',
}

col_6_dtypes = {
    'track_code': 'VARCHAR(255)',
    'date': 'INT',
    'race_num': 'INT',
    'day_evening_flag': 'VARCHAR(255)',
    'footnote_sequence': 'INT',
    'footnote_text': 'VARCHAR(255)'
}

past_performances_dtypes = {  ## Up to date as of 4/28/2014

'track': 'VARCHAR(255)',
'date': 'VARCHAR(255)',
'race': 'INT',
'post_position': 'INT',
'entry': 'VARCHAR(255)',
'distance': 'INT',
'surface': 'VARCHAR(255)',
'race_type': 'VARCHAR(255)',
'age_sex_restricts': 'VARCHAR(255)',
'today_race_class': 'VARCHAR(255)',
'purse': 'INT',
'claiming_price': 'INT',
'horse_claiming_price': 'INT',
'track_record_pace': 'FLOAT',
'race_conditions': 'VARCHAR(255)',
'lasix_list': 'VARCHAR(255)',
'bute_list': 'VARCHAR(255)',
'coupled_list': 'VARCHAR(255)',
'mutuel_list': 'VARCHAR(255)',
'simulcast_track_code': 'VARCHAR(255)',
'simulcast_track_race': 'INT',
'breed_type': 'VARCHAR(255)',
'today_nasal_strip_chg': 'INT',
'allweather_surface': 'INT',
# *** Today's Horse/Trainer/Jockey/Owner ***
'trainer': 'VARCHAR(255)',
'trainer_starts': 'INT',
'trainer_wins': 'INT',
'trainer_places': 'INT',
'trainer_shows': 'INT',
'jockey': 'VARCHAR(255)',
'apprentice_wgt_alw': 'INT',
'jockey_starts': 'INT',
'jockey_wins': 'INT',
'jockey_places': 'INT',
'jockey_shows': 'INT',
'todays_owner': 'VARCHAR(255)',
'owners_silks': 'VARCHAR(255)',
'main_track_only_AE': 'VARCHAR(255)',
'program_number': 'VARCHAR(255)',
'morning_line': 'FLOAT',
# *** Horse History Data ***
'horse_name': 'VARCHAR(255)',
'birth_year': 'INT',
'foaling_month': 'INT',
'sex': 'VARCHAR(255)',
'color': 'VARCHAR(255)',
'weight': 'INT',
'sire': 'VARCHAR(255)',
'sires_sire': 'VARCHAR(255)',
'dam': 'VARCHAR(255)',
'dams_sire': 'VARCHAR(255)',
'breeder': 'VARCHAR(255)',
'where_bred': 'VARCHAR(255)',
'program_post_pos': 'VARCHAR(255)',
# *** Current Horse Stats ***
'todays_meds_new': 'INT',
'todays_meds_old': 'INT',
'equipment_change': 'INT',

#      Horse's Lifetime Record @ Today's Distance

'life_distance_starts': 'INT',
'life_distance_wins': 'INT',
'life_distance_places': 'INT',
'life_distance_shows': 'INT',
'life_distance_earned': 'INT',
#      Horse's Lifetime Record @ Today's track:
'life_track_starts': 'INT',
'life_track_wins': 'INT',
'life_track_places': 'INT',
'life_track_shows': 'INT',
'life_track_earned': 'INT',
#      Horse's Lifetime Turf Record:
'life_turf_starts': 'INT',
'life_turf_wins': 'INT',
'life_turf_places': 'INT',
'life_turf_shows': 'INT',
'life_turf_earnings': 'INT',
#      Horse's Lifetime Wet Record:
'life_wet_starts': 'INT',
'life_wet_wins': 'INT',
'life_wet_places': 'INT',
'life_wet_shows': 'INT',
'life_wet_earned': 'INT',
#       Horse's Current Year Record:
'current_year_year': 'INT',
'current_year_starts': 'INT',
'current_year_wins': 'INT',
'current_year_places': 'INT',
'current_year_shows': 'INT',
'current_year_earned': 'INT',
#      Horse's Previous Year Record:
'past_year_year': 'INT',
'past_year_starts': 'INT',
'past_year_wins': 'INT',
'past_year_places': 'INT',
'past_year_shows': 'INT',
'past_year_earned': 'INT',
#      Horse's Lifetime Record:
'lifetime_starts': 'INT',
'lifetime_wins': 'INT',
'lifetime_places': 'INT',
'lifetime_shows': 'INT',
'lifetime_earned': 'INT',
#      Recent Workouts

'workout_date_1': 'INT',
'workout_date_2': 'INT',
'workout_date_3': 'INT',
'workout_date_4': 'INT',
'workout_date_5': 'INT',
'workout_date_6': 'INT',
'workout_date_7': 'INT',
'workout_date_8': 'INT',
'workout_date_9': 'INT',
'workout_date_10': 'INT',
'workout_date_11': 'INT',
'workout_date_12': 'INT',

'workout_time_1': 'FLOAT',
'workout_time_2': 'FLOAT',
'workout_time_3': 'FLOAT',
'workout_time_4': 'FLOAT',
'workout_time_5': 'FLOAT',
'workout_time_6': 'FLOAT',
'workout_time_7': 'FLOAT',
'workout_time_8': 'FLOAT',
'workout_time_9': 'FLOAT',
'workout_time_10': 'FLOAT',
'workout_time_11': 'FLOAT',
'workout_time_12': 'FLOAT',

'workout_track_1': 'VARCHAR(255)',
'workout_track_2': 'VARCHAR(255)',
'workout_track_3': 'VARCHAR(255)',
'workout_track_4': 'VARCHAR(255)',
'workout_track_5': 'VARCHAR(255)',
'workout_track_6': 'VARCHAR(255)',
'workout_track_7': 'VARCHAR(255)',
'workout_track_8': 'VARCHAR(255)',
'workout_track_9': 'VARCHAR(255)',
'workout_track_10': 'VARCHAR(255)',
'workout_track_11': 'VARCHAR(255)',
'workout_track_12': 'VARCHAR(255)',

'workout_distance_1': 'INT',
'workout_distance_2': 'INT',
'workout_distance_3': 'INT',
'workout_distance_4': 'INT',
'workout_distance_5': 'INT',
'workout_distance_6': 'INT',
'workout_distance_7': 'INT',
'workout_distance_8': 'INT',
'workout_distance_9': 'INT',
'workout_distance_10': 'INT',
'workout_distance_11': 'INT',
'workout_distance_12': 'INT',

'workout_condition_1': 'VARCHAR(255)',
'workout_condition_2': 'VARCHAR(255)',
'workout_condition_3': 'VARCHAR(255)',
'workout_condition_4': 'VARCHAR(255)',
'workout_condition_5': 'VARCHAR(255)',
'workout_condition_6': 'VARCHAR(255)',
'workout_condition_7': 'VARCHAR(255)',
'workout_condition_8': 'VARCHAR(255)',
'workout_condition_9': 'VARCHAR(255)',
'workout_condition_10': 'VARCHAR(255)',
'workout_condition_11': 'VARCHAR(255)',
'workout_condition_12': 'VARCHAR(255)',

'workout_description_1': 'VARCHAR(255)',
'workout_description_2': 'VARCHAR(255)',
'workout_description_3': 'VARCHAR(255)',
'workout_description_4': 'VARCHAR(255)',
'workout_description_5': 'VARCHAR(255)',
'workout_description_6': 'VARCHAR(255)',
'workout_description_7': 'VARCHAR(255)',
'workout_description_8': 'VARCHAR(255)',
'workout_description_9': 'VARCHAR(255)',
'workout_description_10': 'VARCHAR(255)',
'workout_description_11': 'VARCHAR(255)',
'workout_description_12': 'VARCHAR(255)',

'workout_track_type_1': 'VARCHAR(255)',
'workout_track_type_2': 'VARCHAR(255)',
'workout_track_type_3': 'VARCHAR(255)',
'workout_track_type_4': 'VARCHAR(255)',
'workout_track_type_5': 'VARCHAR(255)',
'workout_track_type_6': 'VARCHAR(255)',
'workout_track_type_7': 'VARCHAR(255)',
'workout_track_type_8': 'VARCHAR(255)',
'workout_track_type_9': 'VARCHAR(255)',
'workout_track_type_10': 'VARCHAR(255)',
'workout_track_type_11': 'VARCHAR(255)',
'workout_track_type_12': 'VARCHAR(255)',

'same_workouts_all_day_1': 'INT',
'same_workouts_all_day_2': 'INT',
'same_workouts_all_day_3': 'INT',
'same_workouts_all_day_4': 'INT',
'same_workouts_all_day_5': 'INT',
'same_workouts_all_day_6': 'INT',
'same_workouts_all_day_7': 'INT',
'same_workouts_all_day_8': 'INT',
'same_workouts_all_day_9': 'INT',
'same_workouts_all_day_10': 'INT',
'same_workouts_all_day_11': 'INT',
'same_workouts_all_day_12': 'INT',

'rank_same_workout_1': 'INT',
'rank_same_workout_2': 'INT',
'rank_same_workout_3': 'INT',
'rank_same_workout_4': 'INT',
'rank_same_workout_5': 'INT',
'rank_same_workout_6': 'INT',
'rank_same_workout_7': 'INT',
'rank_same_workout_8': 'INT',
'rank_same_workout_9': 'INT',
'rank_same_workout_10': 'INT',
'rank_same_workout_11': 'INT',
'rank_same_workout_12': 'INT',


'bris_run_style': 'VARCHAR(255)',
'quirin_speed_points': 'INT',
'2f_bris_pace_par': 'INT',
'4f_bris_pace_par': 'INT',
'6f_bris_pace_par': 'INT',
'bris_speed_par': 'INT',
'bris_late_pace_par': 'INT',

'TJ_starts': 'INT',
'TJ_wins': 'INT',
'TJ_places': 'INT',
'TJ_shows': 'INT',
'TJ_roi': 'INT',

'days_since_last_race': 'INT',

'race_conditions_1': 'VARCHAR(255)',
'race_conditions_2': 'VARCHAR(255)',
'race_conditions_3': 'VARCHAR(255)',
'race_conditions_4': 'VARCHAR(255)',
'race_conditions_5': 'VARCHAR(255)',
'race_conditions_6': 'VARCHAR(255)',

'life_starts_alw': 'INT',
'life_wins_alw': 'INT',
'life_places_alw': 'INT',
'life_shows_alw': 'INT',
'life_earnings_alw': 'INT',
'best_bris_speed_alw': 'INT',
'low_claiming_price': 'INT',
'statebread_flag': 'VARCHAR(255)',

'wager_type_1': 'VARCHAR(255)',
'wager_type_2': 'VARCHAR(255)',
'wager_type_3': 'VARCHAR(255)',
'wager_type_4': 'VARCHAR(255)',
'wager_type_5': 'VARCHAR(255)',
'wager_type_6': 'VARCHAR(255)',
'wager_type_7': 'VARCHAR(255)',
'wager_type_8': 'VARCHAR(255)',
'wager_type_9': 'VARCHAR(255)',

'bris_prime_power': 'INT',

#      *** Horse's Past Performace Data for last 10 races ***
#      For each of the last 10 races (most recent to furthest back):

'past_race_date_1': 'VARCHAR(255)',
'past_race_date_2': 'VARCHAR(255)',
'past_race_date_3': 'VARCHAR(255)',
'past_race_date_4': 'VARCHAR(255)',
'past_race_date_5': 'VARCHAR(255)',
'past_race_date_6': 'VARCHAR(255)',
'past_race_date_7': 'VARCHAR(255)',
'past_race_date_8': 'VARCHAR(255)',
'past_race_date_9': 'VARCHAR(255)',
'past_race_date_10': 'VARCHAR(255)',

'past_days_since_last_1': 'INT',
'past_days_since_last_2': 'INT',
'past_days_since_last_3': 'INT',
'past_days_since_last_4': 'INT',
'past_days_since_last_5': 'INT',
'past_days_since_last_6': 'INT',
'past_days_since_last_7': 'INT',
'past_days_since_last_8': 'INT',
'past_days_since_last_9': 'INT',
'maybe_reservd275': 'INT',

'past_track_code_1': 'VARCHAR(255)',
'past_track_code_2': 'VARCHAR(255)',
'past_track_code_3': 'VARCHAR(255)',
'past_track_code_4': 'VARCHAR(255)',
'past_track_code_5': 'VARCHAR(255)',
'past_track_code_6': 'VARCHAR(255)',
'past_track_code_7': 'VARCHAR(255)',
'past_track_code_8': 'VARCHAR(255)',
'past_track_code_9': 'VARCHAR(255)',
'past_track_code_10': 'VARCHAR(255)',

'past_BRIS_track_code_1': 'VARCHAR(255)',
'past_BRIS_track_code_2': 'VARCHAR(255)',
'past_BRIS_track_code_3': 'VARCHAR(255)',
'past_BRIS_track_code_4': 'VARCHAR(255)',
'past_BRIS_track_code_5': 'VARCHAR(255)',
'past_BRIS_track_code_6': 'VARCHAR(255)',
'past_BRIS_track_code_7': 'VARCHAR(255)',
'past_BRIS_track_code_8': 'VARCHAR(255)',
'past_BRIS_track_code_9': 'VARCHAR(255)',
'past_BRIS_track_code_10': 'VARCHAR(255)',

'past_race_number_1': 'INT',
'past_race_number_2': 'INT',
'past_race_number_3': 'INT',
'past_race_number_4': 'INT',
'past_race_number_5': 'INT',
'past_race_number_6': 'INT',
'past_race_number_7': 'INT',
'past_race_number_8': 'INT',
'past_race_number_9': 'INT',
'past_race_number_10': 'INT',

'past_track_cond_1': 'VARCHAR(255)',
'past_track_cond_2': 'VARCHAR(255)',
'past_track_cond_3': 'VARCHAR(255)',
'past_track_cond_4': 'VARCHAR(255)',
'past_track_cond_5': 'VARCHAR(255)',
'past_track_cond_6': 'VARCHAR(255)',
'past_track_cond_7': 'VARCHAR(255)',
'past_track_cond_8': 'VARCHAR(255)',
'past_track_cond_9': 'VARCHAR(255)',
'past_track_cond_10': 'VARCHAR(255)',

'past_distance_1': 'INT',
'past_distance_2': 'INT',
'past_distance_3': 'INT',
'past_distance_4': 'INT',
'past_distance_5': 'INT',
'past_distance_6': 'INT',
'past_distance_7': 'INT',
'past_distance_8': 'INT',
'past_distance_9': 'INT',
'past_distance_10': 'INT',

'past_surface_1': 'VARCHAR(255)',
'past_surface_2': 'VARCHAR(255)',
'past_surface_3': 'VARCHAR(255)',
'past_surface_4': 'VARCHAR(255)',
'past_surface_5': 'VARCHAR(255)',
'past_surface_6': 'VARCHAR(255)',
'past_surface_7': 'VARCHAR(255)',
'past_surface_8': 'VARCHAR(255)',
'past_surface_9': 'VARCHAR(255)',
'past_surface_10': 'VARCHAR(255)',

##      Special Chute Indicator
'past_special_chute_1': 'VARCHAR(255)',
'past_special_chute_2': 'VARCHAR(255)',
'past_special_chute_3': 'VARCHAR(255)',
'past_special_chute_4': 'VARCHAR(255)',
'past_special_chute_5': 'VARCHAR(255)',
'past_special_chute_6': 'VARCHAR(255)',
'past_special_chute_7': 'VARCHAR(255)',
'past_special_chute_8': 'VARCHAR(255)',
'past_special_chute_9': 'VARCHAR(255)',
'past_special_chute_10': 'VARCHAR(255)',

## Number of entrants
'past_entrants_1': 'INT',
'past_entrants_2': 'INT',
'past_entrants_3': 'INT',
'past_entrants_4': 'INT',
'past_entrants_5': 'INT',
'past_entrants_6': 'INT',
'past_entrants_7': 'INT',
'past_entrants_8': 'INT',
'past_entrants_9': 'INT',
'past_entrants_10': 'INT',

##      Past post position

'past_post_1': 'INT',
'past_post_2': 'INT',
'past_post_3': 'INT',
'past_post_4': 'INT',
'past_post_5': 'INT',
'past_post_6': 'INT',
'past_post_7': 'INT',
'past_post_8': 'INT',
'past_post_9': 'INT',
'past_post_10': 'INT',

# Equipment                                                                    b - blinkers
'past_equipment_1': 'VARCHAR(255)',
'past_equipment_2': 'VARCHAR(255)',
'past_equipment_3': 'VARCHAR(255)',
'past_equipment_4': 'VARCHAR(255)',
'past_equipment_5': 'VARCHAR(255)',
'past_equipment_6': 'VARCHAR(255)',
'past_equipment_7': 'VARCHAR(255)',
'past_equipment_8': 'VARCHAR(255)',
'past_equipment_9': 'VARCHAR(255)',
'past_equipment_10': 'VARCHAR(255)',

##      Race name of previous races
'past_race_name_1': 'VARCHAR(255)',
'past_race_name_2': 'VARCHAR(255)',
'past_race_name_3': 'VARCHAR(255)',
'past_race_name_4': 'VARCHAR(255)',
'past_race_name_5': 'VARCHAR(255)',
'past_race_name_6': 'VARCHAR(255)',
'past_race_name_7': 'VARCHAR(255)',
'past_race_name_8': 'VARCHAR(255)',
'past_race_name_9': 'VARCHAR(255)',
'past_race_name_10': 'VARCHAR(255)',

##      Medication
'past_medication_1': 'INT',
'past_medication_2': 'INT',
'past_medication_3': 'INT',
'past_medication_4': 'INT',
'past_medication_5': 'INT',
'past_medication_6': 'INT',
'past_medication_7': 'INT',
'past_medication_8': 'INT',
'past_medication_9': 'INT',
'past_medication_10': 'INT',

##      Trip Comment
'past_trip_comment_1': 'VARCHAR(255)',
'past_trip_comment_2': 'VARCHAR(255)',
'past_trip_comment_3': 'VARCHAR(255)',
'past_trip_comment_4': 'VARCHAR(255)',
'past_trip_comment_5': 'VARCHAR(255)',
'past_trip_comment_6': 'VARCHAR(255)',
'past_trip_comment_7': 'VARCHAR(255)',
'past_trip_comment_8': 'VARCHAR(255)',
'past_trip_comment_9': 'VARCHAR(255)',
'past_trip_comment_10': 'VARCHAR(255)',

##      Winner, Place, and Show horse names
'past_win_1': 'VARCHAR(255)',
'past_win_2': 'VARCHAR(255)',
'past_win_3': 'VARCHAR(255)',
'past_win_4': 'VARCHAR(255)',
'past_win_5': 'VARCHAR(255)',
'past_win_6': 'VARCHAR(255)',
'past_win_7': 'VARCHAR(255)',
'past_win_8': 'VARCHAR(255)',
'past_win_9': 'VARCHAR(255)',
'past_win_10': 'VARCHAR(255)',

'past_place_1': 'VARCHAR(255)',
'past_place_2': 'VARCHAR(255)',
'past_place_3': 'VARCHAR(255)',
'past_place_4': 'VARCHAR(255)',
'past_place_5': 'VARCHAR(255)',
'past_place_6': 'VARCHAR(255)',
'past_place_7': 'VARCHAR(255)',
'past_place_8': 'VARCHAR(255)',
'past_place_9': 'VARCHAR(255)',
'past_place_10': 'VARCHAR(255)',

'past_show_1': 'VARCHAR(255)',
'past_show_2': 'VARCHAR(255)',
'past_show_3': 'VARCHAR(255)',
'past_show_4': 'VARCHAR(255)',
'past_show_5': 'VARCHAR(255)',
'past_show_6': 'VARCHAR(255)',
'past_show_7': 'VARCHAR(255)',
'past_show_8': 'VARCHAR(255)',
'past_show_9': 'VARCHAR(255)',
'past_show_10': 'VARCHAR(255)',

##      Winner, PLcae, and Show Weight Carried

'past_win_weight_1': 'INT',
'past_win_weight_2': 'INT',
'past_win_weight_3': 'INT',
'past_win_weight_4': 'INT',
'past_win_weight_5': 'INT',
'past_win_weight_6': 'INT',
'past_win_weight_7': 'INT',
'past_win_weight_8': 'INT',
'past_win_weight_9': 'INT',
'past_win_weight_10': 'INT',

'past_place_weight_1': 'INT',
'past_place_weight_2': 'INT',
'past_place_weight_3': 'INT',
'past_place_weight_4': 'INT',
'past_place_weight_5': 'INT',
'past_place_weight_6': 'INT',
'past_place_weight_7': 'INT',
'past_place_weight_8': 'INT',
'past_place_weight_9': 'INT',
'past_place_weight_10': 'INT',

'past_show_weight_1': 'INT',
'past_show_weight_2': 'INT',
'past_show_weight_3': 'INT',
'past_show_weight_4': 'INT',
'past_show_weight_5': 'INT',
'past_show_weight_6': 'INT',
'past_show_weight_7': 'INT',
'past_show_weight_8': 'INT',
'past_show_weight_9': 'INT',
'past_show_weight_10': 'INT',

##      Past Winner, Place, and Show Margins

'past_win_margin_1': 'FLOAT',
'past_win_margin_2': 'FLOAT',
'past_win_margin_3': 'FLOAT',
'past_win_margin_4': 'FLOAT',
'past_win_margin_5': 'FLOAT',
'past_win_margin_6': 'FLOAT',
'past_win_margin_7': 'FLOAT',
'past_win_margin_8': 'FLOAT',
'past_win_margin_9': 'FLOAT',
'past_win_margin_10': 'FLOAT',

'past_place_margin_1': 'FLOAT',
'past_place_margin_2': 'FLOAT',
'past_place_margin_3': 'FLOAT',
'past_place_margin_4': 'FLOAT',
'past_place_margin_5': 'FLOAT',
'past_place_margin_6': 'FLOAT',
'past_place_margin_7': 'FLOAT',
'past_place_margin_8': 'FLOAT',
'past_place_margin_9': 'FLOAT',
'past_place_margin_10': 'FLOAT',

'past_show_margin_1': 'FLOAT',
'past_show_margin_2': 'FLOAT',
'past_show_margin_3': 'FLOAT',
'past_show_margin_4': 'FLOAT',
'past_show_margin_5': 'FLOAT',
'past_show_margin_6': 'FLOAT',
'past_show_margin_7': 'FLOAT',
'past_show_margin_8': 'FLOAT',
'past_show_margin_9': 'FLOAT',
'past_show_margin_10': 'FLOAT',

##      Alternate/Extra Comment Line

'past_extra_comment_1': 'VARCHAR(255)',
'past_extra_comment_2': 'VARCHAR(255)',
'past_extra_comment_3': 'VARCHAR(255)',
'past_extra_comment_4': 'VARCHAR(255)',
'past_extra_comment_5': 'VARCHAR(255)',
'past_extra_comment_6': 'VARCHAR(255)',
'past_extra_comment_7': 'VARCHAR(255)',
'past_extra_comment_8': 'VARCHAR(255)',
'past_extra_comment_9': 'VARCHAR(255)',
'past_extra_comment_10': 'VARCHAR(255)',

'past_weight_1': 'INT',
'past_weight_2': 'INT',
'past_weight_3': 'INT',
'past_weight_4': 'INT',
'past_weight_5': 'INT',
'past_weight_6': 'INT',
'past_weight_7': 'INT',
'past_weight_8': 'INT',
'past_weight_9': 'INT',
'past_weight_10': 'INT',

'past_odds_1': 'FLOAT',
'past_odds_2': 'FLOAT',
'past_odds_3': 'FLOAT',
'past_odds_4': 'FLOAT',
'past_odds_5': 'FLOAT',
'past_odds_6': 'FLOAT',
'past_odds_7': 'FLOAT',
'past_odds_8': 'FLOAT',
'past_odds_9': 'FLOAT',
'past_odds_10': 'FLOAT',

'past_entry_1': 'VARCHAR(255)',
'past_entry_2': 'VARCHAR(255)',
'past_entry_3': 'VARCHAR(255)',
'past_entry_4': 'VARCHAR(255)',
'past_entry_5': 'VARCHAR(255)',
'past_entry_6': 'VARCHAR(255)',
'past_entry_7': 'VARCHAR(255)',
'past_entry_8': 'VARCHAR(255)',
'past_entry_9': 'VARCHAR(255)',
'past_entry_10': 'VARCHAR(255)',

'past_race_class_1': 'VARCHAR(255)',
'past_race_class_2': 'VARCHAR(255)',        ##      537     CHARACTER               25
'past_race_class_3': 'VARCHAR(255)',        ##      538     CHARACTER               25
'past_race_class_4': 'VARCHAR(255)',        ##      539     CHARACTER               25
'past_race_class_5': 'VARCHAR(255)',        ##      540     CHARACTER               25
'past_race_class_6': 'VARCHAR(255)',        ##      541     CHARACTER               25
'past_race_class_7': 'VARCHAR(255)',        ##      542     CHARACTER               25
'past_race_class_8': 'VARCHAR(255)',        ##      543     CHARACTER               25
'past_race_class_9': 'VARCHAR(255)',        ##      544     CHARACTER               25
'past_race_class_10': 'VARCHAR(255)',       ##      545     CHARACTER               25

##      Claiming Price (of horse)
'past_claim_price_1': 'INT',
'past_claim_price_2': 'INT',
'past_claim_price_3': 'INT',
'past_claim_price_4': 'INT',
'past_claim_price_5': 'INT',
'past_claim_price_6': 'INT',
'past_claim_price_7': 'INT',
'past_claim_price_8': 'INT',
'past_claim_price_9': 'INT',
'past_claim_price_10': 'INT',

'past_purse_1': 'INT',
'past_purse_2': 'INT',
'past_purse_3': 'INT',
'past_purse_4': 'INT',
'past_purse_5': 'INT',
'past_purse_6': 'INT',
'past_purse_7': 'INT',
'past_purse_8': 'INT',
'past_purse_9': 'INT',
'past_purse_10': 'INT',

##      Start call position
'past_call_pos_start_1': 'VARCHAR(255)',
'past_call_pos_start_2': 'VARCHAR(255)',
'past_call_pos_start_3': 'VARCHAR(255)',
'past_call_pos_start_4': 'VARCHAR(255)',
'past_call_pos_start_5': 'VARCHAR(255)',
'past_call_pos_start_6': 'VARCHAR(255)',
'past_call_pos_start_7': 'VARCHAR(255)',
'past_call_pos_start_8': 'VARCHAR(255)',
'past_call_pos_start_9': 'VARCHAR(255)',
'past_call_pos_start_10': 'VARCHAR(255)',

'past_call_pos_first_1': 'VARCHAR(255)',
'past_call_pos_first_2': 'VARCHAR(255)',
'past_call_pos_first_3': 'VARCHAR(255)',
'past_call_pos_first_4': 'VARCHAR(255)',
'past_call_pos_first_5': 'VARCHAR(255)',
'past_call_pos_first_6': 'VARCHAR(255)',
'past_call_pos_first_7': 'VARCHAR(255)',
'past_call_pos_first_8': 'VARCHAR(255)',
'past_call_pos_first_9': 'VARCHAR(255)',
'past_call_pos_first_10': 'VARCHAR(255)',

'past_call_pos_second_1': 'VARCHAR(255)',
'past_call_pos_second_2': 'VARCHAR(255)',
'past_call_pos_second_3': 'VARCHAR(255)',
'past_call_pos_second_4': 'VARCHAR(255)',
'past_call_pos_second_5': 'VARCHAR(255)',
'past_call_pos_second_6': 'VARCHAR(255)',
'past_call_pos_second_7': 'VARCHAR(255)',
'past_call_pos_second_8': 'VARCHAR(255)',
'past_call_pos_second_9': 'VARCHAR(255)',
'past_call_pos_second_10': 'VARCHAR(255)',

'past_call_pos_gate_1': 'VARCHAR(255)',
'past_call_pos_gate_2': 'VARCHAR(255)',
'past_call_pos_gate_3': 'VARCHAR(255)',
'past_call_pos_gate_4': 'VARCHAR(255)',
'past_call_pos_gate_5': 'VARCHAR(255)',
'past_call_pos_gate_6': 'VARCHAR(255)',
'past_call_pos_gate_7': 'VARCHAR(255)',
'past_call_pos_gate_8': 'VARCHAR(255)',
'past_call_pos_gate_9': 'VARCHAR(255)',
'past_call_pos_gate_10': 'VARCHAR(255)',

'past_call_pos_stretch_1': 'VARCHAR(255)',
'past_call_pos_stretch_2': 'VARCHAR(255)',
'past_call_pos_stretch_3': 'VARCHAR(255)',
'past_call_pos_stretch_4': 'VARCHAR(255)',
'past_call_pos_stretch_5': 'VARCHAR(255)',
'past_call_pos_stretch_6': 'VARCHAR(255)',
'past_call_pos_stretch_7': 'VARCHAR(255)',
'past_call_pos_stretch_8': 'VARCHAR(255)',
'past_call_pos_stretch_9': 'VARCHAR(255)',
'past_call_pos_stretch_10': 'VARCHAR(255)',

'past_call_pos_finish_1': 'VARCHAR(255)',
'past_call_pos_finish_2': 'VARCHAR(255)',
'past_call_pos_finish_3': 'VARCHAR(255)',
'past_call_pos_finish_4': 'VARCHAR(255)',
'past_call_pos_finish_5': 'VARCHAR(255)',
'past_call_pos_finish_6': 'VARCHAR(255)',
'past_call_pos_finish_7': 'VARCHAR(255)',
'past_call_pos_finish_8': 'VARCHAR(255)',
'past_call_pos_finish_9': 'VARCHAR(255)',
'past_call_pos_finish_10': 'VARCHAR(255)',

'past_money_pos_1': 'VARCHAR(255)',
'past_money_pos_2': 'VARCHAR(255)',
'past_money_pos_3': 'VARCHAR(255)',
'past_money_pos_4': 'VARCHAR(255)',
'past_money_pos_5': 'VARCHAR(255)',
'past_money_pos_6': 'VARCHAR(255)',
'past_money_pos_7': 'VARCHAR(255)',
'past_money_pos_8': 'VARCHAR(255)',
'past_money_pos_9': 'VARCHAR(255)',
'past_money_pos_10': 'VARCHAR(255)',

##      Start Call - Beaten lengths/Leader margin
'past_lead_margin_start_1': 'FLOAT', ##      636                     99.99           5
'past_lead_margin_start_2': 'FLOAT', ##      637                     99.99           5
'past_lead_margin_start_3': 'FLOAT', ##      638                     99.99           5
'past_lead_margin_start_4': 'FLOAT', ##      639                     99.99           5
'past_lead_margin_start_5': 'FLOAT', ##      640                     99.99           5
'past_lead_margin_start_6': 'FLOAT', ##      641                     99.99           5
'past_lead_margin_start_7': 'FLOAT', ##      642                     99.99           5
'past_lead_margin_start_8': 'FLOAT', ##      643                     99.99           5
'past_lead_margin_start_9': 'FLOAT', ##      644                     99.99           5
'past_lead_margin_start_10': 'FLOAT',##      645                     99.99           5

##      Start Call - Beaten lengths only
'past_beaten_lengths_start_1': 'FLOAT',      ##      646                     99.99           5
'past_beaten_lengths_start_2': 'FLOAT',      ##      647                     99.99           5
'past_beaten_lengths_start_3': 'FLOAT',      ##      648                     99.99           5
'past_beaten_lengths_start_4': 'FLOAT',      ##      649                     99.99           5
'past_beaten_lengths_start_5': 'FLOAT',      ##      650                     99.99           5
'past_beaten_lengths_start_6': 'FLOAT',      ##      651                     99.99           5
'past_beaten_lengths_start_7': 'FLOAT',      ##      652                     99.99           5
'past_beaten_lengths_start_8': 'FLOAT',      ##      653                     99.99           5
'past_beaten_lengths_start_9': 'FLOAT',      ##      654                     99.99           5
'past_beaten_lengths_start_10': 'FLOAT',     ##      655                     99.99           5

##      1st Call Beaten lengths/Leader margin
'past_lead_margin_first_call_1': 'FLOAT',    ##      656                     99.99           5
'past_lead_margin_first_call_2': 'FLOAT',    ##      657                     99.99           5
'past_lead_margin_first_call_3': 'FLOAT',    ##      658                     99.99           5
'past_lead_margin_first_call_4': 'FLOAT',    ##      659                     99.99           5
'past_lead_margin_first_call_5': 'FLOAT',    ##      660                     99.99           5
'past_lead_margin_first_call_6': 'FLOAT',    ##      661                     99.99           5
'past_lead_margin_first_call_7': 'FLOAT',    ##      662                     99.99           5
'past_lead_margin_first_call_8': 'FLOAT',    ##      663                     99.99           5
'past_lead_margin_first_call_9': 'FLOAT',    ##      664                     99.99           5
'past_lead_margin_first_call_10': 'FLOAT',   ##      665                     99.99           5

##      1st Call Beathen lengths only
'past_beaten_lengths_first_call_1': 'FLOAT', ##      666                     99.99           5
'past_beaten_lengths_first_call_2': 'FLOAT', ##      667                     99.99           5
'past_beaten_lengths_first_call_3': 'FLOAT', ##      668                     99.99           5
'past_beaten_lengths_first_call_4': 'FLOAT', ##      669                     99.99           5
'past_beaten_lengths_first_call_5': 'FLOAT', ##      670                     99.99           5
'past_beaten_lengths_first_call_6': 'FLOAT', ##      671                     99.99           5
'past_beaten_lengths_first_call_7': 'FLOAT', ##      672                     99.99           5
'past_beaten_lengths_first_call_8': 'FLOAT', ##      673                     99.99           5
'past_beaten_lengths_first_call_9': 'FLOAT', ##      674                     99.99           5
'past_beaten_lengths_first_call_10': 'FLOAT',##      675                     99.99           5

##      2d Call Beaten Lengths/Leader marbin
'past_lead_margin_second_call_1': 'FLOAT',   ##      676                     99.99           5
'past_lead_margin_second_call_2': 'FLOAT',   ##      677                     99.99           5
'past_lead_margin_second_call_3': 'FLOAT',   ##      678                     99.99           5
'past_lead_margin_second_call_4': 'FLOAT',   ##      679                     99.99           5
'past_lead_margin_second_call_5': 'FLOAT',   ##      680                     99.99           5
'past_lead_margin_second_call_6': 'FLOAT',   ##      681                     99.99           5
'past_lead_margin_second_call_7': 'FLOAT',   ##      682                     99.99           5
'past_lead_margin_second_call_8': 'FLOAT',   ##      683                     99.99           5
'past_lead_margin_second_call_9': 'FLOAT',   ##      684                     99.99           5
'past_lead_margin_second_call_10': 'FLOAT',  ##      685                     99.99           5

##      2d Call Beath lengths only
'past_beaten_lengths_second_call_1': 'FLOAT',    ##      686                     99.99           5
'past_beaten_lengths_second_call_2': 'FLOAT',    ##      687                     99.99           5
'past_beaten_lengths_second_call_3': 'FLOAT',    ##      688                     99.99           5
'past_beaten_lengths_second_call_4': 'FLOAT',    ##      689                     99.99           5
'past_beaten_lengths_second_call_5': 'FLOAT',    ##      690                     99.99           5
'past_beaten_lengths_second_call_6': 'FLOAT',    ##      691                     99.99           5
'past_beaten_lengths_second_call_7': 'FLOAT',    ##      692                     99.99           5
'past_beaten_lengths_second_call_8': 'FLOAT',    ##      693                     99.99           5
'past_beaten_lengths_second_call_9': 'FLOAT',    ##      694                     99.99           5
'past_beaten_lengths_second_call_10': 'FLOAT',   ##      695                     99.99           5

##      BRIS Race Shape- 1st Call
'past_bris_shape_first_call_1': 'INT',         ##      696                     999             3
'past_bris_shape_first_call_2': 'INT',         ##      697                     999             3
'past_bris_shape_first_call_3': 'INT',         ##      698                     999             3
'past_bris_shape_first_call_4': 'INT',         ##      699                     999             3
'past_bris_shape_first_call_5': 'INT',         ##      700                     999             3
'past_bris_shape_first_call_6': 'INT',         ##      701                     999             3
'past_bris_shape_first_call_7': 'INT',         ##      702                     999             3
'past_bris_shape_first_call_8': 'INT',         ##      703                     999             3
'past_bris_shape_first_call_9': 'INT',         ##      704                     999             3
'past_bris_shape_first_call_10': 'INT',        ##      705                     999             3

##      Stretch beaten lengths/leader margin
'past_lead_margin_stretch_call_1': 'FLOAT',      ##      716                     99.99           5
'past_lead_margin_stretch_call_2': 'FLOAT',      ##      717                     99.99           5
'past_lead_margin_stretch_call_3': 'FLOAT',      ##      718                     99.99           5
'past_lead_margin_stretch_call_4': 'FLOAT',      ##      719                     99.99           5
'past_lead_margin_stretch_call_5': 'FLOAT',      ##      720                     99.99           5
'past_lead_margin_stretch_call_6': 'FLOAT',      ##      721                     99.99           5
'past_lead_margin_stretch_call_7': 'FLOAT',      ##      722                     99.99           5
'past_lead_margin_stretch_call_8': 'FLOAT',      ##      723                     99.99           5
'past_lead_margin_stretch_call_9': 'FLOAT',      ##      724                     99.99           5
'past_lead_margin_stretch_call_10': 'FLOAT',     ##      725                     99.99           5

##      Stretch beaten lengths only
'past_beaten_lengths_stretch_call_1': 'FLOAT',   ##      726
'past_beaten_lengths_stretch_call_2': 'FLOAT',   ##      727
'past_beaten_lengths_stretch_call_3': 'FLOAT',   ##      728
'past_beaten_lengths_stretch_call_4': 'FLOAT',   ##      729
'past_beaten_lengths_stretch_call_5': 'FLOAT',   ##      730
'past_beaten_lengths_stretch_call_6': 'FLOAT',   ##      731
'past_beaten_lengths_stretch_call_7': 'FLOAT',   ##      732
'past_beaten_lengths_stretch_call_8': 'FLOAT',   ##      733
'past_beaten_lengths_stretch_call_9': 'FLOAT',   ##      734
'past_beaten_lengths_stretch_call_10': 'FLOAT',  ##      735

## Finish Beaten lengths/leader margin
'past_lead_margin_finish_1': 'FLOAT',            ##      736     NUMERIC         99.99           5
'past_lead_margin_finish_2': 'FLOAT',            ##      737     NUMERIC         99.99           5
'past_lead_margin_finish_3': 'FLOAT',            ##      738     NUMERIC         99.99           5
'past_lead_margin_finish_4': 'FLOAT',            ##      739     NUMERIC         99.99           5
'past_lead_margin_finish_5': 'FLOAT',            ##      740     NUMERIC         99.99           5
'past_lead_margin_finish_6': 'FLOAT',            ##      741     NUMERIC         99.99           5
'past_lead_margin_finish_7': 'FLOAT',            ##      742     NUMERIC         99.99           5
'past_lead_margin_finish_8': 'FLOAT',            ##      743     NUMERIC         99.99           5
'past_lead_margin_finish_9': 'FLOAT',            ##      744     NUMERIC         99.99           5
'past_lead_margin_finish_10': 'FLOAT',           ##      745     NUMERIC         99.99           5

##      Finish beaten lengths only
'past_beaten_lengths_finish_1': 'FLOAT',         ##      746
'past_beaten_lengths_finish_2': 'FLOAT',         ##      747
'past_beaten_lengths_finish_3': 'FLOAT',         ##      748
'past_beaten_lengths_finish_4': 'FLOAT',         ##      749
'past_beaten_lengths_finish_5': 'FLOAT',         ##      750
'past_beaten_lengths_finish_6': 'FLOAT',         ##      751
'past_beaten_lengths_finish_7': 'FLOAT',         ##      752
'past_beaten_lengths_finish_8': 'FLOAT',         ##      753
'past_beaten_lengths_finish_9': 'FLOAT',         ##      754
'past_beaten_lengths_finish_10': 'FLOAT',        ##      755

##      BRIS Race Shape 2d Call
'past_bris_shape_second_call_1': 'INT',        ##      756     NUMERIC         999             3
'past_bris_shape_second_call_2': 'INT',        ##      757     NUMERIC         999             3
'past_bris_shape_second_call_3': 'INT',        ##      758     NUMERIC         999             3
'past_bris_shape_second_call_4': 'INT',        ##      759     NUMERIC         999             3
'past_bris_shape_second_call_5': 'INT',        ##      760     NUMERIC         999             3
'past_bris_shape_second_call_6': 'INT',        ##      761     NUMERIC         999             3
'past_bris_shape_second_call_7': 'INT',        ##      762     NUMERIC         999             3
'past_bris_shape_second_call_8': 'INT',        ##      763     NUMERIC         999             3
'past_bris_shape_second_call_9': 'INT',        ##      764     NUMERIC         999             3
'past_bris_shape_second_call_10': 'INT',       ##      765     NUMERIC         999             3

##      BRIS Pace Figures
'past_bris_pace_2f_1': 'INT',                  ##      766     NUMERIC         999             3
'past_bris_pace_2f_2': 'INT',                  ##      767     NUMERIC         999             3
'past_bris_pace_2f_3': 'INT',                  ##      768     NUMERIC         999             3
'past_bris_pace_2f_4': 'INT',                  ##      769     NUMERIC         999             3
'past_bris_pace_2f_5': 'INT',                  ##      770     NUMERIC         999             3
'past_bris_pace_2f_6': 'INT',                  ##      771     NUMERIC         999             3
'past_bris_pace_2f_7': 'INT',                  ##      772     NUMERIC         999             3
'past_bris_pace_2f_8': 'INT',                  ##      773     NUMERIC         999             3
'past_bris_pace_2f_9': 'INT',                  ##      774     NUMERIC         999             3
'past_bris_pace_2f_10': 'INT',                 ##      775     NUMERIC         999             3

'past_bris_pace_4f_1': 'INT',                  ##      776     NUMERIC         999             3
'past_bris_pace_4f_2': 'INT',                  ##      777     NUMERIC         999             3
'past_bris_pace_4f_3': 'INT',                  ##      778     NUMERIC         999             3
'past_bris_pace_4f_4': 'INT',                  ##      779     NUMERIC         999             3
'past_bris_pace_4f_5': 'INT',                  ##      780     NUMERIC         999             3
'past_bris_pace_4f_6': 'INT',                  ##      781     NUMERIC         999             3
'past_bris_pace_4f_7': 'INT',                  ##      782     NUMERIC         999             3
'past_bris_pace_4f_8': 'INT',                  ##      783     NUMERIC         999             3
'past_bris_pace_4f_9': 'INT',                  ##      784     NUMERIC         999             3
'past_bris_pace_4f_10': 'INT',                 ##      785     NUMERIC         999             3

'past_bris_pace_6f_1': 'INT',                  ##      786     NUMERIC         999             3
'past_bris_pace_6f_2': 'INT',                  ##      787     NUMERIC         999             3
'past_bris_pace_6f_3': 'INT',                  ##      788     NUMERIC         999             3
'past_bris_pace_6f_4': 'INT',                  ##      789     NUMERIC         999             3
'past_bris_pace_6f_5': 'INT',                  ##      790     NUMERIC         999             3
'past_bris_pace_6f_6': 'INT',                  ##      791     NUMERIC         999             3
'past_bris_pace_6f_7': 'INT',                  ##      792     NUMERIC         999             3
'past_bris_pace_6f_8': 'INT',                  ##      793     NUMERIC         999             3
'past_bris_pace_6f_9': 'INT',                  ##      794     NUMERIC         999             3
'past_bris_pace_6f_10': 'INT',                 ##      795     NUMERIC         999             3

'past_bris_pace_8f_1': 'INT',                  ##      796     NUMERIC         999             3
'past_bris_pace_8f_2': 'INT',                  ##      797     NUMERIC         999             3
'past_bris_pace_8f_3': 'INT',                  ##      798     NUMERIC         999             3
'past_bris_pace_8f_4': 'INT',                  ##      799     NUMERIC         999             3
'past_bris_pace_8f_5': 'INT',                  ##      800     NUMERIC         999             3
'past_bris_pace_8f_6': 'INT',                  ##      801     NUMERIC         999             3
'past_bris_pace_8f_7': 'INT',                  ##      802     NUMERIC         999             3
'past_bris_pace_8f_8': 'INT',                  ##      803     NUMERIC         999             3
'past_bris_pace_8f_9': 'INT',                  ##      804     NUMERIC         999             3
'past_bris_pace_8f_10': 'INT',                 ##      805     NUMERIC         999             3

'past_bris_pace_10f_1': 'INT',                 ##      806     NUMERIC         999             3
'past_bris_pace_10f_2': 'INT',                 ##      809     NUMERIC         999             3
'past_bris_pace_10f_3': 'INT',                 ##      808     NUMERIC         999             3
'past_bris_pace_10f_4': 'INT',                 ##      809     NUMERIC         999             3
'past_bris_pace_10f_5': 'INT',                 ##      810     NUMERIC         999             3
'past_bris_pace_10f_6': 'INT',                 ##      811     NUMERIC         999             3
'past_bris_pace_10f_7': 'INT',                 ##      812     NUMERIC         999             3
'past_bris_pace_10f_8': 'INT',                 ##      813     NUMERIC         999             3
'past_bris_pace_10f_9': 'INT',                 ##      814     NUMERIC         999             3
'past_bris_pace_10f_10': 'INT',                ##      815     NUMERIC         999             3

'past_bris_pace_late_1': 'INT',                ##      816     NUMERIC         999             3
'past_bris_pace_late_2': 'INT',                ##      817     NUMERIC         999             3
'past_bris_pace_late_3': 'INT',                ##      818     NUMERIC         999             3
'past_bris_pace_late_4': 'INT',                ##      819     NUMERIC         999             3
'past_bris_pace_late_5': 'INT',                ##      820     NUMERIC         999             3
'past_bris_pace_late_6': 'INT',                ##      821     NUMERIC         999             3
'past_bris_pace_late_7': 'INT',                ##      822     NUMERIC         999             3
'past_bris_pace_late_8': 'INT',                ##      823     NUMERIC         999             3
'past_bris_pace_late_9': 'INT',                ##      824     NUMERIC         999             3
'past_bris_pace_late_10': 'INT',               ##      825     NUMERIC         999             3

#      BRIS Speed Rating
'past_bris_speed_rating_1': 'INT',         ##      846     NUMERIC         999     3
'past_bris_speed_rating_2': 'INT',         ##      847     NUMERIC         999     3
'past_bris_speed_rating_3': 'INT',         ##      848     NUMERIC         999     3
'past_bris_speed_rating_4': 'INT',         ##      849     NUMERIC         999     3
'past_bris_speed_rating_5': 'INT',         ##      850     NUMERIC         999     3
'past_bris_speed_rating_6': 'INT',         ##      851     NUMERIC         999     3
'past_bris_speed_rating_7': 'INT',         ##      852     NUMERIC         999     3
'past_bris_speed_rating_8': 'INT',         ##      853     NUMERIC         999     3
'past_bris_speed_rating_9': 'INT',         ##      854     NUMERIC         999     3
'past_bris_speed_rating_10': 'INT',        ##      855     NUMERIC         999     3

##      Speed rating
'past_speed_rating_1': 'INT',              ##      856     NUMERIC         999     3
'past_speed_rating_2': 'INT',              ##      857     NUMERIC         999     3
'past_speed_rating_3': 'INT',              ##      858     NUMERIC         999     3
'past_speed_rating_4': 'INT',              ##      859     NUMERIC         999     3
'past_speed_rating_5': 'INT',              ##      860     NUMERIC         999     3
'past_speed_rating_6': 'INT',              ##      861     NUMERIC         999     3
'past_speed_rating_7': 'INT',              ##      862     NUMERIC         999     3
'past_speed_rating_8': 'INT',              ##      863     NUMERIC         999     3
'past_speed_rating_9': 'INT',              ##      864     NUMERIC         999     3
'past_speed_rating_10': 'INT',             ##      865     NUMERIC         999     3

##      Track Variant
'past_track_variant_1': 'INT',             ##      866     NUMERIC         99      2
'past_track_variant_2': 'INT',             ##      867     NUMERIC         99      2
'past_track_variant_3': 'INT',             ##      868     NUMERIC         99      2
'past_track_variant_4': 'INT',             ##      869     NUMERIC         99      2
'past_track_variant_5': 'INT',             ##      870     NUMERIC         99      2
'past_track_variant_6': 'INT',             ##      871     NUMERIC         99      2
'past_track_variant_7': 'INT',             ##      872     NUMERIC         99      2
'past_track_variant_8': 'INT',             ##      873     NUMERIC         99      2
'past_track_variant_9': 'INT',             ##      874     NUMERIC         99      2
'past_track_variant_10': 'INT',            ##      875     NUMERIC         99      2

## Past Fractions (seconds and hundreths)

'past_fraction_2f_1': 'FLOAT',               ##      876     NUMERIC         999.99  6       Seconds & Hundreths
'past_fraction_2f_2': 'FLOAT',               ##      877     NUMERIC         999.99  6
'past_fraction_2f_3': 'FLOAT',               ##      878     NUMERIC         999.99  6
'past_fraction_2f_4': 'FLOAT',               ##      879     NUMERIC         999.99  6
'past_fraction_2f_5': 'FLOAT',               ##      880     NUMERIC         999.99  6
'past_fraction_2f_6': 'FLOAT',               ##      881     NUMERIC         999.99  6
'past_fraction_2f_7': 'FLOAT',               ##      882     NUMERIC         999.99  6
'past_fraction_2f_8': 'FLOAT',               ##      883     NUMERIC         999.99  6
'past_fraction_2f_9': 'FLOAT',               ##      884     NUMERIC         999.99  6
'past_fraction_2f_10': 'FLOAT',              ##      885     NUMERIC         999.99  6

'past_fraction_3f_1': 'FLOAT',               ##      886     NUMERIC         999.99  6
'past_fraction_3f_2': 'FLOAT',               ##      887     NUMERIC         999.99  6
'past_fraction_3f_3': 'FLOAT',               ##      888     NUMERIC         999.99  6
'past_fraction_3f_4': 'FLOAT',               ##      889     NUMERIC         999.99  6
'past_fraction_3f_5': 'FLOAT',               ##      890     NUMERIC         999.99  6
'past_fraction_3f_6': 'FLOAT',               ##      891     NUMERIC         999.99  6
'past_fraction_3f_7': 'FLOAT',               ##      892     NUMERIC         999.99  6
'past_fraction_3f_8': 'FLOAT',               ##      893     NUMERIC         999.99  6
'past_fraction_3f_9': 'FLOAT',               ##      894     NUMERIC         999.99  6
'past_fraction_3f_10': 'FLOAT',              ##      895     NUMERIC         999.99  6

'past_fraction_4f_1': 'FLOAT',               ##      896     NUMERIC         999.99  6
'past_fraction_4f_2': 'FLOAT',               ##      897     NUMERIC         999.99  6
'past_fraction_4f_3': 'FLOAT',               ##      898     NUMERIC         999.99  6
'past_fraction_4f_4': 'FLOAT',               ##      899     NUMERIC         999.99  6
'past_fraction_4f_5': 'FLOAT',               ##      900     NUMERIC         999.99  6
'past_fraction_4f_6': 'FLOAT',               ##      901     NUMERIC         999.99  6
'past_fraction_4f_7': 'FLOAT',               ##      902     NUMERIC         999.99  6
'past_fraction_4f_8': 'FLOAT',               ##      903     NUMERIC         999.99  6
'past_fraction_4f_9': 'FLOAT',               ##      904     NUMERIC         999.99  6
'past_fraction_4f_10': 'FLOAT',              ##      905     NUMERIC         999.99  6

'past_fraction_5f_1': 'FLOAT',               ##      906     NUMERIC         999.99  6
'past_fraction_5f_2': 'FLOAT',               ##      907     NUMERIC         999.99  6
'past_fraction_5f_3': 'FLOAT',               ##      908     NUMERIC         999.99  6
'past_fraction_5f_4': 'FLOAT',               ##      909     NUMERIC         999.99  6
'past_fraction_5f_5': 'FLOAT',               ##      910     NUMERIC         999.99  6
'past_fraction_5f_6': 'FLOAT',               ##      911     NUMERIC         999.99  6
'past_fraction_5f_7': 'FLOAT',               ##      912     NUMERIC         999.99  6
'past_fraction_5f_8': 'FLOAT',               ##      913     NUMERIC         999.99  6
'past_fraction_5f_9': 'FLOAT',               ##      914     NUMERIC         999.99  6
'past_fraction_5f_10': 'FLOAT',              ##      915     NUMERIC         999.99  6

'past_fraction_6f_1': 'FLOAT',               ##      916     NUMERIC         999.99  6
'past_fraction_6f_2': 'FLOAT',               ##      917     NUMERIC         999.99  6
'past_fraction_6f_3': 'FLOAT',               ##      918     NUMERIC         999.99  6
'past_fraction_6f_4': 'FLOAT',               ##      919     NUMERIC         999.99  6
'past_fraction_6f_5': 'FLOAT',               ##      920     NUMERIC         999.99  6
'past_fraction_6f_6': 'FLOAT',               ##      921     NUMERIC         999.99  6
'past_fraction_6f_7': 'FLOAT',               ##      922     NUMERIC         999.99  6
'past_fraction_6f_8': 'FLOAT',               ##      923     NUMERIC         999.99  6
'past_fraction_6f_9': 'FLOAT',               ##      924     NUMERIC         999.99  6
'past_fraction_6f_10': 'FLOAT',              ##      925     NUMERIC         999.99  6

'past_fraction_7f_1': 'FLOAT',               ##      926     NUMERIC         999.99  6
'past_fraction_7f_2': 'FLOAT',               ##      927     NUMERIC         999.99  6
'past_fraction_7f_3': 'FLOAT',               ##      928     NUMERIC         999.99  6
'past_fraction_7f_4': 'FLOAT',               ##      929     NUMERIC         999.99  6
'past_fraction_7f_5': 'FLOAT',               ##      930     NUMERIC         999.99  6
'past_fraction_7f_6': 'FLOAT',               ##      931     NUMERIC         999.99  6
'past_fraction_7f_7': 'FLOAT',               ##      932     NUMERIC         999.99  6
'past_fraction_7f_8': 'FLOAT',               ##      933     NUMERIC         999.99  6
'past_fraction_7f_9': 'FLOAT',               ##      934     NUMERIC         999.99  6
'past_fraction_7f_10': 'FLOAT',              ##      935     NUMERIC         999.99  6

'past_fraction_8f_1': 'FLOAT',               ##      936     NUMERIC         999.99  6
'past_fraction_8f_2': 'FLOAT',               ##      937     NUMERIC         999.99  6
'past_fraction_8f_3': 'FLOAT',               ##      938     NUMERIC         999.99  6
'past_fraction_8f_4': 'FLOAT',               ##      939     NUMERIC         999.99  6
'past_fraction_8f_5': 'FLOAT',               ##      940     NUMERIC         999.99  6
'past_fraction_8f_6': 'FLOAT',               ##      941     NUMERIC         999.99  6
'past_fraction_8f_7': 'FLOAT',               ##      942     NUMERIC         999.99  6
'past_fraction_8f_8': 'FLOAT',               ##      943     NUMERIC         999.99  6
'past_fraction_8f_9': 'FLOAT',               ##      944     NUMERIC         999.99  6
'past_fraction_8f_10': 'FLOAT',              ##      945     NUMERIC         999.99  6

'past_fraction_10f_1': 'FLOAT',              ##      946     NUMERIC         999.99  6
'past_fraction_10f_2': 'FLOAT',              ##      947     NUMERIC         999.99  6
'past_fraction_10f_3': 'FLOAT',              ##      948     NUMERIC         999.99  6
'past_fraction_10f_4': 'FLOAT',              ##      949     NUMERIC         999.99  6
'past_fraction_10f_5': 'FLOAT',              ##      950     NUMERIC         999.99  6
'past_fraction_10f_6': 'FLOAT',              ##      951     NUMERIC         999.99  6
'past_fraction_10f_7': 'FLOAT',              ##      952     NUMERIC         999.99  6
'past_fraction_10f_8': 'FLOAT',              ##      953     NUMERIC         999.99  6
'past_fraction_10f_9': 'FLOAT',              ##      954     NUMERIC         999.99  6
'past_fraction_10f_10': 'FLOAT',             ##      955     NUMERIC         999.99  6

'past_fraction_12f_1': 'FLOAT',              ##      956     NUMERIC         999.99  6
'past_fraction_12f_2': 'FLOAT',              ##      957     NUMERIC         999.99  6
'past_fraction_12f_3': 'FLOAT',              ##      958     NUMERIC         999.99  6
'past_fraction_12f_4': 'FLOAT',              ##      959     NUMERIC         999.99  6
'past_fraction_12f_5': 'FLOAT',              ##      960     NUMERIC         999.99  6
'past_fraction_12f_6': 'FLOAT',              ##      961     NUMERIC         999.99  6
'past_fraction_12f_7': 'FLOAT',              ##      962     NUMERIC         999.99  6
'past_fraction_12f_8': 'FLOAT',              ##      963     NUMERIC         999.99  6
'past_fraction_12f_9': 'FLOAT',              ##      964     NUMERIC         999.99  6
'past_fraction_12f_10': 'FLOAT',             ##      965     NUMERIC         999.99  6

'past_fraction_14f_1': 'FLOAT',              ##      966     NUMERIC         999.99  6
'past_fraction_14f_2': 'FLOAT',              ##      967     NUMERIC         999.99  6
'past_fraction_14f_3': 'FLOAT',              ##      968     NUMERIC         999.99  6
'past_fraction_14f_4': 'FLOAT',              ##      969     NUMERIC         999.99  6
'past_fraction_14f_5': 'FLOAT',              ##      970     NUMERIC         999.99  6
'past_fraction_14f_6': 'FLOAT',              ##      971     NUMERIC         999.99  6
'past_fraction_14f_7': 'FLOAT',              ##      972     NUMERIC         999.99  6
'past_fraction_14f_8': 'FLOAT',              ##      973     NUMERIC         999.99  6
'past_fraction_14f_9': 'FLOAT',              ##      974     NUMERIC         999.99  6
'past_fraction_14f_10': 'FLOAT',             ##      975     NUMERIC         999.99  6

'past_fraction_16f_1': 'FLOAT',              ##      976     NUMERIC         999.99  6
'past_fraction_16f_2': 'FLOAT',              ##      977     NUMERIC         999.99  6
'past_fraction_16f_3': 'FLOAT',              ##      978     NUMERIC         999.99  6
'past_fraction_16f_4': 'FLOAT',              ##      979     NUMERIC         999.99  6
'past_fraction_16f_5': 'FLOAT',              ##      980     NUMERIC         999.99  6
'past_fraction_16f_6': 'FLOAT',              ##      981     NUMERIC         999.99  6
'past_fraction_16f_7': 'FLOAT',              ##      982     NUMERIC         999.99  6
'past_fraction_16f_8': 'FLOAT',              ##      983     NUMERIC         999.99  6
'past_fraction_16f_9': 'FLOAT',              ##      984     NUMERIC         999.99  6
'past_fraction_16f_10': 'FLOAT',             ##      985     NUMERIC         999.99  6

 ##     Fractions #1, #2, #3
'past_fraction_first_1': 'FLOAT',            ##      986     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_2': 'FLOAT',            ##      987     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_3': 'FLOAT',            ##      988     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_4': 'FLOAT',            ##      989     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_5': 'FLOAT',            ##      990     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_6': 'FLOAT',            ##      991     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_7': 'FLOAT',            ##      992     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_8': 'FLOAT',            ##      993     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_9': 'FLOAT',            ##      994     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_first_10': 'FLOAT',           ##      995     NUMERIC         999.99  6       Seconds and hundreths

'past_fraction_second_1': 'FLOAT',           ##      996     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_2': 'FLOAT',           ##      997     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_3': 'FLOAT',           ##      998     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_4': 'FLOAT',           ##      999     NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_5': 'FLOAT',           ##      1000    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_6': 'FLOAT',           ##      1001    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_7': 'FLOAT',           ##      1002    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_8': 'FLOAT',           ##      1003    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_9': 'FLOAT',           ##      1004    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_second_10': 'FLOAT',          ##      1005    NUMERIC         999.99  6       Seconds and hundreths

'past_fraction_third_1': 'FLOAT',            ##      1006    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_2': 'FLOAT',            ##      1007    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_3': 'FLOAT',            ##      1008    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_4': 'FLOAT',            ##      1009    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_5': 'FLOAT',            ##      1010    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_6': 'FLOAT',            ##      1011    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_7': 'FLOAT',            ##      1012    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_8': 'FLOAT',            ##      1013    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_9': 'FLOAT',            ##      1014    NUMERIC         999.99  6       Seconds and hundreths
'past_fraction_third_10': 'FLOAT',           ##      1015    NUMERIC         999.99  6       Seconds and hundreths

#      Final time
'past_final_time_1': 'FLOAT',                ##      1036    NUMERIC         999.99  6       Seconds and hundreths
'past_final_time_2': 'FLOAT',                ##      1037    NUMERIC         999.99  6
'past_final_time_3': 'FLOAT',                ##      1038    NUMERIC         999.99  6
'past_final_time_4': 'FLOAT',                ##      1039    NUMERIC         999.99  6
'past_final_time_5': 'FLOAT',                ##      1040    NUMERIC         999.99  6
'past_final_time_6': 'FLOAT',                ##      1041    NUMERIC         999.99  6
'past_final_time_7': 'FLOAT',                ##      1042    NUMERIC         999.99  6
'past_final_time_8': 'FLOAT',                ##      1043    NUMERIC         999.99  6
'past_final_time_9': 'FLOAT',                ##      1044    NUMERIC         999.99  6
'past_final_time_10': 'FLOAT',               ##      1045    NUMERIC         999.99  6

#      Claimed code
'past_claimed_code_1': 'VARCHAR(255)',              ##      1046    CHARACTER       X       1       c- claimed
'past_claimed_code_2': 'VARCHAR(255)',              ##      1047    CHARACTER       X       1
'past_claimed_code_3': 'VARCHAR(255)',              ##      1048    CHARACTER       X       1
'past_claimed_code_4': 'VARCHAR(255)',              ##      1049    CHARACTER       X       1
'past_claimed_code_5': 'VARCHAR(255)',              ##      1050    CHARACTER       X       1
'past_claimed_code_6': 'VARCHAR(255)',              ##      1051    CHARACTER       X       1
'past_claimed_code_7': 'VARCHAR(255)',              ##      1052    CHARACTER       X       1
'past_claimed_code_8': 'VARCHAR(255)',              ##      1053    CHARACTER       X       1
'past_claimed_code_9': 'VARCHAR(255)',              ##      1054    CHARACTER       X       1
'past_claimed_code_10': 'VARCHAR(255)',             ##      1055    CHARACTER       X       1

##      Past Trainer (when available) and Jockey
'past_trainer_1': 'VARCHAR(255)',                   ##      1056    CHARACTER       X       30
'past_trainer_2': 'VARCHAR(255)',                   ##      1057    CHARACTER       X       30
'past_trainer_3': 'VARCHAR(255)',                   ##      1058    CHARACTER       X       30
'past_trainer_4': 'VARCHAR(255)',                   ##      1059    CHARACTER       X       30
'past_trainer_5': 'VARCHAR(255)',                   ##      1060    CHARACTER       X       30
'past_trainer_6': 'VARCHAR(255)',                   ##      1061    CHARACTER       X       30
'past_trainer_7': 'VARCHAR(255)',                   ##      1062    CHARACTER       X       30
'past_trainer_8': 'VARCHAR(255)',                   ##      1063    CHARACTER       X       30
'past_trainer_9': 'VARCHAR(255)',                   ##      1064    CHARACTER       X       30
'past_trainer_10': 'VARCHAR(255)',                  ##      1065    CHARACTER       X       30

'past_jockey_1': 'VARCHAR(255)',                    ##      1066    CHARACTER       X       30
'past_jockey_2': 'VARCHAR(255)',                    ##      1067    CHARACTER       X       30
'past_jockey_3': 'VARCHAR(255)',                    ##      1068    CHARACTER       X       30
'past_jockey_4': 'VARCHAR(255)',                    ##      1069    CHARACTER       X       30
'past_jockey_5': 'VARCHAR(255)',                    ##      1070    CHARACTER       X       30
'past_jockey_6': 'VARCHAR(255)',                    ##      1071    CHARACTER       X       30
'past_jockey_7': 'VARCHAR(255)',                    ##      1072    CHARACTER       X       30
'past_jockey_8': 'VARCHAR(255)',                    ##      1073    CHARACTER       X       30
'past_jockey_9': 'VARCHAR(255)',                    ##      1074    CHARACTER       X       30
'past_jockey_10': 'VARCHAR(255)',                   ##      1075    CHARACTER       X       30

##      Apprentice weight allowance (if any)
'past_weight_allowance_1': 'INT',          ##      1076    NUMERIC         99      2
'past_weight_allowance_2': 'INT',          ##      1077    NUMERIC         99      2
'past_weight_allowance_3': 'INT',          ##      1078    NUMERIC         99      2
'past_weight_allowance_4': 'INT',          ##      1079    NUMERIC         99      2
'past_weight_allowance_5': 'INT',          ##      1080    NUMERIC         99      2
'past_weight_allowance_6': 'INT',          ##      1081    NUMERIC         99      2
'past_weight_allowance_7': 'INT',          ##      1082    NUMERIC         99      2
'past_weight_allowance_8': 'INT',          ##      1083    NUMERIC         99      2
'past_weight_allowance_9': 'INT',          ##      1084    NUMERIC         99      2
'past_weight_allowance_10': 'INT',         ##      1085    NUMERIC         99      2

##      Race type
'past_race_type_1': 'VARCHAR(255)',                 ##      1086    CHARACTER       XX      2       (G1, G2, G3, N, A, R, T, C,
'past_race_type_2': 'VARCHAR(255)',                 ##      1087    CHARACTER       XX      2       CO, S, M, AO, MO, NO)
'past_race_type_3': 'VARCHAR(255)',                 ##      1088    CHARACTER       XX      2       See field #9
'past_race_type_4': 'VARCHAR(255)',                 ##      1089    CHARACTER       XX      2
'past_race_type_5': 'VARCHAR(255)',                 ##      1090    CHARACTER       XX      2
'past_race_type_6': 'VARCHAR(255)',                 ##      1091    CHARACTER       XX      2       Age/Sex Restrictions
'past_race_type_7': 'VARCHAR(255)',                 ##      1092    CHARACTER       XX      2       (3 character sting):
'past_race_type_8': 'VARCHAR(255)',                 ##      1093    CHARACTER       XX      2       1st character:
'past_race_type_9': 'VARCHAR(255)',                 ##      1094    CHARACTER       XX      2       A- 2 year olds
'past_race_type_10': 'VARCHAR(255)',                ##      1095    CHARACTER       XX      2       B- 3 year olds
                                    ##                                              C- 4 year olds
##      Age and sex restrictions                                                    D- 5 year olds
'past_age_sex_restrictions_1': 'VARCHAR(255)',      ##      1096    CHARACTER       XXX     3       E- 3 & 4 year olds
'past_age_sex_restrictions_2': 'VARCHAR(255)',      ##      1097    CHARACTER       XXX     3       F- 4 & 5 year olds
'past_age_sex_restrictions_3': 'VARCHAR(255)',      ##      1098    CHARACTER       XXX     3       G- 3, 4, & 5 year olds
'past_age_sex_restrictions_4': 'VARCHAR(255)',      ##      1099    CHARACTER       XXX     3       H- all ages
'past_age_sex_restrictions_5': 'VARCHAR(255)',      ##      1100    CHARACTER       XXX     3
'past_age_sex_restrictions_6': 'VARCHAR(255)',      ##      1101    CHARACTER       XXX     3       2d Character:
'past_age_sex_restrictions_7': 'VARCHAR(255)',      ##      1102    CHARACTER       XXX     3       O- That age only
'past_age_sex_restrictions_8': 'VARCHAR(255)',      ##      1103    CHARACTER       XXX     3       U- That age and up
'past_age_sex_restrictions_9': 'VARCHAR(255)',      ##      1104    CHARACTER       XXX     3
'past_age_sex_restrictions_10': 'VARCHAR(255)',     ##      1105    CHARACTER       XXX     3       3d character
                                    ##                                              N - No Sex Restrictions
                                    ##                                              M - Mares and Fillies Only
                                    ##                                              C - Colts or Geldings Only
                                    ##                                              F - Fillies Only
                                    ##      E.g.: 'BON' - means a '3 year olds only,'  no sex restrictions

##      Statebred flag
'past_statebred_flag_1': 'VARCHAR(255)',            ##      1106    CHARACTER       X       1       s- Statebred
'past_statebred_flag_2': 'VARCHAR(255)',            ##      1107    CHARACTER       X       1
'past_statebred_flag_3': 'VARCHAR(255)',            ##      1108    CHARACTER       X       1
'past_statebred_flag_4': 'VARCHAR(255)',            ##      1109    CHARACTER       X       1
'past_statebred_flag_5': 'VARCHAR(255)',            ##      1110    CHARACTER       X       1
'past_statebred_flag_6': 'VARCHAR(255)',            ##      1111    CHARACTER       X       1
'past_statebred_flag_7': 'VARCHAR(255)',            ##      1112    CHARACTER       X       1
'past_statebred_flag_8': 'VARCHAR(255)',            ##      1113    CHARACTER       X       1
'past_statebred_flag_9': 'VARCHAR(255)',            ##      1114    CHARACTER       X       1
'past_statebred_flag_10': 'VARCHAR(255)',           ##      1115    CHARACTER       X       1

##      Restricted/Qualified flag
'past_restricted_or_qualified_1': 'VARCHAR(255)',   ##      1116    CHARACTER       X       R- restrcited
'past_restricted_or_qualified_2': 'VARCHAR(255)',   ##      1117    CHARACTER       X       Q- Qualifier
'past_restricted_or_qualified_3': 'VARCHAR(255)',   ##      1118    CHARACTER       X       O- Optional claimer
'past_restricted_or_qualified_4': 'VARCHAR(255)',   ##      1119    CHARACTER       X
'past_restricted_or_qualified_5': 'VARCHAR(255)',   ##      1120    CHARACTER       X
'past_restricted_or_qualified_6': 'VARCHAR(255)',   ##      1121    CHARACTER       X
'past_restricted_or_qualified_7': 'VARCHAR(255)',   ##      1122    CHARACTER       X
'past_restricted_or_qualified_8': 'VARCHAR(255)',   ##      1123    CHARACTER       X
'past_restricted_or_qualified_9': 'VARCHAR(255)',   ##      1124    CHARACTER       X
'past_restricted_or_qualified_10': 'VARCHAR(255)',  ##      1125    CHARACTER       X

##      Favorite indicator
'past_favorite_flag_1': 'INT',             ##      1126    NUMERIC         X       0- Non-favorite
'past_favorite_flag_2': 'INT',             ##      1127    NUMERIC         X       1- Favorite
'past_favorite_flag_3': 'INT',             ##      1128    NUMERIC         X
'past_favorite_flag_4': 'INT',             ##      1129    NUMERIC         X
'past_favorite_flag_5': 'INT',             ##      1130    NUMERIC         X
'past_favorite_flag_6': 'INT',             ##      1131    NUMERIC         X
'past_favorite_flag_7': 'INT',             ##      1132    NUMERIC         X
'past_favorite_flag_8': 'INT',             ##      1133    NUMERIC         X
'past_favorite_flag_9': 'INT',             ##      1134    NUMERIC         X
'past_favorite_flag_10': 'INT',            ##      1135    NUMERIC         X

##      Front bandages indicator
'past_front_wraps_1': 'INT',               ##      1136    NUMERIC         X       0- No front wraps
'past_front_wraps_2': 'INT',               ##      1137    NUMERIC         X       1- Front wraps
'past_front_wraps_3': 'INT',               ##      1138    NUMERIC         X
'past_front_wraps_4': 'INT',               ##      1139    NUMERIC         X
'past_front_wraps_5': 'INT',               ##      1140    NUMERIC         X
'past_front_wraps_6': 'INT',               ##      1141    NUMERIC         X
'past_front_wraps_7': 'INT',               ##      1142    NUMERIC         X
'past_front_wraps_8': 'INT',               ##      1143    NUMERIC         X
'past_front_wraps_9': 'INT',               ##      1144    NUMERIC         X
'past_front_wraps_10': 'INT',              ##      1145    NUMERIC         X

##      Trainer and Jockey stats Current/Past Year
'trainer_current_year_starts': 'INT',      ##      1147    NUMERIC         9999    4
'trainer_current_year_wins': 'INT',        ##      1148
'trainer_current_year_places': 'INT',      ##      1149
'trainer_current_year_shows': 'INT',       ##      1150
'trainer_current_year_roi': 'FLOAT',         ##      1151    NUMERIC         999.99  6
'trainer_past_year_starts': 'INT',         ##      1152    NUMERIC         9999    4
'trainer_past_year_wins': 'INT',           ##      1153
'trainer_past_year_places': 'INT',         ##      1154
'trainer_past_year_shows': 'INT',          ##      1155
'trainer_past_year_roi': 'FLOAT',            ##      1156    NUMERIC         999.99  6
'jockey_current_year_starts': 'INT',       ##      1157    NUMERIC         9999    4
'jockey_current_year_wins': 'INT',         ##      1158    NUMERIC
'jockey_current_year_places': 'INT',       ##      1159    NUMERIC
'jockey_current_year_shows': 'INT',        ##      1160    NUMERIC
'jockey_current_year_roi': 'FLOAT',          ##      1161    NUMERIC         999.99  6
'jockey_past_year_starts': 'INT',          ##      1162    NUMERIC         9999    4
'jockey_past_year_wins': 'INT',            ##      1163    NUMERIC
'jockey_past_year_places': 'INT',          ##      1164    NUMERIC
'jockey_past_year_shows': 'INT',           ##      1165    NUMERIC
'jockey_past_year_roi': 'FLOAT',             ##      1166    NUMERIC         999.99  6

##      BRIS Speed Par for Class Level of last 10 races
'past_bris_par_for_class_1': 'INT',        ##      1167                            3
'past_bris_par_for_class_2': 'INT',        ##      1168                            3
'past_bris_par_for_class_3': 'INT',        ##      1169                            3
'past_bris_par_for_class_4': 'INT',        ##      1170                            3
'past_bris_par_for_class_5': 'INT',        ##      1171                            3
'past_bris_par_for_class_6': 'INT',        ##      1172                            3
'past_bris_par_for_class_7': 'INT',        ##      1173                            3
'past_bris_par_for_class_8': 'INT',        ##      1174                            3
'past_bris_par_for_class_9': 'INT',        ##      1175                            3
'past_bris_par_for_class_10': 'INT',       ##      1176                            3

##      Sire stud fee (current)
'sire_stud_fee_current': 'INT',            ##      1177    NUMERIC         9999999 7

##      Best BRIS Speeds
'best_bris_speed_fast': 'INT',             ##      1178    NUMERIC         999     3
'best_bris_speed_turf': 'INT',             ##      1179    NUMERIC         999     3
'best_bris_speed_off_track': 'INT',        ##      1180    NUMERIC         999     3
'best_bris_speed__at_distance': 'INT',     ##      1181    NUMERIC         999     3

## Bar Shoe WHAT DOES THIS MEAN?
'past_bar_shoe_1': 'INT',                  ##      1182    CHARACTER       X       1       r- bar shoe
'past_bar_shoe_2': 'INT',                  ##      1183    CHARACTER       X       1
'past_bar_shoe_3': 'INT',                  ##      1184    CHARACTER       X       1
'past_bar_shoe_4': 'INT',                  ##      1185    CHARACTER       X       1
'past_bar_shoe_5': 'INT',                  ##      1186    CHARACTER       X       1
'past_bar_shoe_6': 'INT',                  ##      1187    CHARACTER       X       1
'past_bar_shoe_7': 'INT',                  ##      1188    CHARACTER       X       1
'past_bar_shoe_8': 'INT',                  ##      1189    CHARACTER       X       1
'past_bar_shoe_9': 'INT',                  ##      1190    CHARACTER       X       1
'past_bar_shoe_10': 'INT',                 ##      1191    CHARACTER       X       1

##      Company line codes
'past_company_line_1': 'VARCHAR(255)',              ##      1192    CHARACTER       XXXX    4
'past_company_line_2': 'VARCHAR(255)',              ##      1193    CHARACTER       XXXX    4
'past_company_line_3': 'VARCHAR(255)',              ##      1194    CHARACTER       XXXX    4
'past_company_line_4': 'VARCHAR(255)',              ##      1195    CHARACTER       XXXX    4
'past_company_line_5': 'VARCHAR(255)',              ##      1196    CHARACTER       XXXX    4
'past_company_line_6': 'VARCHAR(255)',              ##      1197    CHARACTER       XXXX    4
'past_company_line_7': 'VARCHAR(255)',              ##      1198    CHARACTER       XXXX    4
'past_company_line_8': 'VARCHAR(255)',              ##      1199    CHARACTER       XXXX    4
'past_company_line_9': 'VARCHAR(255)',              ##      1200    CHARACTER       XXXX    4
'past_company_line_10': 'VARCHAR(255)',             ##      1201    CHARACTER       XXXX    4

##      High and Low claiming price of race
'past_low_claiming_price_1': 'INT',        ##      1202    NUMERIC         9999999 7
'past_low_claiming_price_2': 'INT',        ##      1203    NUMERIC         9999999 7
'past_low_claiming_price_3': 'INT',        ##      1204    NUMERIC         9999999 7
'past_low_claiming_price_4': 'INT',        ##      1205    NUMERIC         9999999 7
'past_low_claiming_price_5': 'INT',        ##      1206    NUMERIC         9999999 7
'past_low_claiming_price_6': 'INT',        ##      1207    NUMERIC         9999999 7
'past_low_claiming_price_7': 'INT',        ##      1208    NUMERIC         9999999 7
'past_low_claiming_price_8': 'INT',        ##      1209    NUMERIC         9999999 7
'past_low_claiming_price_9': 'INT',        ##      1210    NUMERIC         9999999 7
'past_low_claiming_price_10': 'INT',       ##      1211    NUMERIC         9999999 7

'past_high_claiming_price_1': 'INT',       ##      1212    NUMERIC         9999999 7
'past_high_claiming_price_2': 'INT',       ##      1213    NUMERIC         9999999 7
'past_high_claiming_price_3': 'INT',       ##      1214    NUMERIC         9999999 7
'past_high_claiming_price_4': 'INT',       ##      1215    NUMERIC         9999999 7
'past_high_claiming_price_5': 'INT',       ##      1216    NUMERIC         9999999 7
'past_high_claiming_price_6': 'INT',       ##      1217    NUMERIC         9999999 7
'past_high_claiming_price_7': 'INT',       ##      1218    NUMERIC         9999999 7
'past_high_claiming_price_8': 'INT',       ##      1219    NUMERIC         9999999 7
'past_high_claiming_price_9': 'INT',       ##      1220    NUMERIC         9999999 7
'past_high_claiming_price_10': 'INT',      ##      1221    NUMERIC         9999999 7

##      Aution price and when/when sold at auction
'auction_price': 'INT',                    ##      1222    NUMERIC         999999999       9
'auction_where_when': 'VARCHAR(255)',               ##      1223    CHARACTER       X(12)           12

##      Code for prior 10 starts
'past_start_code_1': 'VARCHAR(255)',                ##      1254                                    1       's'- Nasal strip
'past_start_code_2': 'VARCHAR(255)',                ##      1255                                    1       'x'- Off the turf
'past_start_code_3': 'VARCHAR(255)',                ##      1256                                    1
'past_start_code_4': 'VARCHAR(255)',                ##      1257                                    1
'past_start_code_5': 'VARCHAR(255)',                ##      1258                                    1
'past_start_code_6': 'VARCHAR(255)',                ##      1259                                    1
'past_start_code_7': 'VARCHAR(255)',                ##      1260                                    1
'past_start_code_8': 'VARCHAR(255)',                ##      1261                                    1
'past_start_code_9': 'VARCHAR(255)',                ##      1262                                    1
'past_start_code_10': 'VARCHAR(255)',               ##      1263                                    1

##      BRIS Pedigree Ratings
'bris_pedigree_rating_dirt': 'VARCHAR(255)',        ##      1264    CHARACTER       XXXX    4       e.g., '115'
'bris_pedigree_rating_mud': 'VARCHAR(255)',         ##      1265    CHARACTER       XXXX    4
'bris_pedigree_rating_turf': 'VARCHAR(255)',        ##      1266    CHARACTER       XXXX    4
'bris_pedigree_rating_at_distance': 'VARCHAR(255)', ##      1267    CHARACTER       XXXX    4

##      Claimed from and trainer siwtches
'past_claim_trainer_switch_date_1': 'VARCHAR(255)', ##      1268    CHARACTER               10      e.g. '12/30/2000'
'past_claim_trainer_switch_date_2': 'VARCHAR(255)', ##      1269    CHARACTER               10
'past_claim_trainer_switch_date_3': 'VARCHAR(255)', ##      1270    CHARACTER               10
'past_claim_trainer_switch_date_4': 'VARCHAR(255)', ##      1271    CHARACTER               10
'past_claim_trainer_switch_date_5': 'VARCHAR(255)', ##      1272    CHARACTER               10
'past_claim_trainer_switch_date_6': 'VARCHAR(255)', ##      1273    CHARACTER               10
'past_claim_trainer_switch_date_7': 'VARCHAR(255)', ##      1274    CHARACTER               10
'past_claim_trainer_switch_date_8': 'VARCHAR(255)', ##      1275    CHARACTER               10
'past_claim_trainer_switch_date_9': 'VARCHAR(255)', ##      1276    CHARACTER               10
'past_claim_trainer_switch_date_10': 'VARCHAR(255)',##      1277    CHARACTER               10

##      Claimed from and trainer switches
'past_claim_trainer_switch_1_1': 'INT',    ##      1278    NUMERIC                 4
'past_claim_trainer_switch_1_2': 'INT',    ##      1279    NUMERIC                 4
'past_claim_trainer_switch_1_3': 'INT',    ##      1280    NUMERIC                 4
'past_claim_trainer_switch_1_4': 'INT',    ##      1281    NUMERIC                 4
'past_claim_trainer_switch_1_5': 'INT',    ##      1282    NUMERIC                 4
'past_claim_trainer_switch_1_6': 'INT',    ##      1283    NUMERIC                 4
'past_claim_trainer_switch_1_7': 'INT',    ##      1284    NUMERIC                 4
'past_claim_trainer_switch_1_8': 'INT',    ##      1285    NUMERIC                 4
'past_claim_trainer_switch_1_9': 'INT',    ##      1286    NUMERIC                 4
'past_claim_trainer_switch_1_10': 'INT',   ##      1287    NUMERIC                 4

##      Claimed from and trainer switches
'past_claim_trainer_switch_2_1': 'INT',    ##      1288    NUMERIC                 4
'past_claim_trainer_switch_2_2': 'INT',    ##      1289    NUMERIC                 4
'past_claim_trainer_switch_2_3': 'INT',    ##      1290    NUMERIC                 4
'past_claim_trainer_switch_2_4': 'INT',    ##      1291    NUMERIC                 4
'past_claim_trainer_switch_2_5': 'INT',    ##      1292    NUMERIC                 4
'past_claim_trainer_switch_2_6': 'INT',    ##      1293    NUMERIC                 4
'past_claim_trainer_switch_2_7': 'INT',    ##      1294    NUMERIC                 4
'past_claim_trainer_switch_2_8': 'INT',    ##      1295    NUMERIC                 4
'past_claim_trainer_switch_2_9': 'INT',    ##      1296    NUMERIC                 4
'past_claim_trainer_switch_2_10': 'INT',   ##      1297    NUMERIC                 4

##      Claimed from and trainer switches
'past_claim_trainer_switch_3_1': 'INT',    ##      1298    NUMERIC                 4
'past_claim_trainer_switch_3_2': 'INT',    ##      1299    NUMERIC                 4
'past_claim_trainer_switch_3_3': 'INT',    ##      1300    NUMERIC                 4
'past_claim_trainer_switch_3_4': 'INT',    ##      1301    NUMERIC                 4
'past_claim_trainer_switch_3_5': 'INT',    ##      1302    NUMERIC                 4
'past_claim_trainer_switch_3_6': 'INT',    ##      1303    NUMERIC                 4
'past_claim_trainer_switch_3_7': 'INT',    ##      1304    NUMERIC                 4
'past_claim_trainer_switch_3_8': 'INT',    ##      1305    NUMERIC                 4
'past_claim_trainer_switch_3_9': 'INT',    ##      1306    NUMERIC                 4
'past_claim_trainer_switch_3_10': 'INT',   ##      1307    NUMERIC                 4

##      Claimed from and trainer switches
'past_claim_trainer_switch_4_1': 'INT',    ##      1308    NUMERIC                 4
'past_claim_trainer_switch_4_2': 'INT',    ##      1309    NUMERIC                 4
'past_claim_trainer_switch_4_3': 'INT',    ##      1310    NUMERIC                 4
'past_claim_trainer_switch_4_4': 'INT',    ##      1311    NUMERIC                 4
'past_claim_trainer_switch_4_5': 'INT',    ##      1312    NUMERIC                 4
'past_claim_trainer_switch_4_6': 'INT',    ##      1313    NUMERIC                 4
'past_claim_trainer_switch_4_7': 'INT',    ##      1314    NUMERIC                 4
'past_claim_trainer_switch_4_8': 'INT',    ##      1315    NUMERIC                 4
'past_claim_trainer_switch_4_9': 'INT',    ##      1316    NUMERIC                 4
'past_claim_trainer_switch_4_10': 'INT',   ##      1317    NUMERIC                 4

##      Claimed from and trainer switches
'past_claim_trainer_switch_5_1': 'INT',    ##      1318    NUMERIC                 4
'past_claim_trainer_switch_5_2': 'INT',    ##      1319    NUMERIC                 4
'past_claim_trainer_switch_5_3': 'INT',    ##      1320    NUMERIC                 4
'past_claim_trainer_switch_5_4': 'INT',    ##      1321    NUMERIC                 4
'past_claim_trainer_switch_5_5': 'INT',    ##      1322    NUMERIC                 4
'past_claim_trainer_switch_5_6': 'INT',    ##      1323    NUMERIC                 4
'past_claim_trainer_switch_5_7': 'INT',    ##      1324    NUMERIC                 4
'past_claim_trainer_switch_5_8': 'INT',    ##      1325    NUMERIC                 4
'past_claim_trainer_switch_5_9': 'INT',    ##      1326    NUMERIC                 4
'past_claim_trainer_switch_5_10': 'INT',   ##      1327    NUMERIC                 4


##      Best BRIS Speeds: Life, Most recent year horse ran, 2d most recent year horse ran, today's track
'best_bris_speed_life': 'INT',             ##      1328    NUMERIC         9999    4
'best_bris_speed_recent_year': 'INT',      ##      1329    NUMERIC         9999    4
'best_bris_speed_2d_recent_year': 'INT',   ##      1330    NUMERIC         9999    4
'best_bris_speed_todays_track': 'INT',     ##      1331    NUMERIC         9999    4

##      Fast Dirt stats
'fast_dirt_starts': 'INT',                 ##      1332    NUMERIC         999     3
'fast_dirt_wins': 'INT',                   ##      1333    NUMERIC         99      2
'fast_dirt_places': 'INT',                 ##      1334    NUMERIC         99      2
'fast_dirt_wins_shows': 'INT',             ##      1335    NUMERIC         99      2
'fast_dirt_earnings': 'INT',               ##      1336    NUMERIC         9(9)    9

## Key Traininer stat Category 1

'trainer_stat_1_name': 'VARCHAR(255)',              ##      1337    CHARACTER       X(16)   16
'trainer_stat_1_starts': 'INT',            ##      1338    NUMERIC         9999    4
'trainer_stat_1_win_percent': 'FLOAT',       ##      1339    NUMERIC         999.99  6
'trainer_stat_1_itm_percent': 'FLOAT',       ##      1340    NUMERIC         999.99  6       In the money percentage
'trainer_stat_1_roi': 'FLOAT',               ##      1341    NUMERIC         999.99  6       $2 return on investment

## Key Traininer stat Category 2

'trainer_stat_2_name': 'VARCHAR(255)',              ##      1342    CHARACTER       X(16)   16
'trainer_stat_2_starts': 'INT',            ##      1343    NUMERIC         9999    4
'trainer_stat_2_win_percent': 'FLOAT',       ##      1344    NUMERIC         999.99  6
'trainer_stat_2_itm_percent': 'FLOAT',       ##      1345    NUMERIC         999.99  6       In the money percentage
'trainer_stat_2_roi': 'FLOAT',               ##      1346    NUMERIC         999.99  6       $2 return on investment

## Key Traininer stat Category 3

'trainer_stat_3_name': 'VARCHAR(255)',              ##      1347    CHARACTER       X(16)   16
'trainer_stat_3_starts': 'INT',            ##      1348    NUMERIC         9999    4
'trainer_stat_3_win_percent': 'FLOAT',       ##      1349    NUMERIC         999.99  6
'trainer_stat_3_itm_percent': 'FLOAT',       ##      1350    NUMERIC         999.99  6       In the money percentage
'trainer_stat_3_roi': 'FLOAT',               ##      1351    NUMERIC         999.99  6       $2 return on investment

## Key Traininer stat Category 4

'trainer_stat_4_name': 'VARCHAR(255)',              ##      1352    CHARACTER       X(16)   16
'trainer_stat_4_starts': 'INT',            ##      1353    NUMERIC         9999    4
'trainer_stat_4_win_percent': 'FLOAT',       ##      1354    NUMERIC         999.99  6
'trainer_stat_4_itm_percent': 'FLOAT',       ##      1355    NUMERIC         999.99  6       In the money percentage
'trainer_stat_4_roi': 'FLOAT',               ##      1356    NUMERIC         999.99  6       $2 return on investment

## Key Traininer stat Category 5

'trainer_stat_5_name': 'VARCHAR(255)',              ##      1357    CHARACTER       X(16)   16
'trainer_stat_5_starts': 'INT',            ##      1358    NUMERIC         9999    4
'trainer_stat_5_win_percent': 'FLOAT',       ##      1359    NUMERIC         999.99  6
'trainer_stat_5_itm_percent': 'FLOAT',       ##      1360    NUMERIC         999.99  6       In the money percentage
'trainer_stat_5_roi': 'FLOAT',               ##      1361    NUMERIC         999.99  6       $2 return on investment

## Key Traininer stat Category 6

'trainer_stat_6_name': 'VARCHAR(255)',              ##      1362    CHARACTER       X(16)   16
'trainer_stat_6_starts': 'INT',            ##      1363    NUMERIC         9999    4
'trainer_stat_6_win_percent': 'FLOAT',       ##      1364    NUMERIC         999.99  6
'trainer_stat_6_itm_percent': 'FLOAT',       ##      1365    NUMERIC         999.99  6       In the money percentage
'trainer_stat_6_roi': 'FLOAT',               ##      1366    NUMERIC         999.99  6       $2 return on investment

##      JKY @ Distance/ Jky on Turf stats

'jockey_at_distance_on_turf_label': 'VARCHAR(255)',     ##      1367    CHARACTER       X(13)   13
'jockey_at_distance_on_turf_starts': 'INT',    ##      1368    NUMERIC         9999    4
'jockey_at_distance_on_turf_wins': 'INT',      ##      1369    NUMERIC         9999    4
'jockey_at_distance_on_turf_places': 'INT',    ##      1370    NUMERIC         9999    4
'jockey_at_distance_on_turf_shows': 'INT',     ##      1371    NUMERIC         9999    4
'jockey_at_distance_on_turf_roi': 'FLOAT',       ##      1372    NUMERIC         999.99  6
'jockey_at_distance_on_turf_earnings': 'INT',  ##      1373    NUMERIC         9(8)    8

## Post times(by region)

'post_times_by_region': 'VARCHAR(255)',             ##      1374    CHARACTER       X(50)   50

##      Extended Start Comment
'past_extended_start_comment_1': 'VARCHAR(255)',    ##      1383    CHARACTER       X(90)   90
'past_extended_start_comment_2': 'VARCHAR(255)',    ##      1384    CHARACTER       X(90)   90
'past_extended_start_comment_3': 'VARCHAR(255)',    ##      1385    CHARACTER       X(90)   90
'past_extended_start_comment_4': 'VARCHAR(255)',    ##      1386    CHARACTER       X(90)   90
'past_extended_start_comment_5': 'VARCHAR(255)',    ##      1387    CHARACTER       X(90)   90
'past_extended_start_comment_6': 'VARCHAR(255)',    ##      1388    CHARACTER       X(90)   90
'past_extended_start_comment_7': 'VARCHAR(255)',    ##      1389    CHARACTER       X(90)   90
'past_extended_start_comment_8': 'VARCHAR(255)',    ##      1390    CHARACTER       X(90)   90
'past_extended_start_comment_9': 'VARCHAR(255)',    ##      1391    CHARACTER       X(90)   90
'past_extended_start_comment_10': 'VARCHAR(255)',   ##      1392    CHARACTER       X(90)   90

##      'Sealed' track indicator
'past_sealed_track_indicator_1': 'INT',    ##      1393    CHARACTER       X       1       's'- Sealed
'past_sealed_track_indicator_2': 'INT',    ##      1394    CHARACTER       X       1
'past_sealed_track_indicator_3': 'INT',    ##      1395    CHARACTER       X       1
'past_sealed_track_indicator_4': 'INT',    ##      1396    CHARACTER       X       1
'past_sealed_track_indicator_5': 'INT',    ##      1397    CHARACTER       X       1
'past_sealed_track_indicator_6': 'INT',    ##      1398    CHARACTER       X       1
'past_sealed_track_indicator_7': 'INT',    ##      1399    CHARACTER       X       1
'past_sealed_track_indicator_8': 'INT',    ##      1400    CHARACTER       X       1
'past_sealed_track_indicator_9': 'INT',    ##      1401    CHARACTER       X       1
'past_sealed_track_indicator_10': 'INT',   ##      1402    CHARACTER       X       1

##      Prev. All-Weather Sureface Flag
'past_all_weather_flag_1': 'INT',          ##      1403    CHARACTER       X       1       A- All weather surface
'past_all_weather_flag_2': 'INT',          ##      1404    CHARACTER       X       1
'past_all_weather_flag_3': 'INT',          ##      1405    CHARACTER       X       1
'past_all_weather_flag_4': 'INT',          ##      1406    CHARACTER       X       1
'past_all_weather_flag_5': 'INT',          ##      1407    CHARACTER       X       1
'past_all_weather_flag_6': 'INT',          ##      1408    CHARACTER       X       1
'past_all_weather_flag_7': 'INT',          ##      1409    CHARACTER       X       1
'past_all_weather_flag_8': 'INT',          ##      1410    CHARACTER       X       1
'past_all_weather_flag_9': 'INT',          ##      1411    CHARACTER       X       1
'past_all_weather_flag_10': 'INT',         ##      1412    CHARACTER       X       1

##      Trainer/Jockey combo stats (meet)
'TJ_combo_starts': 'INT',                  ##      1413    NUMERIC         9999    4
'TJ_combo_wins': 'INT',                    ##      1414    NUMERIC         9999    4
'TJ_combo_places': 'INT',                  ##      1415    NUMERIC         9999    4
'TJ_combo_shows': 'INT',                   ##      1416    NUMERIC         9999    4
'TJ_combo_roi': 'FLOAT',                     ##      1417    NUMERIC         999.99  6       $2 return on investment

##      Post time (PAcific military time) '0300' for 3am pacific time
'post_time_pacific_military': 'VARCHAR(255)',          ##      1418    CHARACTER       XXXX    4

##      Equibase abbreviated race conditions
'past_equibase_race_conditions_1': 'VARCHAR(255)',  ##      1419    CHARACTER       X(17)   17
'past_equibase_race_conditions_2': 'VARCHAR(255)',  ##      1420    CHARACTER       X(17)   17
'past_equibase_race_conditions_3': 'VARCHAR(255)',  ##      1421    CHARACTER       X(17)   17
'past_equibase_race_conditions_4': 'VARCHAR(255)',  ##      1421    CHARACTER       X(17)   17
'past_equibase_race_conditions_5': 'VARCHAR(255)',  ##      1423    CHARACTER       X(17)   17
'past_equibase_race_conditions_6': 'VARCHAR(255)',  ##      1424    CHARACTER       X(17)   17
'past_equibase_race_conditions_7': 'VARCHAR(255)',  ##      1425    CHARACTER       X(17)   17
'past_equibase_race_conditions_8': 'VARCHAR(255)',  ##      1426    CHARACTER       X(17)   17
'past_equibase_race_conditions_9': 'VARCHAR(255)',  ##      1427    CHARACTER       X(17)   17
'past_equibase_race_conditions_10': 'VARCHAR(255)', ##      1428    CHARACTER       X(17)   17
'equibase_race_conditions': 'VARCHAR(255)',
}