from datetime import date

from Model.Bracket import Bracket
from Model.Participant import Participant


class Tournament:
    def __init__(self,
                 name: str,
                 sport: str,
                 bracket_type: int,
                 tour_date: date,
                 participants: list[Participant],
                 ):

        self._name = name
        self._sport = sport
        self._date = tour_date
        self._type = bracket_type
        self._participants = participants

        self._winner = None
        self._brackets = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def sport(self) -> str:
        return self._sport

    @sport.setter
    def sport(self, value: str) -> None:
        self._sport = value

    @property
    def date(self) -> date:
        return self._date

    @date.setter
    def date(self, value: date) -> None:
        self._date = value

    @property
    def winner(self) -> Participant:
        return self._winner

    @winner.setter
    def winner(self, value: Participant) -> None:
        self._winner = value

    @property
    def participants(self) -> list[Participant]:
        return self._participants

    @participants.setter
    def participants(self, value: list[Participant]) -> None:
        self._participants = value

    @property
    def brackets(self) -> list[Bracket]:
        return self._brackets

    def set_brackets(self) -> None:
        pass
        # TODO: generate brackets

    def add_participant(self, participant: Participant) -> None:
        self._participants.append(participant)
