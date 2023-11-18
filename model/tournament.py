from datetime import date
from enum import StrEnum

from bracket import Bracket, BracketType
from participant import Participant


class TournamentType(StrEnum):
    SINGLE = "Single elimination"
    DOUBLE = "Double elimination"


class Tournament:
    def __init__(self,
                 name: str,
                 sport: str,
                 tournament_type: str,
                 tour_date: date,
                 participants: list[Participant],
                 brackets: list[Bracket] = None,
                 ) -> None:
        self.name = name
        self.sport = sport
        self.tournament_type = tournament_type
        self.tour_date = tour_date
        self.participants = participants
        self.brackets = brackets if brackets else []

        self.winner = None

        self.create_brackets()

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
    def tournament_type(self) -> str:
        return self._tournament_type

    @tournament_type.setter
    def tournament_type(self, value) -> None:
        self._tournament_type = value

    def add_participant(self, participant: Participant) -> None:
        self._participants.append(participant)

    def create_brackets(self) -> None:
        if self.tournament_type == TournamentType.SINGLE:
            self.brackets.append(Bracket(BracketType.SINGLE))

        elif self.tournament_type == TournamentType.DOUBLE:
            self.brackets.append(Bracket(BracketType.UPPER))
            self.brackets.append(Bracket(BracketType.LOWER))

        for bracket in self.brackets:
            bracket.generate_bracket(self.participants)

    def update_result(self,
                      stage: int,
                      match_number_stage: int,
                      result: (int, int),
                      bracket_type=BracketType.SINGLE
                      ) -> None:

        if bracket_type == BracketType.LOWER:
            self.brackets[1].update_result(stage, match_number_stage, result)
        else:
            self.brackets[0].update_result(stage, match_number_stage, result)
            if self.tournament_type == TournamentType.DOUBLE:
                self.brackets[1].take_losers(self.brackets[0].matches[stage][match_number_stage])

        match = self.brackets[0].matches[-1][0]
        if match.score_participant1 > match.score_participant2:
            self.winner = match.participant1
        elif match.score_participant1 < match.score_participant2:
            self.winner = match.participant2
