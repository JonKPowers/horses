class JockeyID:

    def __init__(self, name: str, _id: int):
        self.name: str = name
        self.id: int = _id

class TrainerID:

    def __init__(self, name: str, _id: int):
        self.name: str = name
        self.id: int = _id

class OwnerID:

    def __init__(self, name: str, _id: int = None):
        self.name: str = name
        self.id: int = _id
