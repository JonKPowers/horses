def concatenate_text_fields(list_of_fields):
    all_text = ''
    for i in range(len(list_of_fields)):
        if list_of_fields[i]:
            all_text += str(list_of_fields[i])
    return all_text

import re

def pull_race_restrictions(conditions):
    full_restrictions = ''
    try:
        full_restrictions = re.search(r'(FOR|TWO|THREE|FOUR)[A-Z0-9 ,$\-()/]+\.', conditions).group(0)
    except AttributeError:
        pass
    print(full_restrictions)

    past_restrictions = ''
    try:
        past_restrictions = re.search(r'WHICH[A-Z0-9 ,$\-()/]+\.', full_restrictions).group(0)
    except:
        pass
    print(past_restrictions)

    match = ''
    try:
        match = re.search(r'(((NEVER|NOT) WON ([A-Z0-9$,]+))|HAVE STARTED) (.*?OR (?=(WHICH|CLAIMING|.*BREDS))|.*?\.)', past_restrictions)
    except:
        pass
    try:
        print(f'Group 0: {match.group(0)}\nGroup 1: {match.group(1)}\nGroup 2: {match.group(2)}\nGroup 3: {match.group(3)}\nGroup 4: {match.group(4)}\nGroup 5: {match.group(5)}\nGroup 6: {match.group(6)}\n')
    except:
        print('No match')

    print('----------')
