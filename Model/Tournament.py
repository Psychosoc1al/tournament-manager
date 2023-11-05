from datetime import date

from Model.Bracket import Bracket
from Model.Participant import Participant


class Tournament:
    def __init__(self,
                 name: str,
                 sport: str,
                 tour_date: date,
                 participants: list[Participant],
                 brackets: list[Bracket]):
        self._name = name
        self._sport = sport
        self._date = tour_date
        self._winner = None
        self._participants = participants
        self._brackets = brackets

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
    def date(self, value: date):
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
