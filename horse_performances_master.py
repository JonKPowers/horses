import horse_performances_refactor as hp

# Generate the data handler for the consolidated races aggregated db
consolidated_races_db_handler= hp.AdderDBHandler('horses_consolidated_races',
                                                 'horses_consolidated_races',
                                                 include_horse=False)
consolidated_races_db_handler.build_dataframe()
consolidated_races_db_handler.add_race_ids()

# Generate the data handler for the consolidated performances aggregated db
# NOTE: Will have to add one for aggregated races (a different table in horses_consolidated_races) at some point.
consolidated_performances_db_handler = hp.AdderDBHandler('horses_consolidated_races',
                                                         'horses_consolidated_performances',
                                                         include_horse=True)
consolidated_performances_db_handler.build_dataframe()
consolidated_performances_db_handler.add_race_ids()

# Build up data handlers for the race results and PP data sources
past_performances_db_handler = hp.AdderDBHandler('horses_data', 'horse_pps', include_horse=True)
race_results_db_handler = hp.AdderDBHandler('horses_data', 'race_horse_info', include_horse=True)


# Spin up the aggregators for the race results and PP data sources
past_performances_adder = hp.RaceProcessor(past_performances_db_handler,
                                           consolidated_performances_db_handler,
                                           consolidated_races_db_handler,
                                           include_horse=True)

race_results_adder = hp.RaceProcessor(race_results_db_handler,
                                      consolidated_performances_db_handler,
                                      consolidated_races_db_handler,
                                      include_horse=True)


past_performances_adder.add_to_consolidated_data()

