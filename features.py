import numpy as np
import re


def parse_conditions(condition_string):
    race_info = {
        'cond_race_class': 'NULL',
        'purse_string': 'NULL',
        'purse': 'NULL',
        'race_conditions': 'NULL',
        'weight_info': 'NULL',
        'standard_weight': 'NULL',
        'three_yo_weight': 'NULL',
        'cond_rail_distance': 'NULL',
        'weight_allowance_0_amt': 'NULL',
        'weight_allowance_0_condition': 'NULL',
        'weight_allowance_1_amt': 'NULL',
        'weight_allowance_1_condition': 'NULL',
        'weight_allowance_2_amt': 'NULL',
        'weight_allowance_2_condition': 'NULL',
        'weight_allowance_3_amt': 'NULL',
        'weight_allowance_3_condition': 'NULL',
        'cond_left_on_string': 'NULL',
    }

    # Race class
    try:
        race_class = re.match(r'[\w. ]+(?=\. )', condition_string)
        race_info['cond_race_class'] = race_class.group(0).strip()
        condition_string = condition_string[:race_class.regs[0][0]] + \
                           condition_string[race_class.regs[0][1]:]
        condition_string = condition_string[2:]
    except AttributeError:
        pass

    # Race purse info
    try:
        purse_data = re.match('Purse \$([\d;]+) (\(.+?\) )?', condition_string)
        all_purse_data = re.sub(';', '', purse_data.group(0))
        race_info['purse'] = re.sub(';', '', purse_data.group(1))
        race_info['purse_string'] = all_purse_data
        condition_string = condition_string[purse_data.end(0):]
    except AttributeError:
        pass

    # Race conditions
    try:
        race_conditions = re.match(r'[A-Z0-9 ;\$-]+. ', condition_string)
        condition_string = condition_string[race_conditions.end(0):]
    except AttributeError:
        pass

    # Weight amounts
    try:
        weight_info = re.search(r'(Weight|Three).+?\.( |$)', condition_string)
        # print(weight_info.group(0))
        race_info['weight_info'] = weight_info.group(0)

    except AttributeError:
        pass

        # Single-weight amount
    try:
        one_weight = re.match(r'[Ww]eight.+?(\d+)', weight_info.group(0))
        race_info['standard_weight'] = one_weight.group(1)
    except AttributeError:
        pass

        # Special 3-year-old weight amount
    try:
        three_yo_weights = re.search(r'[Tt]hree.+?(\d+).+?(\d+)', condition_string)
        race_info['three_yo_weight'] = three_yo_weights.group(1)
        race_info['standard_weight'] = three_yo_weights.group(2)
    except AttributeError:
        pass

    try:
        condition_string = condition_string[:weight_info.regs[0][0]] + condition_string[weight_info.regs[0][1]:]
    except AttributeError:
        pass

    # Rail distance
    try:
        rail_info = re.search(r'\(?[Rr]ail.+?(\d+).*\.', condition_string)
        # print(rail_info.group(0), rail_info.group(1))
        race_info['cond_rail_distance'] = rail_info.group(1)
        condition_string = condition_string[:rail_info.regs[0][0]] + condition_string[rail_info.regs[0][1]:]
    except AttributeError:
        pass

    # Weight allowances
    i = 0
    while re.search(r'[^.]* [Aa]llowed \d+ [^.]*\.', condition_string):
        weight_allowance = re.search(r'[^.]* [Aa]llowed (\d+)[^.]*\.', condition_string)
        # print(weight_allowance.group(0))
        condition_string = condition_string[:weight_allowance.regs[0][0]] + \
                           condition_string[weight_allowance.regs[0][1]:]
        race_info[f'weight_allowance_{i}_amt'] = weight_allowance.group(1)
        race_info[f'weight_allowance_{i}_condition'] = weight_allowance.group(0)[:255]
        i += 1
    del i

    race_info['cond_left_on_string'] = condition_string

    return race_info


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
        try:
            for item in age_mappings[age_code]:
                new_column_dict[f'allowed_age_{item}'][i] = 1
        except KeyError:
            for item in age_mappings['HO']:
                new_column_dict[f'allowed_age_{item}'][i] = 'NULL'

        try:
            for item in sex_mappings[sex_code]:
                new_column_dict[f'allowed_{item}'][i] = 1
        except KeyError:
            for item in sex_mappings['N']:
                new_column_dict[f'allowed_{item}'][i] = 'NULL'

    return new_column_dict

def add_features (table_data, extension):
    extension = str(extension)
    if extension == '1':
        print('Adding features to .1 file ...')
        # Parse and flatten age/sex restriction codes
        for key, value in parse_age_sex_restrictions(table_data['age_sex_restrictions']).items():
            table_data[key] = value

    if extension == '2':
        print('Adding features to .2 file ...')

        # ************************************************
        # Flatten medication codes into individual columns
        #
        medication_col = table_data.columns.get_loc('medication_codes')
        bleeder_meds = [0 for _ in range(len(table_data))]
        bute = [0 for _ in range(len(table_data))]
        lasix = [0 for _ in range(len(table_data))]
        for i in range(len(table_data)):
            code = table_data.iloc[i, medication_col].upper()
            if 'A' in code:
                bleeder_meds[i] = 1
            if 'B' in code or 'C' in code:
                bute[i] = 1
            if 'L' in code or 'M' in code:
                lasix[i] = 1
        table_data['meds_adjunct_bleeder'] = bleeder_meds
        table_data['meds_bute'] = bute
        table_data['meds_lasix'] = lasix

        # ***********************************************
        # Flatten equipment codes into individual columns
        #
        equipment_col = table_data.columns.get_loc('equipment_code')
        equipment_list = {
            '1': 'running_ws',
            '2': 'screens',
            '3': 'shields',
            'A': 'aluminum_pads',
            'B': 'blinkers',
            'C': 'mud_calks',
            'D': 'glued_shoes',
            'E': 'inner_rims',
            'F': 'front_bandages',
            'G': 'goggles',
            'H': 'outer_rims',
            'I': 'inserts',
            'J': 'aluminum_pad',
            'K': 'flipping_halter',
            'L': 'bar_shoes',
            'M': 'blocks',
            'N': 'no_whip',
            'O': 'blinkers_off',
            'P': 'pads',
            'Q': 'nasal_strip_off',
            'R': 'bar_shoe',
            'S': 'nasal_strip',
            'T': 'turndowns',
            'U': 'spurs',
            'V': 'cheek_piece',
            'W': 'queens_plates',
            'X': 'cheek_piece_off',
            'Y': 'no_shoes',
            'Z': 'tongue_tie',
        }
        equipment_dict = dict.fromkeys(list(equipment_list.values()))
        for key in equipment_dict.keys():
            equipment_dict[key] = [0 for _ in range(len(table_data))]

        for i in range(len(table_data)):
            code = table_data.iloc[i, equipment_col]
            if code == 'NULL':
                continue
            for letter in code:
                equipment_dict[equipment_list[letter]][i] = 1
        for key, value in equipment_dict.items():
            table_data[key] = value

        # ***********************************************
        # Combine lead/beaten lengths columns into single column,
        # with a positive value for the leader and a negative
        # value for all trailing horses
        calls = ['start', '1st_call', '2d_call', '3d_call', 'stretch_call', 'finish']
        for call in calls:
            column_data = []
            lead_column = table_data.columns.get_loc(f'{call}_lead')
            beaten_column = table_data.columns.get_loc(f'{call}_beaten')
            for i in range(len(table_data)):
                if table_data.iloc[i, lead_column] != 'NULL':
                    column_data.append(table_data.iloc[i, lead_column])
                elif table_data.iloc[i, beaten_column] == 'NULL':
                    column_data.append('NULL')
                elif table_data.iloc[i, beaten_column] == 0:
                    column_data.append('NULL')
                elif table_data.iloc[i, beaten_column] != 0:
                    column_data.append(table_data.iloc[i, beaten_column] * -1)
                else:
                    print(f'logic leak\nRow: {i}')
            table_data[f'lead_or_beaten_lengths_{call}'] = column_data


    if extension == '3':
        print('Adding features to .3 file ...')
    if extension == '4':
        print('Adding features to .4 file ...')
    if extension == '5':
        print('Adding features to .5 file ...')
    if extension == '6':
        print('Adding features to .6 file ...')
    if extension == 'DRF':
        print('Adding features to .DRF file ...')

        # Flatten medication column (this is a data_column_{} entry)
        for i in range(1, 11):
            medication_col = table_data.columns.get_loc(f'past_medication_{i}')
            bute = [0 for _ in range(len(table_data))]
            lasix = [0 for _ in range(len(table_data))]

            for j in range(len(table_data)):
                if table_data.iloc[j, medication_col] == 1:
                    lasix[j] = 1
                if table_data.iloc[j, medication_col] == 2:
                    bute[j] = 1
                if table_data.iloc[j, medication_col] == 3:
                    lasix[j] = 1
                    bute[j] = 1
            table_data[f'past_medication_{i}_lasix'] = lasix
            table_data[f'past_medication_{i}_bute'] = bute

        # ***********************************************
        # Combine lead/beaten lengths columns into single column,
        # with a positive value for the leader and a negative
        # value for all trailing horses

        calls = ['start', 'first_call', 'second_call', 'stretch_call', 'finish']
        for call in calls:
            for j in range(1, 11):
                column_data = []
                lead_beaten_col = table_data.columns.get_loc(f'past_lead_margin_{call}_{j}')
                beaten_only_col = table_data.columns.get_loc(f'past_beaten_lengths_{call}_{j}')

                for i in range(len(table_data)):
                    if table_data.iloc[i, beaten_only_col] != 'NULL':
                        column_data.append(table_data.iloc[i, beaten_only_col] * -1)
                    else:
                        column_data.append(table_data.iloc[i, lead_beaten_col])
                table_data[f'past_lead_or_beaten_lengths_{call}_{j}'] = column_data

        # ***********************************************
        # Parse the race conditions to add:
        #   (1) weight allowance conditions:
        #       - weight_allowance_0_amt
        #       - weight_allowance_0_condition
        #       - weight_allowance_0_amt
        #       - weight_allowance_0_condition
        #       - weight_allowance_0_amt
        #       - weight_allowance_0_condition
        #       - weight_allowance_0_amt
        #       - weight_allowance_0_condition
        # (2) weight conditions:
        #       - standard_weight
        #       - three_yo_weight
        # (3) race_class (probably duplicative of other previously provided columns)
        #       - cond_race_class
        # (4) rail distance (to confirm with previously provided column)
        #       - cond_rail_distance
        # (5) remaining unparsed portion of conditions string (for diagnostic purposes)
        #       - cond_left_on_string
        condition_fields = {
            'cond_race_class': [],
            'standard_weight': [],
            'three_yo_weight': [],
            'cond_rail_distance': [],
            'weight_allowance_0_amt': [],
            'weight_allowance_0_condition': [],
            'weight_allowance_1_amt': [],
            'weight_allowance_1_condition': [],
            'weight_allowance_2_amt': [],
            'weight_allowance_2_condition': [],
            'weight_allowance_3_amt': [],
            'weight_allowance_3_condition': [],
            'cond_left_on_string': [],
        }

        for i in range(len(table_data)):
            condition_string = ''
            for j in range(1, 7):
                if table_data[f'race_conditions_{j}'][i] != 'NULL':
                    condition_string += str(table_data[f'race_conditions_{j}'][i])
                # print(condition_string)
            parsed_data = parse_conditions(condition_string)
            for key in condition_fields.keys():
                condition_fields[key].append(parsed_data[key])
        for key, value in condition_fields.items():
            table_data[key] = value

        # Parse and flatten age_sex_restriction codes, both for current race
        # and for past performance races

        for key, value in parse_age_sex_restrictions(table_data['age_sex_restricts']).items():
            table_data[key] = value

        for i in range(1, 11):
            for key, value in parse_age_sex_restrictions(table_data[f'past_age_sex_restrictions_{i}']).items():
                table_data[f'past_{key}_{i}'] = value

    return table_data


