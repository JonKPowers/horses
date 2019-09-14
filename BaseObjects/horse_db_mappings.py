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
