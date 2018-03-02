def concatenate_text_fields(list_of_fields):
    all_text = ''
    for i in range(len(list_of_fields)):
        if list_of_fields[i]:
            all_text += str(list_of_fields[i])
    return all_text

def review_function(data=conditions, start=0, go=50):
    data = data[start:start+go]
    tricky_strings = []
    i = start
    for item in data:
        print('\n\n\n#######################')
        print(f'#{i}')
        print('#######################')
        pull_race_restrictions(item)
        i += 1
        user_input = input('Enter (t)ricky_string or (q)uit').lower()
        if user_input == 't':
            tricky_strings.append(item)
        elif user_input == 'q':
            break
    return tricky_strings

import re


def pull_race_restrictions(conditions):

    text_to_num_mappings = {
        'A': 1,
        'ONE': 1,
        'TWO': 2,
        'THREE': 3,
        'FOUR': 4,
        'FIVE': 5,
        'SIX': 6,
        'ONCE': 1,
        'TWICE': 2,
        'THREE TIMES': 3,
        'FOUR_TIMES': 4,
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

        'claim_start_req_price': None,
        'claim_start_req_time': None,
        'claim_start_excluded_races': None,
        'optional_claiming_price': None,

        'exceptions_allowed': None,
        'excepted_number_limit': None,
        'excepted_money_limit': None,
        'excepted_time_limit': None,
        'excepted_excluded_races': None,

    }
    #********TO DO: WHAT TO DO IF WE CAN'T FIND THE FULL SENTENCE?***********
    # - Not a major issue--looks like it's not really happening

    # Strip off all commas and the trailing period--these are causing too much parsing complexity and aren't adding anything here.
    conditions = re.sub(r',', '', conditions)
    # Normalize spelling of statebred
    conditions = re.sub(r'(STATE BRED|STATE-BRED)', 'STATEBRED', conditions)

    full_conditions = ''
    try:
        full_conditions = re.search(r'(FOR|TWO|THREE|FOUR)[A-Z0-9 ,$\-()/]+\.', conditions).group(0)
    except AttributeError:
        pass

    # This pulls the restriction sentence out of full race conditions. If blank, there are none.
    try:
        restriction_string = re.search(r'WHICH[A-Z0-9 ,$\-()/]+\.', full_conditions).group(0)
        restrictions_dict['has_restrictions'] = 1
        restrictions_dict['full_condition_slug'] = restriction_string
        print(restriction_string)
    except:
        # If there are no restrictions set 'has_restrictions' to 0 and everything else to None; return the dict
        for key in restrictions_dict:
            restrictions_dict[key] = None
        restrictions_dict['has_restrictions'] = 0

        print(f'Nope: {full_conditions}\n')
        return restrictions_dict

    match = ''

    # Look for an allowance optional claiming amount
    try:
        claiming_amt = re.search(' (FOR A|OR)? (OPTIONAL )?CLAIMING PRICE (OF )?\$([\d \-\$]+)(?=\.)', restriction_string)
        for i in range(len(claiming_amt.regs)):
            print(f'Claiming_amt {i}: {claiming_amt.group(i)}')
        restrictions_dict['optional_claiming_price'] = claiming_amt.group(4)
        restriction_string = restriction_string[:claiming_amt.span(0)[0]] + restriction_string[claiming_amt.span(0)[1]:]
        print(f'Restriction string after claiming amt removal: {restriction_string}')


    except:
        restrictions_dict['optional_claiming_price'] = 0
        print('No optional claiming amount found--using 0')

    # Pull off the first restriction slug
    try:
        match = re.search(r'(((NEVER|NOT) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)?)|HAVE STARTED) (.*?OR (?=(WHICH|CLAIMING|.*BREDS))|.*?\.)?', restriction_string)
        restrictions_dict['restriction_slug'] = match.group(0)
    except:
        pass

    try:
        for i in range(len(match.regs)):
            print(f'Match {i}: {match.group(i)}')
    except:
        print('No match')

    # First parse if this is an optional claiming race
    if re.match(r'HAVE STARTED FOR A CLAIMING PRICE', match.group(0)):
        claim_info = re.search(r'FOR A CLAIMING PRICE OF \$([\d,]+)(.*?(SINCE|IN) (([A-Z ]+)?[0-9, \-]+))?(AND WHICH [A-Z0-9, ]+)?(OR CLAIMING PRICE \$([\d,]+))?', match.group(0))
        try:
            for i in range(len(claim_info.regs)):
                print(f'\tClaim_info {i}: {claim_info.group(i)}')
        except:
            pass

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


        restrictions_dict['claim_start_req_price'] = re.sub(r',', '', claim_info.group(1))
        restrictions_dict['claim_start_req_time'] = claim_info.group(4)
        restrictions_dict['claim_start_excluded_races'] = 'TO DO ITEM!'


    # Then process simple race matches
    elif match:
        if '$' not in match.group(4):
            restrictions_dict['number_limit'] = text_to_num_mappings.get(match.group(4), f'ERROR: {match.group(4)}')
            restrictions_dict['money_limit'] = 0

        if '$' in match.group(4):
            restrictions_dict['money_limit'] = match.group(4)[1:]
            restrictions_dict['number_limit'] = text_to_num_mappings.get(match.group(5), 'ERROR!')
            #*******Need to address number limit with words like ONCE, TWICE, etc.

        # Find the lookback period for race restrictions
        try:
            time_limit = re.search(r'(SINCE|IN) (([A-Z ]+)?[0-9, \-]+)', match.group(6))
            for i in range(len(time_limit.regs)):
                print(f'-Time limit {i}: {time_limit.group(i)}')
            restrictions_dict['time_limit'] = time_limit.group(2)
        except:
            restrictions_dict['time_limit'] = 'Lifetime'
            print('-No specific time limit found--using lifetime')

        # Find race excluded from race restriction calculations
        try:
            excluded_races = re.search(r'OTHER THAN ([A-Z ,]+)', match.group(6))
            for i in range(len(excluded_races.regs)):
                print(f'+Excluded races {i}: {excluded_races.group(i)}')
            restrictions_dict['excluded_races'] = re.sub(r' OR ?$', '', excluded_races.group(1))
        except:
            restrictions_dict['excluded_races'] = 0
            print('+No excluded races found--using 0')









    print('')
    for key, value in restrictions_dict.items():
        print(f'*{key}: {value}')



    print('----------')


