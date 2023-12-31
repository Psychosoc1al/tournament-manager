from enum import Enum

from model.match import Match
from model.participant import Participant


class BracketType(Enum):
    SINGLE = 0
    UPPER = 1
    LOWER = 2


class Bracket:
    def __init__(self, bracket_type: BracketType) -> None:
        self.bracket_type = bracket_type
        self.matches = []

    @property
    def bracket_type(self) -> BracketType:
        return self._type

    @bracket_type.setter
    def bracket_type(self, value: BracketType) -> None:
        self._type = value

    @property
    def matches(self) -> list[list[Match]]:
        return self._matches

    @matches.setter
    def matches(self, value: list[list[Match]]) -> None:
        self._matches = value

    def __fill_void_up(self, size: int) -> None:
        while size > 1:
            self.matches.append([])
            for i in range(size // 2):
                self.matches[-1].append(
                    Match(len(self.matches) - 1, i, Participant(), Participant())
                )
                if (
                    self.matches[-2][2 * i].participant2.name == "???"
                    and self.matches[-2][2 * i].participant1.name != "???"
                ):
                    self.matches[-1][-1].participant1 = self.matches[-2][
                        2 * i
                    ].participant1
                if (
                    self.matches[-2][2 * i + 1].participant2.name == "???"
                    and self.matches[-2][2 * i + 1].participant1.name != "???"
                ):
                    self.matches[-1][-1].participant2 = self.matches[-2][
                        2 * i + 1
                    ].participant1
            size //= 2

    def __fill_void_down(self, size: int) -> None:
        while size >= 1:
            for _ in range(2):
                self.matches.append([])
                for i in range(size):
                    self.matches[-1].append(
                        Match(len(self.matches) - 1, i, Participant(), Participant())
                    )
            size //= 2

    def generate_bracket(self, participants: list[Participant]) -> None:
        start_size = len(participants)
        size = 2
        while size < start_size:
            size *= 2
        if (
            self.bracket_type == BracketType.UPPER
            or self.bracket_type == BracketType.SINGLE
        ):
            self.matches.append([])
            for i in range(start_size - size // 2):
                self.matches[0].append(
                    Match(0, i, participants[2 * i], participants[2 * i + 1])
                )
            for i in range((start_size - size // 2) * 2, start_size):
                self.matches[0].append(
                    Match(
                        0, i - (start_size - size // 2), participants[i], Participant()
                    )
                )
            size //= 2
            self.__fill_void_up(size)
            for match in self.matches[0]:
                if match.participant2.name == "???":
                    self.update_result(match.stage, match.match_number_stage, (0, -1))
        elif self.bracket_type == BracketType.LOWER:
            size //= 4
            self.__fill_void_down(size)
            self.matches.append(
                [Match(len(self.matches) - 1, 0, Participant(), Participant())]
            )
        else:
            raise ValueError

    def __move_winner(
        self, stage: int, match_number_stage: int, winner: Participant
    ) -> None:
        if match_number_stage % 2 == 0:
            self.matches[stage + 1][match_number_stage // 2].participant1 = winner
        else:
            self.matches[stage + 1][match_number_stage // 2].participant2 = winner

    def update_result(
        self, stage: int, match_number_stage: int, result: tuple[int, int]
    ) -> None:
        self.matches[stage][match_number_stage].score_participant1 = result[0]
        self.matches[stage][match_number_stage].score_participant2 = result[1]
        if result[0] > result[1]:
            winner = self.matches[stage][match_number_stage].participant1
        else:
            winner = self.matches[stage][match_number_stage].participant2
        if stage < len(self.matches) - 1:
            if (
                self.bracket_type == BracketType.UPPER
                or self.bracket_type == BracketType.SINGLE
            ):
                self.__move_winner(stage, match_number_stage, winner)
            elif self.bracket_type == BracketType.LOWER:
                if stage % 2 != 0:
                    self.__move_winner(stage, match_number_stage, winner)
                else:
                    self.matches[stage + 1][match_number_stage].participant2 = winner

    def __move_loser(
        self, stage: int, match_number_stage: int, loser: Participant
    ) -> None:
        if stage == 0:
            if match_number_stage % 2 == 0:
                self.matches[0][match_number_stage // 2].participant1 = loser
            else:
                self.matches[0][match_number_stage // 2].participant2 = loser
        else:
            if stage % 2 != 0:
                number = len(self.matches[stage * 2 - 1]) - 1 - match_number_stage
            else:
                number = match_number_stage
            self.matches[stage * 2 - 1][number].participant1 = loser

    def take_loser(self, match: Match):
        if self.bracket_type == BracketType.LOWER:
            stage = match.stage
            match_number_stage = match.match_number_stage
            result = (match.score_participant1, match.score_participant2)
            if result[0] > result[1]:
                loser = match.participant2
            else:
                loser = match.participant1
            self.__move_loser(stage, match_number_stage, loser)
        else:
            raise ValueError

    def take_winner(self) -> Participant:
        if (
            self.matches[-1][0].score_participant1
            > self.matches[-1][0].score_participant2
        ):
            return self.matches[-1][0].participant1
        elif (
            self.matches[-1][0].score_participant1
            < self.matches[-1][0].score_participant2
        ):
            return self.matches[-1][0].participant2
        else:
            return Participant()

    def create_final(self, participant: Participant):
        if self.bracket_type == BracketType.LOWER:
            self.matches[-1][0].participant2 = participant
        else:
            raise ValueError
