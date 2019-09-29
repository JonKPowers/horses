class HorseID:

    def __init__(self, name: str, id: int = None):
        self._name = name
        self._id = int(id)

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        return self._id