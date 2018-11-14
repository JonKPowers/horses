import logging
import db_handler_persistent as dbh
from aggregation_RaceProcessor import RaceProcessor
from aggregation_AdderDataHandler import AdderDataHandler

import numpy as np
import pandas as pd
import datetime



class PPAdderDataHandler(AdderDataHandler):
    def dummy(self):
        pass

class PPRaceProcessor(RaceProcessor):
    def reconcile_discrepancy(self, new_data, existing_data, column):
        pass
