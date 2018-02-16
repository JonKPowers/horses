
def tidy_it_up(table_data, extension):
    extension = str(extension)
    if extension == '1':
        print('Tidying .1 file ...')

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

        # *********************************************
        # Fill and na's with NULL for MYSQL transfer
        table_data.fillna('NULL', inplace=True)

    if extension == '2':
        print('Tidying .2 file ...')

        table_data['nonbetting_flag'].replace('Y', 1, inplace=True)
        table_data['nonbetting_flag'].fillna(0, inplace=True)

        table_data['disqualified_flag'].replace('Y', 1, inplace=True)
        table_data['disqualified_flag'].fillna(0, inplace=True)


        table_data['corrected_weight'].replace('Y', 1, inplace=True)
        table_data['corrected_weight'].fillna(0, inplace=True)

        table_data['claimed_flag'].replace('Y', 1, inplace=True)
        table_data['claimed_flag'].replace('N', 0, inplace=True)
        table_data['dead_heat_flag'].replace('DH', 1, inplace=True)



        # *********************************************
        # Field with [value]/NaN flags
        # TO DO:
        #   (1) Run through these columns and replace the flags with int(1)

        # *********************************************
        # Character fields to make null

        table_data['claimed_trainer_middle'].fillna('NULL', inplace=True)

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)


        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    if extension == '3':
        print('Tidying .3 file (ITM payoffs) ...')

        # *********************************************
        # Field with [value]/NaN flags
        # TO DO:
        #   (1) Run through these columns and replace the flags with int(1)

        # *********************************************
        # Character fields to make null

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)


        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    if extension == '4':
        print('Tidying .4 file (exotic payoffs) ...')

        # *********************************************
        # Field with [value]/NaN flags
        # TO DO:
        #   (1) Run through these columns and replace the flags with int(1)

        # *********************************************
        # Character fields to make null

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)


        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    if extension == '5':
        print('Tidying .5 file (breeding info)...')
        where_bred = []
        foreign_bred = list(table_data['foreignbred_code'])
        state_bred = list(table_data['statebred_code'])
        foreign_bred_null = list(table_data['foreignbred_code'].isnull())

        for i in range(len(foreign_bred)):
            if foreign_bred_null[i]:
                where_bred.append(state_bred[i])
            else:
                where_bred.append(foreign_bred[i])
        table_data['where_bred'] = where_bred

        table_data.fillna('NULL', inplace=True)

    if extension == '6':
        print('Tidying .6 file (footnotes) ...')



        # *********************************************
        # Character fields to make null

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)


        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    if extension == 'DRF':
        print('Tidying .DRF file (past performances) ...')

        # *********************************************
        # Items that are marked with negative values for special meaning:
        # Workout times:
        for i in range(1, 11):
            table_data['workout_time_{}'.format(i)] = table_data['workout_time_{}'.format(i)].abs()
        for i in range(1, 11):
            table_data['workout_distance_{}'.format(i)] = table_data['workout_distance_{}'.format(i)].abs()
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


        for i in range(1, 11):
            table_data['past_special_chute_{}'.format(i)].replace('c', 1, inplace=True)
            table_data['past_special_chute_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_bar_shoe_{}'.format(i)].replace('r', 1, inplace=True)
            table_data['past_bar_shoe_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_sealed_track_indicator_{}'.format(i)].replace('s', 1, inplace=True)
            table_data['past_sealed_track_indicator_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_all_weather_flag_{}'.format(i)].replace('A', 1, inplace=True)
            table_data['past_all_weather_flag_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_equipment_{}'.format(i)].replace('b', 1, inplace=True)
            table_data['past_equipment_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_entry_{}'.format(i)].replace('e', 1, inplace=True)
            table_data['past_entry_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_claimed_code_{}'.format(i)].replace('c', 1, inplace=True)
            table_data['past_claimed_code_{}'.format(i)].replace('v', 1, inplace=True)
            table_data['past_claimed_code_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_statebred_flag_{}'.format(i)].replace('s', 1, inplace=True)
            table_data['past_statebred_flag_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_restricted_or_qualified_{}'.format(i)].replace('R', 1, inplace=True)
            table_data['past_restricted_or_qualified_{}'.format(i)].fillna(0, inplace=True)

        for i in range(1, 11):
            table_data['past_call_pos_start_{}'.format(i)].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data['past_call_pos_first_{}'.format(i)].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data['past_call_pos_second_{}'.format(i)].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data['past_call_pos_stretch_{}'.format(i)].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        for i in range(1, 11):
            table_data['past_call_pos_finish_{}'.format(i)].replace(r'[A-Za-z?*]+', 'NULL', regex=True, inplace=True)

        # *********************************************
        # Character fields to make null

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)


        # **********************************************
        # Fill the rest with 'NULL'
        table_data.fillna('NULL', inplace=True)

    return table_data