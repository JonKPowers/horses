
def tidy_it_up(table_data, extension, verbose=False):
    extension = str(extension)
    if extension == '1':
        if verbose: ('Tidying .1 file ...')

        # *********************************************
        # Flag fixes

        table_data['about_dist_flag'].replace('A', 1, inplace=True)
        table_data['about_dist_flag'].fillna(0, inplace=True)

        table_data['all_weather_flag'].replace('A', 1, inplace=True)
        table_data['all_weather_flag'].fillna(0, inplace=True)

        table_data['state_bred_flag'].replace('S', 1, inplace=True)
        table_data['state_bred_flag'].fillna(0, inplace=True)

        table_data['chute_start_flag'].replace('C', 1, inplace=True)
        table_data['chute_start_flag'].replace('N', 0, inplace=True)
        table_data['chute_start_flag'].fillna(0, inplace=True)

        table_data['off_turf_flag'].replace('O', 1, inplace=True)
        table_data['off_turf_flag'].fillna(0, inplace=True)

        table_data['off_turf_dist_change'].replace('Y', 1, inplace=True)
        table_data['off_turf_dist_change'].replace('N', 0, inplace=True)

        table_data['race_grade'].replace(0, 'NULL', inplace=True)

        # *********************************************
        # Fill and na's with NULL for MYSQL transfer
        table_data.fillna('NULL', inplace=True)

    if extension == '2':
        if verbose: print('Tidying .2 file ...')

        table_data['nonbetting_flag'].replace('Y', 1, inplace=True)
        table_data['nonbetting_flag'].fillna(0, inplace=True)

        table_data['disqualified_flag'].replace('Y', 1, inplace=True)
        table_data['disqualified_flag'].fillna(0, inplace=True)


        table_data['corrected_weight'].replace('Y', 1, inplace=True)
        table_data['corrected_weight'].fillna(0, inplace=True)

        table_data['claimed_flag'].replace('Y', 1, inplace=True)
        table_data['claimed_flag'].replace('N', 0, inplace=True)

        table_data['dead_heat_flag'].replace('DH', 1, inplace=True)
        table_data['dead_heat_flag'].fillna(0, inplace=True)

        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    if extension == '3':
        if verbose: print('Tidying .3 file (ITM payoffs) ...')
        table_data.fillna('NULL', inplace=True)

    if extension == '4':
        if verbose: print('Tidying .4 file (exotic payoffs) ...')
        table_data.fillna('NULL', inplace=True)

    if extension == '5':
        if verbose: print('Tidying .5 file (breeding info)...')
        table_data.fillna('NULL', inplace=True)

    if extension == '6':
        if verbose: print('Tidying .6 file (footnotes) ...')
        table_data.fillna('NULL', inplace=True)

    if extension == 'DRF':
        print('Tidying .DRF file (past performances) ...')

        for i in range(1, 11):
            past_bullet_flag = list()
            for j in range(len(table_data)):
                if table_data[f'workout_time_{i}'][j] < 0:
                    past_bullet_flag.append(1)
                else:
                    past_bullet_flag.append(0)
            table_data[f'workout_time_{i}_bullet'] = past_bullet_flag

        for i in range(1, 11):
            table_data[f'workout_time_{i}'] = table_data[f'workout_time_{i}'].abs()

        for i in range(1, 11):
            past_about_distance = list()
            for j in range(len(table_data)):
                if table_data[f'past_distance_{i}'][j] < 0:
                    past_about_distance.append(1)
                else:
                    past_about_distance.append(0)
            table_data[f'past_distance_{i}_about_flag'] = past_about_distance
        for i in range(1, 11):
            table_data[f'past_distance_{i}'] = table_data[f'past_distance_{i}'].abs()
        for i in range(1, 11):
            table_data[f'workout_distance_{i}'] = table_data[f'workout_distance_{i}'].abs()
        table_data['distance'] = table_data['distance'].abs()

        # *********************************************
        # Field with [value]/NaN flags

        table_data['apprentice_wgt_alw'].fillna(0, inplace=True)

        table_data['statebread_flag'].replace('s', 1, inplace=True)
        table_data['statebread_flag'].fillna(0, inplace=True)

        table_data['today_nasal_strip_chg'].replace(9, 'NULL', inplace=True)
        table_data['todays_meds_new'].replace(9, 'NULL', inplace=True)
        table_data['todays_meds_old'].replace(9, 'NULL', inplace=True)
        table_data['equipment_change'].replace(9, 'NULL', inplace=True)

        table_data['allweather_surface'].replace('A', 1, inplace=True)
        table_data['allweather_surface'].fillna(0, inplace=True)

        table_data['bris_run_style'].replace('NA', None, inplace=True)

        # Change a n/a claiming_price value to 0 to match race_results handling.
        table_data['claiming_price'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_special_chute_{i}'].replace('c', 1, inplace=True)
            table_data[f'past_special_chute_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_bar_shoe_{i}'].replace('r', 1, inplace=True)
            table_data[f'past_bar_shoe_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_start_code_{i}'].replace('X', 1, inplace=True)
            table_data[f'past_start_code_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_sealed_track_indicator_{i}'].replace('s', 1, inplace=True)
            table_data[f'past_sealed_track_indicator_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_all_weather_flag_{i}'].replace('A', 1, inplace=True)
            table_data[f'past_all_weather_flag_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_weight_allowance_{i}'].fillna(0, inplace=True)

        # Convert surface-type field in PP data to "new" surface-type style
        # (code is 'A' for all-weather dirt track and 'D' for non-all-weather)
        for i in range(1, 11):
            surface_field = table_data.columns.get_loc(f'past_surface_{i}')
            all_weather_field = table_data.columns.get_loc(f'past_all_weather_flag_{i}')
            for j in range(len(table_data)):
                if table_data.iloc[j, all_weather_field] == 1:
                    table_data.iloc[j, surface_field] = 'A'

        # Convert surface-type field DRF race info to "new surface-type style
        # (code is 'A' for all-weather dirt track and 'D' for non-all-weather

        surface_field = table_data.columns.get_loc('surface')
        all_weather_field = table_data.columns.get_loc('allweather_surface')
        for i in range(len(table_data)):
            if table_data.iloc[i, all_weather_field] == 1:
                table_data.iloc[i, surface_field] = 'A'

        for i in range(1, 11):
            table_data[f'past_equipment_{i}'].replace('b', 1, inplace=True)
            table_data[f'past_equipment_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_entry_{i}'].replace('e', 1, inplace=True)
            table_data[f'past_entry_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_claimed_code_{i}'].replace('c', 1, inplace=True)
            table_data[f'past_claimed_code_{i}'].replace('v', 1, inplace=True)
            table_data[f'past_claimed_code_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_statebred_flag_{i}'].replace('s', 1, inplace=True)
            table_data[f'past_statebred_flag_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_restricted_or_qualified_{i}'].replace('R', 1, inplace=True)
            table_data[f'past_restricted_or_qualified_{i}'].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data[f'past_call_pos_start_{i}'].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data[f'past_call_pos_first_{i}'].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data[f'past_call_pos_second_{i}'].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data[f'past_call_pos_stretch_{i}'].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data[f'past_company_line_{i}'].replace(r' ', 'X', regex=True, inplace=True)

        for i in range(1, 11):
            table_data[f'past_call_pos_finish_{i}'].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        # Extract whether there was a off turf distance change for the PP race, and add a column with a flag for that
        for i in range(1, 11):
            past_off_turf_dist_change = list()
            for j in range(len(table_data)):
                if table_data[f'past_start_code_{i}'][j] == 'x':
                    past_off_turf_dist_change.append(1)
                else:
                    past_off_turf_dist_change.append(0)
            table_data[f'past_{i}_off_turf_dist_change'] = past_off_turf_dist_change

        # Extract whether the horse used a nasal string for the PP race; add a column with a flag for that info
        # Extract whether there was a off turf distance change for the PP race, and add a column with a flag for that
        for i in range(1, 11):
            past_nasal_strip = list()
            for j in range(len(table_data)):
                if table_data[f'past_start_code_{i}'][j] == 's':
                    past_nasal_strip.append(1)
                else:
                    past_nasal_strip.append(0)
            table_data[f'past_{i}_nasal_strip'] = past_nasal_strip

        for i in range(1, 11):
            table_data[f'past_start_code_{i}'].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        # *********************************************
        # Character fields to make null

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)

        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    return table_data
