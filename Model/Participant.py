class Participant:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def __str__(self):
        return self._name
