import horse_performances_refactor as hp

# Import configuration constants and encapsulate them into a data pack
from aggregation_datapack import DataPack
from horse_performances_consolidated_table_structure import CONSOLIDATED_TABLE_STRUCTURE
from horse_performances_additional_fields import ADDITIONAL_FIELDS
from horse_performances_table_to_index_mappings import TABLE_TO_INDEX_MAPPINGS
from horse_performances_distances_to_process import DISTANCES_TO_PROCESS
from horse_performances_position_distance_mappings import POSITION_DISTANCE_MAPPINGS
from horses_performances_lead_or_beaten_distance_mappings import LEAD_OR_BEATEN_DISTANCE_MAPPINGS
from constant_aggregated_performances_unique import UNIQUE

data_pack = DataPack(CONSOLIDATED_TABLE_STRUCTURE = CONSOLIDATED_TABLE_STRUCTURE,
                     ADDITIONAL_FIELDS = ADDITIONAL_FIELDS,
                     TABLE_TO_INDEX_MAPPINGS = TABLE_TO_INDEX_MAPPINGS,
                     DISTANCES_TO_PROCESS = DISTANCES_TO_PROCESS,
                     POSITION_DISTANCE_MAPPINGS = POSITION_DISTANCE_MAPPINGS,
                     LEAD_OR_BEATEN_DISTANCE_MAPPINGS = LEAD_OR_BEATEN_DISTANCE_MAPPINGS,
                     UNIQUE=UNIQUE)


# Generate the data handler for the consolidated races aggregated db
consolidated_races_db_handler= hp.AdderDataHandler('horses_consolidated_races', 'horses_consolidated_races',
                                                   data_pack, include_horse=False, initialize_db=True)
consolidated_races_db_handler.build_dataframe()
consolidated_races_db_handler.add_race_ids()

# Generate the data handler for the consolidated performances aggregated db
# NOTE: Will have to add one for aggregated races (a different table in horses_consolidated_races) at some point.
consolidated_performances_db_handler = hp.AdderDataHandler('horses_consolidated_races', 'horses_consolidated_performances',
                                                           data_pack, include_horse=True)
consolidated_performances_db_handler.build_dataframe()
consolidated_performances_db_handler.add_race_ids()

# Build up data handlers for the race results and PP data sources
past_performances_db_handler = hp.AdderDataHandler('horses_data', 'horse_pps', data_pack,
                                                   include_horse=True, other='LIMIT 10000 OFFSET 90000')
race_results_db_handler = hp.AdderDataHandler('horses_data', 'race_horse_info', data_pack,
                                              include_horse=True, other='LIMIT 10000 OFFSET 90000')


# Spin up the aggregators for the race results and PP data sources
past_performances_adder = hp.RaceProcessor(past_performances_db_handler, consolidated_performances_db_handler,
                                           consolidated_races_db_handler, include_horse=True)

race_results_adder = hp.RaceProcessor(race_results_db_handler, consolidated_performances_db_handler,
                                      consolidated_races_db_handler, include_horse=True)

race_results_adder.add_to_consolidated_data()
past_performances_adder.add_to_consolidated_data()

