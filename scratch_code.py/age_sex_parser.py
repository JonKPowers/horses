def parse_age_sex_restrictions(restriction_column):

    new_columns = ['allowed_age_two',
                   'allowed_age_three',
                   'allowed_age_four',
                   'allowed_age_five',
                   'allowed_age_older',
                   'allowed_fillies',
                   'allowed_mares',
                   'allowed_colts_geldings',
                   ]

    age_mappings = {
        'AO': ['two'],
        'AU': ['two', 'three', 'four', 'five', 'older'],
        'BO': ['three'],
        'BU': ['three', 'four', 'five', 'older'],
        'CO': ['four'],
        'CU': ['four', 'five', 'older'],
        'DO': ['five'],
        'DU': ['five', 'older'],
        'EO': ['three', 'four'],
        'FO': ['four', 'five'],
        'GO': ['three', 'four', 'five'],
        'HO': ['two', 'three', 'four', 'five', 'older'],
    }

    sex_mappings = {
        'N': ['fillies', 'mares', 'colts_geldings'],
        'M': ['fillies', 'mares'],
        'F': ['fillies'],
        'C': ['colts_geldings'],
    }

    new_column_dict = dict.fromkeys(new_columns)
    for key in new_column_dict:
        new_column_dict[key] = [0 for _ in range(len(restriction_column))]


    for i in range(len(restriction_column)):
        age_sex_string = restriction_column[i]
        age_code = age_sex_string[:2]
        sex_code = age_sex_string[2:]
        for item in age_mappings[age_code]:
            new_column_dict[f'allowed_age_{item}'][i] = 1
        for item in sex_mappings[sex_code]:
            new_column_dict[f'allowed_{item}'][i] = 1

    return new_column_dict