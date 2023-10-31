from enum import Enum

from Match import Match
from Participant import Participant


class BracketType(Enum):
    UPPER = 1
    LOWER = 2


class Bracket:

    def __init__(self, type: BracketType):
        self._type = type
        self._matches = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: BracketType):
        self._type = value

    @property
    def matches(self):
        return self._matches

    @matches.setter
    def matches(self, value: list):
        self._matches = value

    def add_match(self, match: Match):
        self._matches.append(match)

    def generate_bracket(self, participants: list[Participant]):
        pass  # TODO

    def update_result(self, match: Match, result: (int, int)):
        pass  # TODO
