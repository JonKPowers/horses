def concatenate_text_fields(list_of_fields):
    all_text = ''
    for i in range(len(list_of_fields)):
        if list_of_fields[i]:
            all_text += str(list_of_fields[i])
    return all_text

import re


def pull_race_restrictions(conditions):

    print('#######################')
    print('#')
    print('#######################')

    text_to_num_mappings = {
        'A': 1,
        'ONE': 1,
        'TWO': 2,
        'THREE': 3,
        'FOUR': 4,
        'FIVE': 5,
        'SIX': 6,
    }

    # ******TO DO******************
    # (1) capture breeding restrictions in full_restrictions (e.g., "BRED IN FLORIDA, MARYLAND, ...")


    restrictions_dict = {
        'has_restrictions': None,
        'full_condition_slug': None,
        'restriction_slug': None,

        'number_limit': None,
        'money_limit': None,
        'time_limit': None,
        'excluded_races': None,
        'exceptions_allowed': None,

        'claiming_price_threshold': None,
        'claiming_price_time_limit': None,
        'claiming_excluded_races': None,
        'optional_claiming_price': None,

    }
    #********TO DO: WHAT TO DO IF WE CAN'T FIND THE FULL SENTENCE?***********
    # - Not a major issue--looks like it's not really happening
    full_conditions = ''
    try:
        full_conditions = re.search(r'(FOR|TWO|THREE|FOUR)[A-Z0-9 ,$\-()/]+\.', conditions).group(0)
    except AttributeError:
        pass

    # This pulls the restriction sentence out of full race conditions. If blank, there are none.
    try:
        past_restrictions = re.search(r'WHICH[A-Z0-9 ,$\-()/]+\.', full_conditions).group(0)
        restrictions_dict['has_restrictions'] = 1
        restrictions_dict['full_condition_slug'] = past_restrictions
        print(past_restrictions)
    except:
        # If there are no restrictions set 'has_restrictions' to 0 and everything else to None; return the dict
        for key in restrictions_dict:
            restrictions_dict[key] = None
        restrictions_dict['has_restrictions'] = 0

        print(f'Nope: {full_conditions}\n')
        return restrictions_dict

    match = ''
    try:
        match = re.search(r'(((NEVER|NOT) WON ([A-Z0-9$,]+))|HAVE STARTED) (.*?OR (?=(WHICH|CLAIMING|.*BREDS))|.*?\.)', past_restrictions)
        restrictions_dict['restriction_slug'] = match.group(0)
    except:
        pass

    try:
        print(f'Group 0: {match.group(0)}\nGroup 1: {match.group(1)}\nGroup 2: {match.group(2)}\nGroup 3: {match.group(3)}\nGroup 4: {match.group(4)}\nGroup 5: {match.group(5)}\nGroup 6: {match.group(6)}\n')

        # Parse simple race conditions:

        if match.group(3) == 'NEVER':
            restrictions_dict['time_limit'] = 'Lifetime'

        if '$' not in match.group(4):
            restrictions_dict['number_limit'] = text_to_num_mappings.get(match.group(4), f'ERROR: {match.group(4)}')
            time_limit = re.search(r'(SINCE|IN) (([A-Z ]+)?[0-9, \-]+)', match.group(5))
            for i in range(len(time_limit.regs)):
                print(f'-Time limit {i}: {time_limit.group(i)}')
            restrictions_dict['time_limit'] = time_limit.group(2)
    except:
        print('No match')






    # Parsing procedure for optional claiming races
    if re.match(r'HAVE STARTED FOR A CLAIMING PRICE', match.group(0)):
        claim_info = re.search(r'FOR A CLAIMING PRICE OF \$([\d,]+)(.*?(SINCE|IN) (([A-Z ]+)?[0-9, \-]+))?(AND WHICH [A-Z0-9, ]+)?(OR CLAIMING PRICE \$([\d,]+))?', match.group(0))
        try:
            for i in range(len(claim_info.regs)):
                print(f'\tClaim_info {i}: {claim_info.group(i)}')
        except:
            pass

        if claim_info.group(7):
            restrictions_dict['optional_claiming_price'] = re.sub(',', '', claim_info.group(8))

        if claim_info.group(6):
            claim_restrictions = re.search(r'(NOT|NEVER) WON ([A-Z]+) RACES? ?(OTHER THAN ([A-Z ,]+))? ?((SINCE|IN) (([A-Z ]+)?[0-9 ,\-]+))', claim_info.group(6))
            if claim_restrictions:
                restrictions_dict['number_limit'] = text_to_num_mappings.get(claim_restrictions.group(2), "ERROR!")
                restrictions_dict['money_limit'] = 'TO DO ITEM!'  # NEED TO SEE IF THIS EVER COMES UP
                restrictions_dict['time_limit'] = claim_restrictions.group(7)
                restrictions_dict['excluded_races'] = claim_restrictions.group(4)
                restrictions_dict['exceptions_allowed'] = 'TO DO ITEM!'
            try:
                print('')
                for i in range(len(claim_restrictions.regs)):
                    print(f'\tClaim_restrictions {i}: {claim_restrictions.group(i)}')
            except:
                pass

        # Set the dictionary values


        restrictions_dict['claiming_price_threshold'] = re.sub(r',', '', claim_info.group(1))
        restrictions_dict['claiming_price_time_limit'] = claim_info.group(4)
        restrictions_dict['claiming_excluded_races'] = 'TO DO ITEM!'
        restrictions_dict['optional_claiming_price'] = 'TO DO ITEM!'


    print('')
    for key, value in restrictions_dict.items():
        print(f'*{key}: {value}')



    print('----------')


