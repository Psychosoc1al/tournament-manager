class Participant:
    def __init__(self, name: str = None) -> None:
        self.name = name if name else '???'

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def __str__(self) -> str:
        return self._name
