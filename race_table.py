import logging

from aggregation_functions import SQLConnection, QueryDB, query_table, DbHandler

db_processor = DbHandler(db='horses_consolidated_races')
db_horses_data = QueryDB(db='horses_data')

table_name = 'horses_consolidated_races'

table_structure = {
    # Format 'sql_col_name': ('sql_datatype', 'race_general_results_col', 'race_info col', 'horse_pps col')
    'source_file': ('VARCHAR(255)', 'source_file', 'source_file', 'source_file',),
    'track': ('VARCHAR(255)', 'track', 'track', 'track_code',),
    'date': ('DATE', 'date', 'date', 'race_date',),
    'race_num': ('TINYINT', 'race_num', 'race_num', 'race_num',),
    'race_name': ('VARCHAR(255)', 'race_name', None, None,),
    'time_local': ('INT', 'off_time', None, None,),
    'time_zone':('VARCHAR(255)', None, None, None,),

    'temperature': ('INT', 'race_temp', None, None,),
    'weather': ('VARCHAR(255)', 'weather', None, None,),

    'distance': ('INT', 'distance', 'distance', 'distance',),
    'run_up_distance': ('INT', 'run_up_dist', None, None,),
    'temp_rail_distance': ('INT', 'temp_rail_dist', None, None),
    'about_distance_flag': ('TINYINT', 'about_distance', None, None,),

    'surface': ('VARCHAR(255)', 'surface_new', 'surface', 'surface',),
    # 'sealed_track'
    'track_condition': ('VARCHAR(255)', 'track_condition', None, 'track_condition',),
    'chute_start': ('TINYINT', 'chute_start', None, 'special_chute',),

    'off_turf': ('TINYINT', 'off_turf', None, None,),
    'off_turf_dist_change': ('TINYINT', 'off_turf_distance_change', None, None),

    'field_size': ('INT', 'field_size', None, 'num_of_horses',),
    'breed': ('VARCHAR(255)', 'breed', 'breed', None),

    'purse': ('INT', 'purse', 'purse', 'race_purse',),

    'race_type': ('VARCHAR(255)', 'race_type_BRIS', 'race_type', 'race_type',),

    'claiming_price_base': ('INT', 'max_claim', 'claiming_price', 'highest_claim_price',),
    'optional_claiming_price': ('INT', 'optional_claiming_price', 'optional_claiming_price',),

    'allowed_age_two': ('TINYINT', 'allowed_age_two', 'allowed_age_two', 'allowed_age_two',),
    'allowed_age_three': ('TINYINT', 'allowed_age_three', 'allowed_age_three', 'allowed_age_three',),
    'allowed_age_four': ('TINYINT', 'allowed_age_four', 'allowed_age_four', 'allowed_age_four',),
    'allowed_age_five': ('TINYINT', 'allowed_age_five', 'allowed_age_five', 'allowed_age_five',),
    'allowed_age_older': ('TINYINT', 'allowed_age_older', 'allowed_age_older', 'allowed_age_older',),

    'allowed_fillies': ('TINYINT', 'allowed_fillies', 'allowed_fillies', 'allowed_fillies',),
    'allowed_mares': ('TINYINT', 'allowed_mares', 'allowed_mares', 'allowed_mares',),
    'allowed_colts_geldings': ('TINYINT', 'allowed_colts_geldings', 'allowed_colts_geldings', 'allowed_colts_geldings',),

    'statebred_race': ('TINYINT', 'statebred_race', 'statebred_race', 'statebred_race',),

    'race_conditions_1_claim_start_req_price': ('INT', 'condition_1_claim_start_required_price', 'condition_1_claim_start_required_price', None,),
    'race_conditions_1_claim_start_time_limit': ('INT', 'condition_1_claim_start_required_months', 'condition_1_claim_start_required_months', None,),
    'race_conditions_1_not_won_limit': ('INT', 'condition_1_number_limit', 'condition_1_number_limit', None,),
    'race_conditions_1_money_limit': ('INT', 'condition_1_money_limit', 'condition_1_money_limit', None,),
    'race_conditions_1_time_limit': ('INT', 'condition_1_time_limit_months', 'condition_1_time_limit_months', None,),
    'race_conditions_1_excluded_claiming': ('TINYINT', 'condition_1_excluded_claiming', 'condition_1_excluded_claiming', None,),
    'race_conditions_1_excluded_maiden': ('TINYINT', 'condition_1_excluded_maiden', 'condition_1_excluded_maiden', None,),
    'race_conditions_1_excluded_optional': ('TINYINT', 'condition_1_excluded_optional', 'condition_1_excluded_optional', None,),
    'race_conditions_1_excluded_restricted': ('TINYINT', 'condition_1_excluded_restricted', 'condition_1_excluded_restricted', None,),
    'race_conditions_1_excluded_restricted_allowance': ('TINYINT', 'condition_1_excluded_restricted_allowance', 'condition_1_excluded_restricted_allowance', None,),
    'race_conditions_1_excluded_starter': ('TINYINT', 'condition_1_excluded_starter', 'condition_1_excluded_starter', None,),
    'race_conditions_1_excluded_state_sired': ('TINYINT', 'condition_1_excluded_state_sired', 'condition_1_excluded_state_sired', None),
    'race_conditions_1_excluded_state_sired_stakes': ('TINYINT', 'condition_1_excluded_state_sired_stakes', 'condition_1_excluded_state_sired_stakes', None,),
    'race_conditions_1_excluded_statebred': ('TINYINT', 'condition_1_excluded_statebred', 'condition_1_excluded_statebred', None,),
    'race_conditions_1_excluded_statebred_allowance': ('TINYINT', 'condition_1_excluded_statebred_allowance', 'condition_1_excluded_statebred_allowance', None,),
    'race_conditions_1_excluded_statebred_stakes': ('TINYINT', 'condition_1_excluded_statebred_stakes', 'condition_1_excluded_statebred_stakes', None,),
    'race_conditions_1_excluded_trial': ('TINYINT', 'condition_1_excluded_trial', 'condition_1_excluded_trial', None,),
    'race_conditions_1_excluded_waiver': ('TINYINT', 'condition_1_excluded_waiver', 'condition_1_excluded_waiver', None,),
    'race_conditions_1_excluded_waiver_claiming': ('TINYINT', 'condition_1_excluded_waiver_claiming', 'condition_1_excluded_waiver_claiming', None,),

    'race_conditions_2_claim_start_req_price': ('INT', 'condition_2_claim_start_required_price', 'condition_2_claim_start_required_price', None,),
    'race_conditions_2_claim_start_time_limit': ('INT', 'condition_2_claim_start_required_months', 'condition_2_claim_start_required_months', None,),
    'race_conditions_2_not_won_limit': ('INT', 'condition_2_number_limit', 'condition_2_number_limit', None,),
    'race_conditions_2_money_limit': ('INT', 'condition_2_money_limit', 'condition_2_money_limit', None,),
    'race_conditions_2_time_limit': ('INT', 'condition_2_time_limit_months', 'condition_2_time_limit_months', None,),
    'race_conditions_2_excluded_claiming': ('TINYINT', 'condition_2_excluded_claiming', 'condition_2_excluded_claiming', None,),
    'race_conditions_2_excluded_maiden': ('TINYINT', 'condition_2_excluded_maiden', 'condition_2_excluded_maiden', None,),
    'race_conditions_2_excluded_optional': ('TINYINT', 'condition_2_excluded_optional', 'condition_2_excluded_optional', None,),
    'race_conditions_2_excluded_restricted': ('TINYINT', 'condition_2_excluded_restricted', 'condition_2_excluded_restricted', None,),
    'race_conditions_2_excluded_restricted_allowance': ('TINYINT', 'condition_2_excluded_restricted_allowance', 'condition_2_excluded_restricted_allowance', None,),
    'race_conditions_2_excluded_starter': ('TINYINT', 'condition_2_excluded_starter', 'condition_2_excluded_starter', None,),
    'race_conditions_2_excluded_state_sired': ('TINYINT', 'condition_2_excluded_state_sired', 'condition_2_excluded_state_sired', None),
    'race_conditions_2_excluded_state_sired_stakes': ('TINYINT', 'condition_2_excluded_state_sired_stakes', 'condition_2_excluded_state_sired_stakes', None,),
    'race_conditions_2_excluded_statebred': ('TINYINT', 'condition_2_excluded_statebred', 'condition_2_excluded_statebred', None,),
    'race_conditions_2_excluded_statebred_allowance': ('TINYINT', 'condition_2_excluded_statebred_allowance', 'condition_2_excluded_statebred_allowance', None,),
    'race_conditions_2_excluded_statebred_stakes': ('TINYINT', 'condition_2_excluded_statebred_stakes', 'condition_2_excluded_statebred_stakes', None,),
    'race_conditions_2_excluded_trial': ('TINYINT', 'condition_2_excluded_trial', 'condition_2_excluded_trial', None,),
    'race_conditions_2_excluded_waiver': ('TINYINT', 'condition_2_excluded_waiver', 'condition_2_excluded_waiver', None,),
    'race_conditions_2_excluded_waiver_claiming': ('TINYINT', 'condition_2_excluded_waiver_claiming', 'condition_2_excluded_waiver_claiming', None,),

    'race_conditions_3_claim_start_req_price': ('INT', 'condition_3_claim_start_required_price', 'condition_3_claim_start_required_price', None,),
    'race_conditions_3_claim_start_time_limit': ('INT', 'condition_3_claim_start_required_months', 'condition_3_claim_start_required_months', None,),
    'race_conditions_3_not_won_limit': ('INT', 'condition_3_number_limit', 'condition_3_number_limit', None,),
    'race_conditions_3_money_limit': ('INT', 'condition_3_money_limit', 'condition_3_money_limit', None,),
    'race_conditions_3_time_limit': ('INT', 'condition_3_time_limit_months', 'condition_3_time_limit_months', None,),
    'race_conditions_3_excluded_claiming': ('TINYINT', 'condition_3_excluded_claiming', 'condition_3_excluded_claiming', None,),
    'race_conditions_3_excluded_maiden': ('TINYINT', 'condition_3_excluded_maiden', 'condition_3_excluded_maiden', None,),
    'race_conditions_3_excluded_optional': ('TINYINT', 'condition_3_excluded_optional', 'condition_3_excluded_optional', None,),
    'race_conditions_3_excluded_restricted': ('TINYINT', 'condition_3_excluded_restricted', 'condition_3_excluded_restricted', None,),
    'race_conditions_3_excluded_restricted_allowance': ('TINYINT', 'condition_3_excluded_restricted_allowance', 'condition_3_excluded_restricted_allowance', None,),
    'race_conditions_3_excluded_starter': ('TINYINT', 'condition_3_excluded_starter', 'condition_3_excluded_starter', None,),
    'race_conditions_3_excluded_state_sired': ('TINYINT', 'condition_3_excluded_state_sired', 'condition_3_excluded_state_sired', None),
    'race_conditions_3_excluded_state_sired_stakes': ('TINYINT', 'condition_3_excluded_state_sired_stakes', 'condition_3_excluded_state_sired_stakes', None,),
    'race_conditions_3_excluded_statebred': ('TINYINT', 'condition_3_excluded_statebred', 'condition_3_excluded_statebred', None,),
    'race_conditions_3_excluded_statebred_allowance': ('TINYINT', 'condition_3_excluded_statebred_allowance', 'condition_3_excluded_statebred_allowance', None,),
    'race_conditions_3_excluded_statebred_stakes': ('TINYINT', 'condition_3_excluded_statebred_stakes', 'condition_3_excluded_statebred_stakes', None,),
    'race_conditions_3_excluded_trial': ('TINYINT', 'condition_3_excluded_trial', 'condition_3_excluded_trial', None,),
    'race_conditions_3_excluded_waiver': ('TINYINT', 'condition_3_excluded_waiver', 'condition_3_excluded_waiver', None,),
    'race_conditions_3_excluded_waiver_claiming': ('TINYINT', 'condition_3_excluded_waiver_claiming', 'condition_3_excluded_waiver_claiming', None,),

    'race_conditions_text_1': ('VARCHAR(255)', 'race_conditions_1', 'race_cond_1', None,),
    'race_conditions_text_2': ('VARCHAR(255)', 'race_conditions_2', 'race_cond_2', None,),
    'race_conditions_text_3': ('VARCHAR(255)', 'race_conditions_3', 'race_cond_3', None,),
    'race_conditions_text_4': ('VARCHAR(255)', 'race_conditions_4', 'race_cond_4', None,),
    'race_conditions_text_5': ('VARCHAR(255)', 'race_conditions_5', 'race_cond_5', None,),
    'race_conditions_text_6': ('VARCHAR(255)', None, 'race_cond_6', None,),

    # 'race_notes': (),
}
table_to_index_mapping = {
    'race_general_results' : 1,
    'race_info': 2,
    'horse_pps': 3,
}

# Initialize_table
db_dtypes = {key: value[0] for key, value in table_structure.items()}
unique = ['track', 'date', 'race_num']
db_processor.initialize_table(table_name, db_dtypes, unique_key=unique, foreign_key=None)


def race_in_db(db_handler, table, track, date, race_num):
    """
    Returns True if a particular race (unique track-date-race_num) is in the db; otherwise returns false
    """
    sql = f'SELECT COUNT(*) FROM {table} WHERE '
    sql += f'track = "{track}" '
    sql += f'AND date = "{date}" '
    sql += f'AND race_num = "{race_num}"'
    return db_handler.query_db(sql)[0][0]


def dict_values_match(dict_key, dict_1, dict_2):
    if dict_1[dict_key] == dict_2[dict_key]:
        return True
    else:
        return False

def process_race_general_results():
    # Create dict with sql column names and corresponding race_general_results column names
    db_dict = {key: value[table_to_index_mapping['race_general_results']] for key, value in table_structure.items()
               if value[table_to_index_mapping['race_general_results']]}
    sql_columns = [key for key, _ in db_dict.items()]
    source_columns = [db_dict[column] for column in sql_columns]

    # Pull list of race identifiers stored in race_general_results.
    list_of_races  = query_table(db_horses_data, 'race_general_results', ['track', 'date', 'race_num'])

    # For each race, pull info from db and add it to new table:
    i = 0
    for race in list_of_races:
        total_num = len(list_of_races)
        print(f'i: {i} of {total_num}. {race}')
        race_data = query_table(db_horses_data,
                                             'race_general_results',
                                             source_columns,
                                             where='track="{}" AND date="{}" AND race_num="{}"'.format(*race))
        db_processor.add_to_table(table_name, race_data, sql_columns)
        i += 1


def process_race_info():
    # Create dict with sql col names and corresponding race_info column names
    db_dict = {key: value[table_to_index_mapping['race_info']] for key, value in table_structure.items()
               if value[table_to_index_mapping['race_info']]}
    sql_columns = [key for key, _ in db_dict.items()]
    source_columns = [db_dict[column] for column in sql_columns]

    # Pull list of race identifiers stored in race_info
    list_of_races = query_table(db_horses_data, 'race_info', ['track', 'date', 'race_num'])

    # Variable to hold race identifiers for data issues
    races_with_inconsistent_data = []

    i = 0
    total_num = len(list_of_races)

    for race in list_of_races:
        print(f'i: {i} of {total_num}. {race}')
        in_db = race_in_db(db_processor, table_name, *race)
        print(in_db)
        race_data = query_table(db_horses_data,
                                             'race_info',
                                             source_columns,
                                             where='track="{}" AND date="{}" AND race_num="{}"'.format(*race))

        # If the race isn't in the db, add in data from race_info:
        if not in_db:
            print('Not in db')
            db_processor.add_to_table(table_name, race_data, sql_columns)
        # If it is in the db, check that values match
        else:
            print('Is in db')
            data_in_db = query_table(db_processor, table_name, *race)
            info_in_db = {key: value for key, value in zip(source_columns, data_in_db)}
            new_info = {key: value for key, value in zip(source_columns, race_data)}
            info_matches = {key: dict_values_match(key, info_in_db, new_info) for key in data_in_db.keys()}

            if all(info_matches.values()):
                print('All the info matches')

            if not all(info_matches.values()):
                races_with_inconsistent_data.append(race)
                inconsistent_keys = [key for key in info_matches.keys() if info_matches[key] == False]
                print(f'**********\nMismatch: {key}')
                print(f'race_general_results: {info_in_db[key]}')
                print(f'race_info: {new_info[key]}')
                input('')
        i += 1
    return races_with_inconsistent_data









