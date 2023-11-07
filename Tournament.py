from datetime import datetime
from enum import Enum

from Bracket import Bracket, BracketType
from Participant import Participant


class TournamentType(Enum):
    SINGLE = 0
    DOUBLE = 1

class Tournament:
    def __init__(self,
                 name: str,
                 date: datetime,
                 participants: list[Participant],
                 type: TournamentType):
        self._name = name
        self._date = date
        self._winner = None
        self._brackets = []
        self._participants = participants
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: datetime):
        self._date = value

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, value: Participant):
        self._winner = value

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value: list[Participant]):
        self._participants = value

    @property
    def brackets(self):
        return self._brackets

    @brackets.setter
    def brackets(self, value: list[Bracket]):
        self._brackets = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: TournamentType):
        self._type = value

    def create_brackets(self):
        if self.type == TournamentType.SINGLE:
            self.brackets.append(Bracket(BracketType.SINGLE))
        elif self.type == TournamentType.DOUBLE:
            self.brackets.append(Bracket(BracketType.UPPER))
            self.brackets.append(Bracket(BracketType.LOWER))
        for bracket in self.brackets:
            bracket.generate_bracket(self.participants)

    def update_result(self, stage: int, match_number_stage: int, result: (int, int), type=BracketType.SINGLE):
        if type == BracketType.LOWER:
            self.brackets[1].update_result(stage, match_number_stage, result)
        else:
            self.brackets[0].update_result(stage, match_number_stage, result)
            if self.type == TournamentType.DOUBLE:
                self.brackets[1].take_losers(self.brackets[0].matches[stage][match_number_stage])
        if self.brackets[0].matches[-1][0].score_participant1 > self.brackets[0].matches[-1][0].score_participant2:
            self.winner = self.brackets[0].matches[-1][0].participant1
        elif self.brackets[0].matches[-1][0].score_participant1 < self.brackets[0].matches[-1][0].score_participant2:
            self.winner = self.brackets[0].matches[-1][0].participant2
