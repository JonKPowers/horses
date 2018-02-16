horses_table = {
    'table_name': 'horses_info',
    'sql_cols': {
        'simple_entry': 'INT',
        'horse_name': 'VARCHAR(255)',
        'horse_id': 'INT',

        'sex': 'VARCHAR(255)',

        'foal_date': 'DATE',
        'where_bred': 'VARCHAR(255)',
        'breeder': 'VARCHAR(255)',

        'sire': 'VARCHAR(255)',
        'dam': 'VARCHAR(255)',
        'sires_sire': 'VARCHAR(255)',
        'dam_sire': 'VARCHAR(255)',

        'color': 'VARCHAR(255)',

    },

    'unique_keys': [
        'horse_id',
    ],

    'foreign_keys': [    # a list of tuples (local_col, foreign_table(foreign_col))

    ],

    'not_null': ['horse_name'],

    'files_to_process': ['5', '2', 'DRF'],

    '5': {
        'field_mappings': {
            # SQL_col: 5_file_col
            'horse_name': 'horse_name',
            'sex': 'sex',
            'foal_date': 'foal_date',
            'where_bred': ['foreign_bred_code', 'state_bred_code'],
            'breeder': 'breeder',
            'sire': 'sire',
            'dam': 'dam',
            'dam_sire': 'broodmare_sire',
            'color': 'color',
        },

        'duplicate_query_field': 'horse_name',

        'duplicate_confirm_field': 'foal_date',
    },

    '2': {
        'field_mappings': {
            # SQL_col: 2_file_col
            'horse_name': 'horse_name',
            'horse_id': 'horse_reg_id',
            'foal_date': '',
            # only have 'birth_year'
            'where_bred': '',
            # need to sort between 'foreign_bred_code' and 'state_bred_code'
        },
    },

    'DRF': {
        # SQL_col: DRF_file_col
        'horse_name': 'horse_name',
        'sex': 'sex',
        'foal_date': '',
            # Need to get through 'birth_year' and 'foaling_month'
        'where_bred': 'where_bred',
        'breeder': '',
        'sire': 'sire',
        'dam': 'dam',
        'sires_sire': 'sires_sire',
        'dam_sire': 'dams_sire',
        'color': 'color',

        # Maybe add these horses that are also mentioned.
        #
        # 'win_horse': 'past_win_{}',
        # 'place_horse': 'past_place_{}',
        # 'show_horse': 'past_show_{}',
    },
}

jockey_table = {
    '2': {
        'jockey_id': 'jockey_id',
        'jockey': 'jockey_name',
        'jockey_first': 'jockey_first_name',
        'jockey_middle': 'jockey_middle_name',
        'jockey_last': 'jockey_last_name',
    },

    'DRF': {
        'jockey_name': 'jockey',
        'jockey': 'past_jockey_{}'
    },
}

trainer_table = {
    '2': {
        'trainer_id': 'trainer_id',
        'trainer_name': 'trainer_name',
        'trainer_first': 'trainer_first_name',
        'trainer_middle': 'trainer_middle_name',
        'trainer_last': 'trainer_last_name',

        'claimed_trainer': 'claimed_trainer',
        'claimed_trainer_id': 'claimed_trainer_id',
        'claimed_trainer_first': 'claimed_trainer_first',
        'claimed_trainer_middle': 'claimed_trainer_middle',
        'claimed_trainer_last': 'claimed_trainer_last',

    },

    'DRF': {
        'trainer_name': 'trainer',
        'trainer': 'past_trainer_{}'
    },
}

owner_table = {

    '2': {
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'owner_first': 'owner_first_name',
        'owner_middle': 'owner_middle_name',

        'claimed_owner': 'claimed_owner',
        'claimed_owner_id': 'claimed_owner_id',
        'claimed_owner_first': 'claimed_owner_first',
        'claimed_owner_middle': 'claimed_owner_middle',
        'claimed_owner_last': 'claimed_owner_last',
    },

    'DRF': {
        'owner_name': 'todays_owner',
        'date': 'date',
        'silks': 'owners_silks',
    }
}