from datetime import date
from enum import Enum

from bracket import Bracket, BracketType
from participant import Participant


class TournamentType(Enum):
    SINGLE_ELIMINATION = 0
    DOUBLE_ELIMINATION = 1


class Tournament:
    def __init__(self,
                 name: str,
                 sport: str,
                 bracket_type: str,
                 tour_date: date,
                 participants: list[Participant],
                 ) -> None:
        self.name = name
        self.sport = sport
        self.bracket_type = bracket_type
        self.tour_date = tour_date
        self.participants = participants

        self.winner = None
        self.brackets = []

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
    def tour_date(self) -> date:
        return self._tour_date

    @tour_date.setter
    def tour_date(self, value: date) -> None:
        self._tour_date = value

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

    @brackets.setter
    def brackets(self, value) -> None:
        self._brackets = value

    @property
    def bracket_type(self) -> str:
        return self._bracket_type

    @bracket_type.setter
    def bracket_type(self, value) -> None:
        self._bracket_type = value

    def add_participant(self, participant: Participant) -> None:
        self._participants.append(participant)

    def create_brackets(self) -> None:
        if self._bracket_type == TournamentType.SINGLE_ELIMINATION:
            self._brackets.append(Bracket(BracketType.SINGLE))

        elif self._bracket_type == TournamentType.DOUBLE_ELIMINATION:
            self._brackets.append(Bracket(BracketType.UPPER))
            self._brackets.append(Bracket(BracketType.LOWER))

        for bracket in self._brackets:
            bracket.generate_bracket(self.participants)

    def update_result(self,
                      stage: int,
                      match_number_stage: int,
                      result: (int, int),
                      bracket_type=BracketType.SINGLE
                      ) -> None:

        if bracket_type == BracketType.LOWER:
            self._brackets[1].update_result(stage, match_number_stage, result)
        else:
            self._brackets[0].update_result(stage, match_number_stage, result)
            if self._bracket_type == TournamentType.DOUBLE_ELIMINATION:
                self._brackets[1].take_losers(self._brackets[0].matches[stage][match_number_stage])

        match = self._brackets[0].matches[-1][0]
        if match.score_participant1 > match.score_participant2:
            self.winner = match.participant1
        elif match.score_participant1 < match.score_participant2:
            self.winner = match.participant2
