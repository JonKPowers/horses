# ----------------------------------------------------------------
#   Items to do for processing csv/pd.df items
#       (1) .1--about_dist_flag should be changed to 0 or 1 (from NaN or 'A')

def tidy_it_up(table_data, extension):
    extension = str(extension)
    if extension == '1':
        print('Tidying .1 file ...')

        # *********************************************
        # Field with [value]/NaN flags
        # TO DO:
        #   (1) Run through these columns and replace the flags with int(1)

        table_data['about_dist_flag'] = table_data['about_dist_flag'].fillna(0)

        table_data['all_weather_flag'] = table_data['all_weather_flag'].fillna(0)

        table_data['chute_start_flag'] = table_data['chute_start_flag'].fillna(0)

        table_data['off_turf_flag'] = table_data['off_turf_flag'].fillna(0)



        # *********************************************
        # Field with binary flags
        # *********************************************
        # Fill the rest with 'NULL'
        table_data = table_data.fillna('NULL')

    if extension == '2':
        print('Tidying .2 file ...')

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
        print('Tidying .3 file ...')

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

    if extension == '3':
        print('Tidying .3 file ...')

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
        print('Tidying .4 file ...')

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
        print('Tidying .5 file ...')

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
        print('Tidying .6 file ...')

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