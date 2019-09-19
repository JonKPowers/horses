bio_fields = {
    # Format for dictionary entry:
    # {name of field in db table: name of attribute in Horse object}
    # e.g., {'where_bred': 'state_bred'}
    #
    # Target table in horse db: horses_info

    'horse_name': 'horse_name',
    # 'horse_id': 'id',
    'birth_year': 'birth_year',
    'foaling_month': 'birth_month',
    'where_bred': 'birth_state',   # todo Change to 'birth_state' in main db
    'sire': 'sire',
    'dam': 'dam',
}

horse_performance_distances = [
    0,
    330,
    440,
    660,
    880,
    990,
    1100,
    1210,
    1320,
    1430,
    1540,
    1610,
    1650,
    1760,
    1830,
    1870,
    1980,
]
# Format:
# {name of db field: distance of item}

horse_performance_fields = {
    'position': {f'position_{distance}': distance for distance in horse_performance_distances},
    'lead_or_beaten': {f'lead_or_beaten_{distance}': distance for distance in horse_performance_distances},
}


