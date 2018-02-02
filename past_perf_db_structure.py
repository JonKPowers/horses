table_list = {
    'horses': 'horses',
    'workouts': 'workouts',
}

horse_table_structure = {
    'db_fields' : {
        'horse_name': 'horse_name',
        'birth_year': 'birth_year',
        'foaling_month': 'foaling_month',
        'sex': 'sex',
        'color': 'color',
        'sire': 'sire',
        'sires_sire': 'sires_sire',
        'dam': 'dam',
        'dams_sire': 'dams_sire',
        'breeder': 'breeder',
        'where_bred': 'where_bred',
    },

    'primary_key': [
        'ID',
    ],

    'unique_key': [
        'horse_name',
        'birth_year',
        'foaling_month',
    ],

    'foreign_keys': [

    ],
}

workout_table_structure = {
    'db_fields': {
        'horse_name': 'horse_name',
        'birth_year': 'birth_year',
        'foaling_month': 'foaling_month',
        'date': 'workout_date_{}',
        'track': 'workout_track_{}',
        'distance': 'workout_distance_{}',
        'time': 'workout_time_{}',
        'run_description': 'workout_description_{}',
        'track_type': 'workout_track_type_{}',
        'track_condition': 'workout_condition_{}',
        'rank_of_same_works': 'rank_same_workout_{}',
        'number_of_same_works': 'same_workouts_all_day_{}',
    },

    'primary_key': [
        'ID',
    ],

    'unique_key': [
        'horse_name',
        'birth_year',
        'foaling_month',
        'date',
    ],

    'foreign_keys': {
        'horse_name': table_list['horses'] + '(horse_name)',
    }
}
