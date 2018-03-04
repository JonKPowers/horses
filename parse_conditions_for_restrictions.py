import re

class conditions_parser:

    def __init__(self):
        self.restrictions_dict_list = {
            'has_restrictions': [],
            'full_condition_slug': [],
            'restriction_slug': [],

            'number_limit': [],
            'money_limit': [],
            'time_limit': [],
            'excluded_races': [],

            'exceptions_allowed': [],

            'excepted_1_number_limit': [],
            'excepted_1_money_limit': [],
            'excepted_1_time_limit': [],
            'excepted_1_excluded_races': [],
            'excepted_2_number_limit': [],
            'excepted_2_money_limit': [],
            'excepted_2_time_limit': [],
            'excepted_2_excluded_races': [],

            'claim_start_req_price': [],
            'claim_start_req_time': [],
            'excepted_1_claim_start_req_price': [],
            'excepted_1_claim_start_req_time': [],
            'excepted_2_claim_start_req_price': [],
            'excepted_2_claim_start_req_time': [],

            'optional_claiming_price': [],
            'left_to_parse': [],
        }

        self.restrictions_dict_nones = {
            'has_restrictions': None,
            'full_condition_slug': None,
            'restriction_slug': None,

            'number_limit': None,
            'money_limit': None,
            'time_limit': None,
            'excluded_races': None,

            'exceptions_allowed': None,

            'excepted_1_number_limit': None,
            'excepted_1_money_limit': None,
            'excepted_1_time_limit': None,
            'excepted_1_excluded_races': None,
            'excepted_2_number_limit': None,
            'excepted_2_money_limit': None,
            'excepted_2_time_limit': None,
            'excepted_2_excluded_races': None,

            'claim_start_req_price': None,
            'claim_start_req_time': None,
            'excepted_1_claim_start_req_price': None,
            'excepted_1_claim_start_req_time': None,
            'excepted_2_claim_start_req_price': None,
            'excepted_2_claim_start_req_time': None,

            'optional_claiming_price': None,
            'left_to_parse': None,
        }

        self.slug_restrictions_dict = {
            'number_limit': None,
            'money_limit': None,
            'time_limit': None,
            'excluded_races': None,

            'claim_start_req_price': None,
            'claim_start_req_time': None,
        }

        self.text_to_num_mappings = {
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

        self.conditions_string = ''
        self.restrictions_string = ''
        self.current_slug = None
        self.match_string_1 = ''
        self.match_string_2 = ''
        self.match_string_3 = ''

    def process_condition_list(self, condition_list):
        for i in range(len(condition_list)):
            print(f'***************\n*{i}\n***************')
            try:
                for key, value in self.pull_race_restrictions(condition_list[i]).items():
                    self.restrictions_dict_list[key].append(value)
            except (TypeError, AttributeError):
                for key in self.restrictions_dict_list.keys():
                    self.restrictions_dict_list[key].append('ISSUE!')
        return self.restrictions_dict_list

    def strip_conditions_string(self):
        """This function cleans up the raw conditions string, removing commas (which have caused some
        issues when parsing) and normalizing the spelling of certain words."""

        # Strip off all commas and the trailing period--these are causing too much parsing complexity and aren't adding anything here.
        self.conditions_string = re.sub(r',', '', self.conditions_string)

        # Normalize spelling of statebred
        self.conditions_string = re.sub(r'(STATE BRED|STATE-BRED)', 'STATEBRED', self.conditions_string)

    def get_restrictions_string(self):
        """This function takes a full string of race conditions and pulls out the sentence containing
        the race restrictions and then pulls from that the sentence fragment containing the non-age
        restrictions. If the sentence fragment is found, return 1; if not, return 0"""

        # Pull the full race restrictions sentence. If not found, return 0.
        try:
            full_conditions = re.search(r'(FOR|TWO|THREE|FOUR)[A-Z0-9 ,$\-()/]+\.', self.conditions_string).group(0)
        except AttributeError:
            print('Full race restrictions not found')
            return 0

        # Pull out the non-age race restrictions and return it. If not found, return 0
        try:
            self.restrictions_string = re.search(r'WHICH[A-Z0-9 ,$\-()/]+\.', full_conditions).group(0)
            return 1
        except AttributeError:
            print('Non-age race restrictions not found')
            return 0

    def get_restrictions_slug(self):
        """Pulls a single set of restrictions from restrictions_string and returns the slug with that
        single set of restrictions"""

        return re.search(
            r'(((NEVER|NOT) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)?)|HAVE STARTED) (.*?OR (?=(WHICH|.*BREDS))|.*?\.)?',
            self.restrictions_string)

    def pull_optional_claiming_amt(self):
        """This function looks for an optional claiming amount at the end of restrictions_string.
        If found, it returns the amount. If not found, it returns 0"""
        claiming_amt = re.search(' (FOR A|OR)? (OPTIONAL )?CLAIMING PRICE (OF )?\$([\d \-\$]+)(?=\.)',
                                 self.restrictions_string)
        try:
            # Print out the match results
            for i in range(len(claiming_amt.regs)):
                print(f'Claiming info {i}: {claiming_amt.group(i)}')

            # Chop the optional claiming amount string off of restrictions_string. Print the post-chopped string
            self.restrictions_string = self.restrictions_string[:claiming_amt.span(0)[0]] + \
                                       self.restrictions_string[claiming_amt.span(0)[1]:]
            print(f'Restriction string after claiming amt removal: {self.restrictions_string}')

            # Return the optional claiming amount with dollar signs removed
            if '-' in claiming_amt.group(4):
                amounts = re.search(r'.*?(\d+).+?(\d+)', claiming_amt.group(4))
                return int(amounts.group(1)) if int(amounts.group(1)) < int(amounts.group(2)) else int(amounts.group(2))

            else:
                return int(claiming_amt.group(4))

        except:
            print('Claiming amount not found')
            return 0

    def get_claiming_restriction(self):
        claiming_match = re.search(
                r'HAVE STARTED FOR A CLAIMING PRICE OF \$(([\d, \-]+) (OR LESS)?) ?(.*?(SINCE|IN) (([A-Z ]+)?[0-9, \-]+))?',
                self.restrictions_string)

        # Make a dict with the match object and its groups, which is returned by this function call
        claim_info = {
            'match' : claiming_match,
        }

        for i in range(len(claiming_match.regs)):
            claim_info[str(i)] = claiming_match.group(i)

        return claim_info

    def get_simple_race_restrictions(self):
        race_restrictions = re.search(r'(NOT|NEVER) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)? ?(RACES?)? ?(OTHER THAN ([A-Z ,]+))? ?((SINCE|IN) (([A-Z ]+)?[0-9 ,\-]+))?',
                                      self.restrictions_string)
        # Make a dict with the match object and its groups, which is returned by this function call
        restriction_info = {
            'match': race_restrictions,
        }

        for i in range(len(race_restrictions.regs)):
            restriction_info[str(i)] = race_restrictions.group(i)

        if race_restrictions.group(7) == None:
            restriction_info['9'] = 'Lifetime'

        return restriction_info

    def parse_restriction_slug(self):

        # Create a restrictions dict for info from parsing this slug.
        slug_restrictions_dict = self.slug_restrictions_dict.copy()

        # Check if there is a claiming-start requirement:
        #
        #   NOTE:   This will NOT catch an 'other than qualifier on the claim-start requirement.
        #           I haven't seen one yet, but it's something to keep an eye on and maybe put some
        #           tests in to catch.
        #
        if re.search(r'HAVE STARTED FOR A CLAIMING PRICE', self.restrictions_string):
            # Set dict entries with claiming-start info
            claim_info = self.get_claiming_restriction()
            for key in claim_info.keys():
                print(f'claim_info[{key}]: {claim_info[key]}')
            slug_restrictions_dict['claim_start_req_price'] =  int(claim_info['2'])
            slug_restrictions_dict['claim_start_req_time'] = claim_info['6']
            # Delete the claiming-start info off the current slug.
            self.restrictions_string = self.restrictions_string[:claim_info['match'].span(0)[0]] + \
                                self.restrictions_string[claim_info['match'].span(0)[1]:]
            # Print post-deletion slug
            print(f'restrictions string after deleting claiming info:\n\t{self.restrictions_string}')
        else:
            print('No claiming-start requirement found')

        if re.search(r'(NOT|NEVER) WON', self.restrictions_string):
            restriction_info = self.get_simple_race_restrictions()
            self.restriction_info = restriction_info
            for key in restriction_info.keys():
                print(f'restriction_info[{key}]: {restriction_info[key]}')
            slug_restrictions_dict['number_limit'] = self.text_to_num_mappings.get(restriction_info['3'] if restriction_info['3'] else restriction_info['2'], 'ERROR!')
            slug_restrictions_dict['money_limit'] = int(re.sub('\$', '', restriction_info['2'])) if '$' in restriction_info['2'] else None
            slug_restrictions_dict['time_limit'] = restriction_info['9']
            slug_restrictions_dict['excluded_races'] = re.sub(r' ?OR ?$', '', restriction_info['6']) if restriction_info['6'] else None
            # Delete the restriction_info match off of current_slug
            self.restrictions_string = self.restrictions_string[:restriction_info['match'].span(0)[0]] + \
                                self.restrictions_string[restriction_info['match'].span(0)[1]:]
            # Print post-deletion slug
            print(f'restrictions_string after deleting restriction info: \n\t{self.restrictions_string}')
        else:
            print('No race restrictions found')

        return slug_restrictions_dict

    def pull_race_restrictions(self, conditions_string):

        # ******TO DO******************
        # (1) capture breeding restrictions in full_restrictions (e.g., "BRED IN FLORIDA, MARYLAND, ...")


        # Set up dict to hold info from the string being processed
        restrictions_dict = self.restrictions_dict_nones.copy()

        # Put the conditions string onto the object
        self.conditions_string = conditions_string
        # Clean up the conditions string
        self.strip_conditions_string()

        # Try to find sentence fragment containing race restrictions from the full race conditions
        # If found, set dict values. If not, set a not-found state and return the dict
        if self.get_restrictions_string():
            restrictions_dict['has_restrictions'] = 1
            restrictions_dict['full_condition_slug'] = self.restrictions_string
            print(self.restrictions_string)
        else:
            # ***************TO DO: Consider whether there is a better 'None-state' for this dict*****************
            print(f'Nope: {self.conditions_string}\n')
            for key in restrictions_dict:
                restrictions_dict[key] = None
            restrictions_dict['has_restrictions'] = 0
            return restrictions_dict

        # Check if there's an optional claiming amount and set the dictionary value
        optional_claiming_amount = self.pull_optional_claiming_amt()
        if optional_claiming_amount:
            restrictions_dict['optional_claiming_price'] = int(optional_claiming_amount)
        else:
            restrictions_dict['optional_claiming_price'] = 0

        # Get the first restriction slug
        self.current_slug = self.get_restrictions_slug()

        # Parse the first restriction slug, delete it from restriction_string, and look for more restriction_strings; parse them if found
        for i in range(3):
            if self.current_slug:
                for j in range(len(self.current_slug.regs)):
                    print(f'Current slug match {j}: {self.current_slug.group(j)}')
                print(f'{i}: Processing slug: {self.current_slug.group(0)}')
                parsed_restrictions = self.parse_restriction_slug()

                print(f'{i}: Slug processed. Attempting to add to restrictions dict')
                for key in parsed_restrictions.keys():
                    restrictions_dict[key if i == 0 else f'excepted_{i}_' + key] = parsed_restrictions[key]

                # Try to get the next restriction slug if there is one
                self.current_slug = self.get_restrictions_slug()

            if i == 2:
                while re.search(r' ?WHICH HAVE ?', self.restrictions_string):
                    strip = re.search(r' ?WHICH HAVE ?', self.restrictions_string)
                    self.restrictions_string = self.restrictions_string[:strip.span(0)[0]] + \
                                               self.restrictions_string[strip.span(0)[1]:]
                restrictions_dict['left_to_parse'] = self.restrictions_string

        print('')
        for key, value in restrictions_dict.items():
            print(f'*{key}: {value}')
        print('----------')

        return restrictions_dict


def parse_race_conditions(condition_list):

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

            'exceptions_allowed': None,

            'excepted_1_number_limit': None,
            'excepted_1_money_limit': None,
            'excepted_1_time_limit': None,
            'excepted_1_excluded_races': None,
            'excepted_2_number_limit': None,
            'excepted_2_money_limit': None,
            'excepted_2_time_limit': None,
            'excepted_2_excluded_races': None,

            'claim_start_req_price': None,
            'claim_start_req_time': None,
            'excepted_1_claim_start_req_price': None,
            'excepted_1_claim_start_req_time': None,
            'excepted_2_claim_start_req_price': None,
            'excepted_2_claim_start_req_time': None,

            'optional_claiming_price': None,
            'left_to_parse': None,
        }

        def parse_restriction_slug(slug_match):
            # First parse if this is an optional claiming race
            slug_restrictions_dict = {
                'number_limit': None,
                'money_limit': None,
                'time_limit': None,
                'excluded_races': None,

                'claim_start_req_price': None,
                'claim_start_req_time': None,
            }

            if re.match(r'HAVE STARTED FOR A CLAIMING PRICE', slug_match.group(0)):
                claim_info = re.search(
                    r'FOR A CLAIMING PRICE OF \$([\d,]+)(.*?(SINCE|IN) (([A-Z ]+)?[0-9, \-]+))?(AND WHICH [A-Z0-9, $]+)?(OR CLAIMING PRICE \$([\d,]+))?',
                    slug_match.group(0))
                try:
                    for i in range(len(claim_info.regs)):
                        print(f'\tClaim_info {i}: {claim_info.group(i)}')
                except:
                    pass

                if claim_info.group(6):
                    claim_restrictions = re.search(
                        r'(NOT|NEVER) WON ([A-Z]+) RACES? ?(OTHER THAN ([A-Z ,]+))? ?((SINCE|IN) (([A-Z ]+)?[0-9 ,\-]+))',
                        claim_info.group(6))
                    if claim_restrictions:
                        slug_restrictions_dict['number_limit'] = text_to_num_mappings.get(claim_restrictions.group(2),
                                                                                          "ERROR!")
                        slug_restrictions_dict['money_limit'] = 'TO DO ITEM!'  # NEED TO SEE IF THIS EVER COMES UP
                        slug_restrictions_dict['time_limit'] = claim_restrictions.group(7)
                        slug_restrictions_dict['excluded_races'] = claim_restrictions.group(4)
                        slug_restrictions_dict['exceptions_allowed'] = 'TO DO ITEM!'
                    try:
                        print('')
                        for i in range(len(claim_restrictions.regs)):
                            print(f'\tClaim_restrictions {i}: {claim_restrictions.group(i)}')
                    except:
                        pass

                    claim_restrictions_money = re.search(
                        r'(NEVER|NOT) WON ([0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)? ?(OTHER THAN ([A-Z ,]+))?',
                        claim_info.group(6))
                    if claim_restrictions_money:
                        slug_restrictions_dict['money_limit'] = claim_restrictions_money.group(2)[1:]
                        slug_restrictions_dict['number_limit'] = text_to_num_mappings.get(
                            claim_restrictions_money.group(3), 'ERROR!')
                        slug_restrictions_dict['excluded_races'] = claim_restrictions_money.group(5)
                        slug_restrictions_dict['time_limit'] = 'TO DO ITEM!'
                    try:
                        print('')
                        for i in range(len(claim_restrictions_money.regs)):
                            print(f'\tClaim_restrictions_money {i}: {claim_restrictions_money.group(i)}')
                    except:
                        pass

                # Set the dictionary values
                slug_restrictions_dict['claim_start_req_price'] = re.sub(r',', '', claim_info.group(1))
                slug_restrictions_dict['claim_start_req_time'] = claim_info.group(4)


            # Then process simple race matches
            elif slug_match:
                if '$' not in slug_match.group(4):
                    slug_restrictions_dict['number_limit'] = text_to_num_mappings.get(slug_match.group(4),
                                                                                      f'ERROR: {match.group(4)}')
                    slug_restrictions_dict['money_limit'] = 0

                if '$' in slug_match.group(4):
                    slug_restrictions_dict['money_limit'] = slug_match.group(4)[1:]
                    slug_restrictions_dict['number_limit'] = text_to_num_mappings.get(slug_match.group(5), 'ERROR!')
                    # *******Need to address number limit with words like ONCE, TWICE, etc.

                # Find the lookback period for race restrictions
                try:
                    time_limit = re.search(r'(SINCE|IN) (([A-Z ]+)?[0-9, \-]+)', slug_match.group(6))
                    for i in range(len(time_limit.regs)):
                        print(f'-Time limit {i}: {time_limit.group(i)}')
                    slug_restrictions_dict['time_limit'] = time_limit.group(2)
                except:
                    slug_restrictions_dict['time_limit'] = 'Lifetime'
                    print('-No specific time limit found--using lifetime')

                # Find race excluded from race restriction calculations
                try:
                    excluded_races = re.search(r'OTHER THAN ([A-Z ,]+)', slug_match.group(6))
                    for i in range(len(excluded_races.regs)):
                        print(f'+Excluded races {i}: {excluded_races.group(i)}')
                    slug_restrictions_dict['excluded_races'] = re.sub(r' OR ?$', '', excluded_races.group(1))
                except:
                    slug_restrictions_dict['excluded_races'] = 0
                    print('+No excluded races found--using 0')

            return slug_restrictions_dict

        # ********TO DO: WHAT TO DO IF WE CAN'T FIND THE FULL SENTENCE?***********
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
            claiming_amt = re.search(' (FOR A|OR)? (OPTIONAL )?CLAIMING PRICE (OF )?\$([\d \-\$]+)(?=\.)',
                                     restriction_string)
            for i in range(len(claiming_amt.regs)):
                print(f'Claiming_amt {i}: {claiming_amt.group(i)}')
            restrictions_dict['optional_claiming_price'] = re.sub('\$', '', claiming_amt.group(4))
            restriction_string = restriction_string[:claiming_amt.span(0)[0]] + restriction_string[
                                                                                claiming_amt.span(0)[1]:]
            print(f'Restriction string after claiming amt removal: {restriction_string}')


        except:
            restrictions_dict['optional_claiming_price'] = 0
            print('No optional claiming amount found--using 0')

        # Pull off the first restriction slug
        try:
            match = re.search(
                r'(((NEVER|NOT) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)?)|HAVE STARTED) (.*?OR (?=(WHICH|.*BREDS))|.*?\.)?',
                restriction_string)
            restrictions_dict['restriction_slug'] = match.group(0)
        except:
            pass

        # Parse the first restriction slug, delete it from restriction_string, and look for more restriction_strings; parse them if found
        for i in range(3):
            if match:
                print(f'{i}: Processing slug')
                try:
                    for j in range(len(match.regs)):
                        print(f'Match {j}: {match.group(j)}')
                except:
                    print('No match')
                parsed_restrictions = parse_restriction_slug(match)
                print(f'{i}: Slug processed. Attempting to add to restrictions dict')
                for key in parsed_restrictions.keys():
                    restrictions_dict[key if i == 0 else f'excepted_{i}_' + key] = parsed_restrictions[key]
                restriction_string = restriction_string[:match.span(0)[0]] + restriction_string[match.span(0)[1]:]
                match = re.search(
                    r'(((NEVER|NOT) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)?)|HAVE STARTED) (.*?OR (?=(WHICH|.*BREDS))|.*?\.)?',
                    restriction_string)
            if i == 2:
                restrictions_dict['left_to_parse'] = restriction_string

        print('')
        for key, value in restrictions_dict.items():
            print(f'*{key}: {value}')
        print('----------')

        return restrictions_dict

    restrictions_dict = {
        'has_restrictions': [],
        'full_condition_slug': [],
        'restriction_slug': [],

        'number_limit': [],
        'money_limit': [],
        'time_limit': [],
        'excluded_races': [],

        'exceptions_allowed': [],

        'excepted_1_number_limit': [],
        'excepted_1_money_limit': [],
        'excepted_1_time_limit': [],
        'excepted_1_excluded_races': [],
        'excepted_2_number_limit': [],
        'excepted_2_money_limit': [],
        'excepted_2_time_limit': [],
        'excepted_2_excluded_races': [],

        'claim_start_req_price': [],
        'claim_start_req_time': [],
        'excepted_1_claim_start_req_price': [],
        'excepted_1_claim_start_req_time': [],
        'excepted_2_claim_start_req_price': [],
        'excepted_2_claim_start_req_time': [],

        'optional_claiming_price': [],
        'left_to_parse': [],
    }

    for i in range(len(condition_list)):
        print(f'***************\n*{i}\n***************')
        try:
            for key, value in pull_race_restrictions(condition_list[i]).items():
                restrictions_dict[key].append(value)
        except (TypeError, AttributeError):
            for key in restrictions_dict.keys():
                restrictions_dict[key].append('ISSUE!')
    return restrictions_dict

