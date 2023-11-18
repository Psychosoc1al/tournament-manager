from enum import Enum

from Match import Match
from Participant import Participant


class BracketType(Enum):
    SINGLE = 0
    UPPER = 1
    LOWER = 2


class Bracket:
    def __init__(self, bracket_type: BracketType) -> None:
        self.type = bracket_type
        self.matches = []

    @property
    def type(self) -> BracketType:
        return self._type

    @type.setter
    def type(self, value: BracketType) -> None:
        self._type = value

    @property
    def matches(self) -> list[Match]:
        print(self._matches)
        return self._matches

    @matches.setter
    def matches(self, value: list[Match]) -> None:
        self._matches = value

    def add_match(self, match: Match) -> None:
        self.matches.append(match)

    def generate_bracket(self, participants: list[Participant]) -> None:
        start_size = len(participants)
        k = 2
        while k < start_size:
            k *= 2
        size = k
        self.matches.append([])
        for i in range(start_size - size // 2):
            self.matches[0].append(Match(0, i, participants[2 * i], participants[2 * i + 1]))
        for i in range((start_size - size // 2) * 2, start_size):
            self.matches[0].append(Match(0, i, participants[i], Participant(None)))
        size //= 2
        while size > 1:
            self.matches.append([])
            for i in range(size // 2):
                self.matches[-1].append(Match(len(self.matches) - 1, i, Participant(None), Participant(None)))
                if self.matches[-2][2 * i].participant2.name is None and \
                        self.matches[-2][2 * i].participant1.name is not None:
                    self.matches[-1][-1].participant1 = self.matches[-2][2 * i].participant1
                if self.matches[-2][2 * i + 1].participant2.name is None and \
                        self.matches[-2][2 * i + 1].participant1.name is not None:
                    self.matches[-1][-1].participant2 = self.matches[-2][2 * i + 1].participant1
            size //= 2
        size = 2
        while size < start_size:
            size *= 2
        if self.type == BracketType.UPPER or self.type == BracketType.SINGLE:
            self.matches.append([])
            for i in range(start_size - size // 2):
                self.matches[0].append(Match(0, i, participants[2 * i], participants[2 * i + 1]))
            for i in range((start_size - size // 2) * 2, start_size):
                self.matches[0].append(Match(0, i - (start_size - size // 2), participants[i], Participant("???")))
            size //= 2
            while size > 1:
                self.matches.append([])
                for i in range(size // 2):
                    self.matches[-1].append(Match(len(self.matches) - 1, i, Participant("???"), Participant("???")))
                    if self.matches[-2][2 * i].participant2.name == "???" and \
                            self.matches[-2][2 * i].participant1.name != "???":
                        self.matches[-1][-1].participant1 = self.matches[-2][2 * i].participant1
                    if self.matches[-2][2 * i + 1].participant2.name == "???" and \
                            self.matches[-2][2 * i + 1].participant1.name != "???":
                        self.matches[-1][-1].participant2 = self.matches[-2][2 * i + 1].participant1
                size //= 2
            for match in self.matches[0]:
                if match.participant2.name == "???":
                    self.update_result(match.stage, match.match_number_stage, (0, -1))
        elif self.type == BracketType.LOWER:
            size //= 4
            while size >= 1:
                for _ in range(2):
                    self.matches.append([])
                    for i in range(size):
                        self.matches[-1].append(
                            Match(len(self.matches) - 1, i, Participant("???"), Participant("???")))
                size //= 2
        else:
            raise ValueError

    def update_result(self, stage: int, match_number_stage: int, result: (int, int)) -> None:
        self.matches[stage][match_number_stage].score_participant1 = result[0]
        self.matches[stage][match_number_stage].score_participant2 = result[1]
        if result[0] > result[1]:
            winner = self.matches[stage][match_number_stage].participant1
        else:
            winner = self.matches[stage][match_number_stage].participant2
        if stage < len(self.matches) - 1:
            if self.type == BracketType.UPPER or self.type == BracketType.SINGLE:
                if match_number_stage % 2 == 0:
                    self.matches[stage + 1][match_number_stage // 2].participant1 = winner
                else:
                    self.matches[stage + 1][match_number_stage // 2].participant2 = winner
            elif self.type == BracketType.LOWER:
                if stage % 2 != 0:
                    if match_number_stage % 2 == 0:
                        self.matches[stage + 1][match_number_stage // 2].participant1 = winner
                    else:
                        self.matches[stage + 1][match_number_stage // 2].participant2 = winner
                else:
                    self.matches[stage + 1][match_number_stage].participant2 = winner

    def take_losers(self, match: Match):
        if self.type == BracketType.LOWER:
            stage = match.stage
            match_number_stage = match.match_number_stage
            result = (match.score_participant1, match.score_participant2)
            if result[0] > result[1]:
                loser = match.participant2
            else:
                loser = match.participant1
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
        else:
            raise ValueError
