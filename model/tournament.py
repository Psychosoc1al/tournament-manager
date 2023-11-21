from datetime import date
from enum import Enum

from model.bracket import Bracket, BracketType
from model.participant import Participant


class TournamentType(str, Enum):
    SINGLE = 'Single elimination'
    DOUBLE = 'Double elimination'


class Tournament:
    def __init__(self,
                 name: str,
                 sport: str,
                 tournament_type: str,
                 tour_date: date,
                 participants: list[Participant],
                 results: list[list[tuple[int, int, int, int]]] = None,
                 ) -> None:
        self.name = name
        self.sport = sport
        self.tournament_type = tournament_type
        self.tour_date = tour_date
        self.participants = participants
        self.brackets = []

        self.winner = None
        self.results = results

        self.create_brackets()
        if results:
            self._restore_results()

    def save_results(self) -> None:
        self.results = []
        for bracket in self.brackets:
            self.results.append([])
            for stage in bracket.matches:
                self.results[-1].append([])
                for match in stage:
                    self.results[-1][-1].append(
                        (match.stage, match.match_number_stage, match.score_participant1, match.score_participant2)
                    )

    def _restore_results(self) -> None:
        for bracket, result in zip(self.brackets, self.results):
            for stage, stage_result in zip(bracket.matches, result):
                for match, match_result in zip(stage, stage_result):
                    if match_result[2] > 0 or match_result[3] > 0:
                        bracket.update_result(
                            match.stage,
                            match.match_number_stage,
                            (match_result[2], match_result[3])
                        )

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
    def brackets(self, value: list[Bracket]) -> None:
        self._brackets = value

    @property
    def tournament_type(self) -> str:
        return self._tournament_type

    @tournament_type.setter
    def tournament_type(self, value: str) -> None:
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
                self.brackets[1].create_final(self.brackets[0].take_winner())

        if self.tournament_type == TournamentType.DOUBLE:
            match = self.brackets[1].matches[-1][0]
        else:
            match = self.brackets[0].matches[-1][0]

        if match.score_participant1 > match.score_participant2:
            self.winner = match.participant1
        elif match.score_participant1 < match.score_participant2:
            self.winner = match.participant2


if __name__ == '__main__':
    tournament = Tournament(
        name='Test',
        sport='Test',
        tournament_type=TournamentType.DOUBLE,
        tour_date=date.today(),
        participants=[Participant(f'Test{i}') for i in range(1, 9)],
    )
    bracket0 = tournament.brackets[0]
    bracket1 = tournament.brackets[1]

    tournament.update_result(0, 0, (1, 0), BracketType.UPPER)
    tournament.update_result(0, 1, (1, 0), BracketType.UPPER)
    tournament.update_result(0, 2, (1, 0), BracketType.UPPER)
    tournament.update_result(0, 3, (1, 0), BracketType.UPPER)
    tournament.update_result(1, 0, (1, 0), BracketType.UPPER)
    tournament.update_result(1, 1, (1, 0), BracketType.UPPER)
    tournament.update_result(2, 0, (1, 0), BracketType.UPPER)

    tournament.update_result(0, 0, (1, 0), BracketType.LOWER)
    tournament.update_result(0, 1, (1, 0), BracketType.LOWER)
    tournament.update_result(1, 0, (1, 0), BracketType.LOWER)
    tournament.update_result(1, 1, (1, 0), BracketType.LOWER)
    tournament.update_result(2, 0, (1, 0), BracketType.LOWER)
    tournament.update_result(3, 0, (1, 0), BracketType.LOWER)
    tournament.update_result(4, 0, (1, 0), BracketType.LOWER)

    print(*[[(bracket0.matches[i][j].participant1.name, bracket0.matches[i][j].participant2.name) for j in
             range(len(bracket0.matches[i]))] for i in range(len(bracket0.matches))], sep='\n')
    print()
    print(*[[(bracket1.matches[i][j].participant1.name, bracket1.matches[i][j].participant2.name) for j in
             range(len(bracket1.matches[i]))] for i in range(len(bracket1.matches))], sep='\n')
    print()
    print(tournament.winner)
