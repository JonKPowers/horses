from BaseObjects import HorseID


class HorseID:

    def __init__(self, name: str, id: int = None):
        self._name = name
        try:
            self._id = int(id)
        except (ValueError, TypeError) as e:
            self._id = None
            # print(e, f'({name})')

    @classmethod
    def unknown_horse(cls):
        return cls('Unknown Horse', 0)

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id

    def __str__(self):
        return f'{self._name} ({self._id})'

    def __hash__(self):
        return hash((self._name, self._id))

    def __eq__(self, other: HorseID):
        if self._id is not None and other._id is not None:
            return (self._name == other._name) and (self._id == other._id)

        return self._name == other._name
