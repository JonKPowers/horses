import re
from datetime import datetime
from dateutil import relativedelta


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
            'claim_start_req_time_limit': [],
            'excepted_1_claim_start_req_price': [],
            'excepted_1_claim_start_req_time_limit': [],
            'excepted_2_claim_start_req_price': [],
            'excepted_2_claim_start_req_time_limit': [],

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
            'claim_start_req_time_limit': None,
            'excepted_1_claim_start_req_price': None,
            'excepted_1_claim_start_req_time_limit': None,
            'excepted_2_claim_start_req_price': None,
            'excepted_2_claim_start_req_time_limit': None,

            'optional_claiming_price': None,
            'left_to_parse': None,
        }

        self.slug_restrictions_dict = {
            'number_limit': None,
            'money_limit': None,
            'time_limit': None,
            'excluded_races': None,

            'claim_start_req_price': None,
            'claim_start_req_time_limit': None,
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
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
        }

        self.excluded_race_types = [
            'CLAIMING',
            'MAIDEN',
            'OPTIONAL',
            'RESTRICTED ALLOWANCE',
            'RESTRICTED',
            'STARTER',
            'STATEBRED ALLOWANCE',
            'STATEBRED STAKES',
            'STATEBRED',
            'TRIAL',
            'WAIVER CLAIMING',
            'WAIVER',
            'STATE SIRED STAKES',
            'STATE SIRED',
        ]
        self.exceptions_list = [
            '',
            'excepted_1_',
            'excepted_2_',
            'claim_start_req_'
        ]

        self.conditions_string = ''
        self.restrictions_string = ''
        self.current_slug = None
        self.current_slug_text = ''
        self.current_slug_span_start = None

    def process_condition_list(self, condition_list, date_list):

        self.processed_restrictions_dict = self.restrictions_dict_list.copy()
        self.date_list = date_list

        for i in range(len(condition_list)):
            print(f'***************\n*{i}\n***************')
            try:
                for key, value in self.pull_race_restrictions(condition_list[i]).items():
                    self.processed_restrictions_dict[key].append(value)
            except (TypeError, AttributeError):
                for key in self.processed_restrictions_dict.keys():
                    self.processed_restrictions_dict[key].append('ISSUE!')

        self.process_date_info()
        for key, value in self.date_info.items():
            self.processed_restrictions_dict[key] = value

        return self.processed_restrictions_dict

    def strip_conditions_string(self):
        """This function cleans up the raw conditions string, removing commas (which have caused some
        issues when parsing) and normalizing the spelling of certain words."""

        # Strip off all commas and the trailing period--these are causing too much parsing complexity and aren't adding anything here.
        self.conditions_string = re.sub(r',', '', self.conditions_string)

        # Strip out double spaces
        while re.search(r' {2}', self.conditions_string):
            self.conditions_string = re.sub(r' {2}', ' ', self.conditions_string)

        # Normalize spelling of statebred, allowance, and XX bred State-Name Bred
        self.conditions_string = re.sub(r'(STATE BRED|STATE-BRED)', 'STATEBRED', self.conditions_string)
        self.conditions_string = re.sub(r'ALLOWANCES', 'ALLOWANCE', self.conditions_string)
        self.conditions_string = re.sub(r' ALW ', ' ALLOWANCE ', self.conditions_string)
        self.conditions_string = re.sub(r' [A-Z]{2} BRED', ' STATEBRED', self.conditions_string)
        self.conditions_string = re.sub(r'(ALABAMA|ALASKA|ARIZONA|ARKANSAS|CALIFORNIA|COLORADO|CONNECTICUT|DELAWARE'
                                        r'|FLORIDA|GEORGIA|HAWAII|IDAHO|ILLINOIS|INDIANA|IOWA|KANSAS|KENTUCKY'
                                        r'|LOUISIANA|MAINE|MARYLAND|MASSACHUSETTS|MICHIGAN|MINNESOTA|MISSISSIPPI'
                                        r'|MISSOURI|MONTANA|NEBRASKA|NEVADA|NEW HAMPSHIRE|NEW JERSEY|NEW MEXICO'
                                        r'|NEW YORK|NORTH CAROLINA|NORTH DAKOTA|OHIO|OKLAHOMA|OREGON|PENNSYLVANIA'
                                        r'|RHODE ISLAND|SOUTH CAROLINA|SOUTH DAKOTA|TENNESSEE|TEXAS|UTAH|VERMONT'
                                        r'|VIRGINIA|WASHINGTON|WEST VIRGINIA|WISCONSIN|WYOMING) BRED',
                                        'STATEBRED', self.conditions_string)
        self.conditions_string = re.sub(r' [A-Z]{2} SIRED', 'STATE SIRED', self.conditions_string)

        # Fix misspellings
        self.conditions_string = re.sub(r'JANURARY', 'JANUARY', self.conditions_string)

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
            r'(((NEVER|NOT) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)?)|HAVE STARTED) (.*?OR (?=(WHICH|NEVER|.*BREDS))|.*?\.)?',
            self.restrictions_string)

    def pull_optional_claiming_amt(self):
        """This function looks for an optional claiming amount at the end of restrictions_string.
        If found, it returns the amount. If not found, it returns 0"""
        claiming_amt = re.search(' (FOR A|OR)? (OPTIONAL )?CLAIMING (PRICE )?(OF )?\$([\d \-\$]+)(?=\.)',
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
            if '-' in claiming_amt.group(5):
                amounts = re.search(r'.*?(\d+).+?(\d+)', claiming_amt.group(5))
                return int(amounts.group(1)) if int(amounts.group(1)) < int(amounts.group(2)) else int(amounts.group(2))

            else:
                return int(claiming_amt.group(5))

        except:
            print('Claiming amount not found')
            return 0

    def get_claiming_restriction(self):
        claiming_match = re.search(
                r'HAVE STARTED FOR A CLAIMING PRICE OF \$(([\d, \-]+) (OR LESS)?) ?'
                r'(.*?(BETWEEN|SINCE|IN) (([A-Z ]+)?[0-9, \-]+))?',
                self.current_slug_text)

        # Make a dict with the match object and its groups, which is returned by this function call
        claim_info = {
            'match': claiming_match,
        }

        for i in range(len(claiming_match.regs)):
            claim_info[str(i)] = claiming_match.group(i)

        return claim_info

    def get_simple_race_restrictions(self):
        race_restrictions = re.search(r'(NOT|NEVER) WON ([A-Z0-9$,]+) ?(ONCE|TWICE|THREE TIMES|FOUR TIMES)? ?'
                                      r'(RACES?)? ?(OTHER THAN ([A-Z ,]+))? ?((SINCE|IN) (([A-Z ]+)?[0-9 ,\-]+))?',
                                      self.current_slug_text)
        # Make a dict with the match object and its groups, which is returned by this function call
        restriction_info = {
            'match': race_restrictions,
        }

        for i in range(len(race_restrictions.regs)):
            restriction_info[str(i)] = race_restrictions.group(i)

        if race_restrictions.group(7) is None:
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
        if re.search(r'HAVE STARTED FOR A CLAIMING PRICE', self.current_slug_text):
            # Set dict entries with claiming-start info
            claim_info = self.get_claiming_restriction()
            for key in claim_info.keys():
                print(f'claim_info[{key}]: {claim_info[key]}')
            slug_restrictions_dict['claim_start_req_price'] = int(claim_info['2'])
            slug_restrictions_dict['claim_start_req_time_limit'] = claim_info['6']
            # Delete the claiming-start info off the current slug.
            self.restrictions_string = self.restrictions_string[:claim_info['match'].span(0)[0] + self.current_slug_span_start] + \
                                self.restrictions_string[claim_info['match'].span(0)[1] + self.current_slug_span_start:]
            # Print post-deletion slug
            print(f'restrictions string after deleting claiming info:\n\t{self.restrictions_string}')
        else:
            print('No claiming-start requirement found')

        if re.search(r'(NOT|NEVER) WON', self.current_slug_text):
            restriction_info = self.get_simple_race_restrictions()
            self.restriction_info = restriction_info
            for key in restriction_info.keys():
                print(f'restriction_info[{key}]: {restriction_info[key]}')
            slug_restrictions_dict['number_limit'] = self.text_to_num_mappings.get(restriction_info['3'] if restriction_info['3'] else restriction_info['2'], 'ERROR!')
            slug_restrictions_dict['money_limit'] = int(re.sub('\$', '', restriction_info['2'])) if '$' in restriction_info['2'] else 0
            slug_restrictions_dict['time_limit'] = restriction_info['9']
            slug_restrictions_dict['excluded_races'] = re.sub(r' ?OR ?$', '', restriction_info['6']) if restriction_info['6'] else 0
            # Delete the restriction_info match off of current_slug
            self.restrictions_string = self.restrictions_string[:restriction_info['match'].span(0)[0] + self.current_slug_span_start] + \
                                self.restrictions_string[restriction_info['match'].span(0)[1] + self.current_slug_span_start:]
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

        # Parse the first restriction slug, delete it from restriction_string, and look for more restriction_strings;
        # parse them if found
        for i in range(3):
            if self.current_slug:
                for j in range(len(self.current_slug.regs)):
                    print(f'Current slug match {j}: {self.current_slug.group(j)}')
                print(f'{i}: Processing slug: {self.current_slug.group(0)}')

                self.current_slug_text = self.current_slug.group(0)
                self.current_slug_span_start = self.current_slug.span(0)[0]
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

    def columnize_excluded_race_types(self):
        hot_one_dict = {}
        for num in self.exceptions_list:
            unrecognized_race_types = list(self.processed_restrictions_dict[num + 'excluded_races'])
            hot_one_dict[num + 'original_string'] = self.processed_restrictions_dict[num + 'excluded_races']
            hot_one_dict[num + 'unrecognized_races'] = unrecognized_race_types

            # Make a binary 1/0 column for each excluded race type
            for race_type in self.excluded_race_types:
                excluded_in_race = [0 for _ in range(len(unrecognized_race_types))]
                for i in range(len(excluded_in_race)):
                    if race_type in str(unrecognized_race_types[i]):
                        excluded_in_race[i] = 1
                        # Delete the race type from excluded races so we can see what race types aren't being captured
                        # This also prevents over counting of things like "Restricted allowance" and "Restricted"
                        unrecognized_race_types[i] = re.sub(r'{}'.format(race_type), '', unrecognized_race_types[i])
                hot_one_dict[num + race_type] = excluded_in_race

        for key, value in hot_one_dict.items():
            self.processed_restrictions_dict[key] = value

        return hot_one_dict

    def process_date_info(self):

        self.date_info = {}
        date_info_template = {
                'time_limit': [],
                'date_1': [],
                'date_2': [],
                'timedelta_months': [],
                'timedelta_days': [],
                'time_limit_months': [],
            }
        date_list = self.date_list

        def get_date_from_string(date_string, date_2):
            if re.search(r'[A-Z]+ \d{1,2} \d{4}', start_date[i]):
                matched_string = re.search(r'[A-Z]+ \d{1,2} \d{4}', start_date[i]).group(0)
                return datetime.strptime(matched_string, '%B %d %Y')
            elif re.search(r'(\d{4}) ?- ?\d{2,4}', start_date[i]):
                first_year = re.search(r'(\d{4}) ?- ?\d{2,4}', start_date[i]).group(1)
                return datetime.strptime(first_year, '%Y')
            elif re.search(r'^\d{4}', start_date[i]):
                return datetime.strptime(start_date[i], '%Y')
            elif re.search(r'^[A-Z]+ \d{1,2}$', start_date[i]):
                start_date[i] = start_date[i] + ' ' + str(date_2.year)
                return_date = datetime.strptime(start_date[i], '%B %d %Y')
                if return_date.date() == date_2 or return_date.date() > date_2:
                    return_date = return_date - relativedelta.relativedelta(years=1)
                return return_date
            else:
                return 'ERROR!'

        def get_time_limit_months(timedelta):
            if timedelta.days < 0:
                return 'ERROR!--NEGATIVE NUM'
            elif timedelta.days < 11:
                return timedelta.months + (12 * timedelta.years)
            elif timedelta.days < 21:
                return timedelta.months + 0.5 + (12 * timedelta.years)
            elif timedelta.days > 20:
                return timedelta.months + 1 + (12 * timedelta.years)

        for exception_item in self.exceptions_list:

            date_info= date_info_template.copy()

            start_date = self.processed_restrictions_dict[exception_item + 'time_limit']
            start_date = [str(item).strip() for item in start_date]

            for i in range(len(date_list)):
                date_2 = date_list[i]
                date_1 = get_date_from_string(start_date[i], date_2)

                print(f'i: {exception_item} - {i}. Date_1: {type(date_1)} - {date_1}')
                print(f'i: {i}. Date_2: {type(date_2)} - {date_2}')

                timedelta = relativedelta.relativedelta(date_2, date_1.date()) if date_1 != 'ERROR!' else None

                if timedelta:
                    time_limit_months = get_time_limit_months(timedelta)


                date_info['time_limit'].append(start_date[i])
                date_info['date_1'].append(date_1)
                date_info['date_2'].append(date_2)
                date_info['timedelta_months'].append(timedelta.months if timedelta else None)
                date_info['timedelta_days'].append(timedelta.days if timedelta else None)
                date_info['time_limit_months'].append(time_limit_months if timedelta else 0)

                for key in date_info.keys():
                    self.date_info[exception_item + key] = date_info[key]

        return self.date_info
