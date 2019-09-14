from BaseObjects.RaceID import RaceID

class HorsePerformance:
    def __init__(self, race_id: RaceID):
        self.race_id: RaceID = race_id

        self.position: dict = dict()
        self.lead_beaten: dict = dict()

        self.position[0]: int = None
        self.position[330]: int = None
        self.position[440]: int = None
        self.position[660]: int = None
        self.position[880]: int = None
        self.position[990]: int = None
        self.position[1100]: int = None
        self.position[1210]: int = None
        self.position[1320]: int = None
        self.position[1430]: int = None
        self.position[1540]: int = None
        self.position[1610]: int = None
        self.position[1650]: int = None
        self.position[1760]: int = None
        self.position[1830]: int = None
        self.position[1870]: int = None
        self.position[1980]: int = None

        self.lead_beaten[0]: int = None
        self.lead_beaten[330]: int = None
        self.lead_beaten[440]: int = None
        self.lead_beaten[660]: int = None
        self.lead_beaten[880]: int = None
        self.lead_beaten[990]: int = None
        self.lead_beaten[1100]: int = None
        self.lead_beaten[1210]: int = None
        self.lead_beaten[1320]: int = None
        self.lead_beaten[1430]: int = None
        self.lead_beaten[1540]: int = None
        self.lead_beaten[1610]: int = None
        self.lead_beaten[1650]: int = None
        self.lead_beaten[1760]: int = None
        self.lead_beaten[1830]: int = None
        self.lead_beaten[1870]: int = None
        self.lead_beaten[1980]: int = None
