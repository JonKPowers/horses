def add_features (table_data, extension):
    extension = str(extension)
    if extension == '1':
        print('Adding features to .1 file ...')
    if extension == '2':
        print('Adding features to .2 file ...')

        # Flatten medication codes into individual columns
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

        # Flatten equipment codes into individual columns
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
            'V': 'equipment_item',
            'W': 'queens_plates',
            'X': 'equipment_item_2',
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
    return table_data


