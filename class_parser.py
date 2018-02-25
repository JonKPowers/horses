import re
import pandas as pd

class_fields = [
    'maiden',
    'maiden_special_weight',
    'claiming',
    'allowance',
    'optional_claiming',
    'other',
    
    'fillies_only',
    'statebred_race',

    'claimed_from_race',

]

race_type_mappings = {
    'mdspwt': 'maiden_special_weight',
    'md': 'maiden',
    'clm': 'claiming',
    'oc': 'optional_claiming',
    'moc': 'maiden_optional_claiming',
    'alw': 'allowance',
    'G': 'graded_stakes',
    'futtrl': 'futurity_trail',
    'dbytrl': 'derby_trail',
    'hcp': 'handicap',
    'named': 'named_race',

}


def parse_race_class(class_string):
    race_data = dict.fromkeys(class_fields, 0)

    match = re.search(r'^[fs]', class_string.lower())
    while match is not None:
        try:
            print('trying')
            if match.group(0) == 'f':
                race_data['fillies_only'] = 1
            elif match.group(0) == 's':
                race_data['statebred_race'] = 1
            class_string = re.sub(match.group(0), '', class_string.lower())
        except:
            pass
        match = re.search(r'^[fs]', class_string.lower())

    match = re.match(r'^[A-Za-z]+(?=\d)?', class_string)


def test_parse(input_list):
    parsed_list = []
    restriction_codes = []
    field_order = ['string',

                   'fillies_only',
                   'statebred',
                   'other_restrictions',
                   'claimed_from_race',
                   'race_type',
                   'race_name',
                   'claiming_amt',
                   'purse',
                   'stakes_grade',

                   'restriction_slug',
                   'errors',
                   'never_won',
                   'life_restriction',
                   'time_restriction',
                   'mile_or_more_restriction',
                   'exceptions_allowed',
                   'three_year_olds_exempt',
                   'v_race_restriction',
                   'alw_no_conditions',
                   'alw_with_conditions',
                   ]
    for i in range(len(input_list)):
        class_info = {
            'string': None,
            'fillies_only': 0,
            'statebred': 0,
            'other_restrictions': 0,
            'claimed_from_race': 0,
            'race_type': None,
            'race_name': None,
            'stakes_grade': None,

            'purse': None,
            'claiming_amt': None,

            'alw_no_conditions': None,
            'alw_with_conditions': None,

            'restriction_slug': None,
            'never_won': None,
            'life_restriction': None,
            'time_restriction': None,
            'mile_or_more_restriction': None,
            'v_race_restriction': None,

            'three_year_olds_exempt': 0,
            'exceptions_allowed': None,
            'errors': '',
        }

        lookup_map = {
            'x': 'exceptions_allowed',
            'l': 'life_restriction',
            'y': 'time_restriction',
            'b': 'three_year_olds_exempt',
            'c': 'claimed_from_race',
            'm': 'mile_or_more',
            'v': 'v_race_restriction'
        }

        class_string = input_list[i]
        if class_string is None:
            continue

        print(f'{i}: {class_string}')
        class_string = re.sub(r'\s+', '', class_string)
        class_info['string'] = class_string

        if re.search(r'-G\d$', class_string):
            class_info['race_type'] = race_type_mappings.get('G', f'Bad lookup: {class_string}')
            class_info['stakes_grade'] = re.search(r'-G(\d)', class_string).group(1)

            # Need to set the race grade. Can probably skip the race name since that's provided elsewhere.
            parsed_list.append([class_info[field] for field in field_order])
            continue

        # Pull off modifiers from beginning of class abbreviation
        try:
            match = re.search(r'^[fsr]', class_string).group(0)
            while match is not None:
                if match == 'f':
                    class_info['fillies_only'] = 1
                elif match == 's':
                    class_info['statebred'] = 1
                elif match == 'r':
                    class_info['other_restrictions'] = 1
                class_string = re.sub(match, '', class_string, count = 1)
                match = re.search(r'^[fsr]', class_string).group(0)
        except AttributeError:
            pass

        # Pull off the general race type
        try:
            if re.search(r'hcp|handicap', class_string.lower()):
                class_match = 'hcp'
            elif re.search(r'[A-Za-z./]+\d+[kK]', class_string):
                class_match = 'named'
                class_info['race_name'] = re.match(r'^[A-Za-z]+(?=\d)?', class_string).group(0)
            else:
                class_match = re.match(r'^[A-Za-z]+(?=\d)?', class_string).group(0)
            print(class_match)
            class_info['race_type'] = race_type_mappings.get(class_match.lower(), f'Bad lookup: {class_match}')
            class_string = re.sub(class_match, '', class_string, count=1)
        except:
            pass

        # while re.search(r'(b(nc)?|(?<!n)c)$', class_string):
        #     try:
        #         if re.search(r'b$', class_string).group(0):
        #             class_info['three_year_olds_exempt'] = 1
        #             class_string = re.sub(r'b$', '', class_string)
        #     except AttributeError:
        #         pass
        #
        #     try:
        #         if re.search(r'(?<!n)c$', class_string).group(0):
        #             class_info['claimed_from_race'] = 1
        #             class_string = re.sub(r'(?<!n)c$', '', class_string)
        #     except AttributeError:
        #         pass


        # ************Maiden/Claiming/OC specific code
        if class_info['race_type'] in ['maiden', 'claiming', 'optional_claiming', 'maiden_optional_claiming',
                                       'futurity_trail', 'derby_trail']:
            # Claiming amount information
            amt_match = re.match(r'\d+', class_string).group(0)
            class_info['claiming_amt'] = amt_match
            class_string = re.sub(amt_match, '', class_string, count=1)
            # Race restrictions--pull slug and then parse it
            try:
                restriction_slug = re.match(r'[nr].*$', class_string).group(0)
                class_info['restriction_slug'] = restriction_slug
            except AttributeError:
                pass

            if re.match(r'n', class_string):
                class_info['never_won'] = class_string[1]
                try:
                    column = lookup_map[class_string[2]]
                    class_info[column] = 1
                except IndexError:
                    pass
                except KeyError:
                    class_info['errors'] += f'Bad restriction letter: {letter}'
                class_string = class_string[3:]

            if class_string:
                for letter in class_string:
                    try:
                        column = lookup_map[letter]
                        class_info[column] = 1
                    except KeyError:
                        class_info['errors'] += f'Bad restriction letter: {letter}'

        # ************Allowance parsing**********************
        if class_info['race_type'] == 'allowance':
            # Purse amount
            try:
                amt_match = re.match(r'\d+', class_string).group(0)
            except:
                class_info['purse'] = f'Error: {class_string}'

            class_info['purse'] = amt_match
            class_string = re.sub(amt_match, '', class_string, count=1)
            # Race Restrictions
            try:
                restriction_slug = re.match(r'[nr].*$', class_string).group(0)
                class_info['restriction_slug'] = restriction_slug

                if restriction_slug == 'nc':
                    class_info['alw_no_conditions'] = 1
                elif restriction_slug == 'c':
                    class_info['alw_with_conditions'] = 1
                else:
                    try:
                        never_won = re.search(r'(?<=n)\d', class_string).group(0)
                        class_info['never_won'] = never_won
                    except AttributeError:
                        pass

                    try:
                        restriction_type = re.search(r'(?<=n\d)[A-Za-z]+', class_string).group(0)
                        for letter in restriction_type:
                            try:
                                column = lookup_map[letter]
                                class_info[column] = 1
                            except KeyError:
                                print('Error!')
                                class_info['errors'] = f'Bad restriction letter: {letter}'
                    except AttributeError:
                        pass
            except AttributeError:
                pass

        if class_info['race_type'] == 'handicap':
            try:
                class_info['purse'] = int(re.search(r'[A-Za-z./]+(\d+)[kK]?', class_string).group(1))
                print(re.search(r'[A-Za-z./]+(\d+)[kK]', class_string).group(1))
            except AttributeError:
                pass

        if class_info['race_type'] == 'named_race':
            try:
                class_info['purse'] = (int(re.search(r'[A-Za-z./]+(\d+)[kK]', class_string).group(1)) * 1000)
            except AttributeError:
                pass

        parsed_list.append([class_info[field] for field in field_order])
    return pd.DataFrame(parsed_list, columns=field_order), restriction_codes