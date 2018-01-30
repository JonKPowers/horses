# ----------------------------------------------------------------
#   Items to do for processing csv/pd.df items
#       (1) .1--about_dist_flag should be changed to 0 or 1 (from NaN or 'A')

def tidy_it_up(table_data, extension):
    extension = str(extension)
    if extension == '1':
        print('Tidying .1 file ...')

        # *********************************************
        # Flag fixes

        table_data['about_dist_flag'] = table_data['about_dist_flag'].replace('A', 1)
        table_data['all_weather_flag'] = table_data['all_weather_flag'].replace('A', 1)
        table_data['chute_start_flag'] = table_data['chute_start_flag'].replace('C', 1)
        table_data['off_turf_flag'] = table_data['off_turf_flag'].replace('O', 1)
        table_data['off_turf_dist_change'] = table_data['off_turf_dist_change'].replace('Y', 1)

        # *********************************************
        # Fill and na's with NULL for MYSQL transfer
        table_data = table_data.fillna('NULL')

    if extension == '2':
        print('Tidying .2 file ...')

        table_data['nonbetting_flag'] = table_data['nonbetting_flag'].replace('Y', 1)
        table_data['disqualified_flag'] = table_data['disqualified_flag'].replace('Y', 1)
        table_data['corrected_weight'] = table_data['corrected_weight'].replace('Y', 1)
        table_data['claimed_flag'] = table_data['claimed_flag'].replace('Y', 1)
        table_data['dead_heat_flag'] = table_data['dead_heat_flag'].replace('DH', 1)



        # *********************************************
        # Field with [value]/NaN flags
        # TO DO:
        #   (1) Run through these columns and replace the flags with int(1)

        # *********************************************
        # Character fields to make null

        table_data['claimed_trainer_middle'] = table_data['claimed_trainer_middle'].fillna('NULL')

        # **********************************************
        # FIELD DTYPES TO FIX
        #   'claimed_trainer_middle' from FLOAT to VARCHAR(255)


        # **********************************************
        # Fill the rest with 'NULL'
        table_data = table_data.fillna('NULL')

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
        table_data = table_data.fillna('NULL')

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
        table_data = table_data.fillna('NULL')

    if extension == '5':
        print('Tidying .5 file (breeding info)...')

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
        table_data = table_data.fillna('NULL')

    if extension == '6':
        print('Tidying .6 file (footnotes) ...')

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
        table_data = table_data.fillna('NULL')

    return table_data