from BaseObjects import HorseID


class HorseID:

    def __init__(self, name: str, id: int = None):
        self._name = name
        if id is not None:
            self._id = int(id)

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id

    def __str__(self):
        return f'{self._name} ({self._id})'

    def __hash__(self):
        return hash((self._name, self._id))

    def __eq__(self, other: HorseID):
        return (self._name == other._name) and (self._id == other._id)
