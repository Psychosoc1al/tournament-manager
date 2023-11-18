class Participant:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def __str__(self) -> str:
        return self._name
