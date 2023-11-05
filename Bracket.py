from enum import Enum

from Match import Match
from Participant import Participant


class BracketType(Enum):
    SINGLE = 0
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
        start_size = len(participants)
        size = 2
        while size < start_size:
            size *= 2
        if self.type == BracketType.UPPER or self.type == BracketType.SINGLE:
            self.matches.append([])
            for i in range(start_size - size//2):
                self.matches[0].append(Match(0, i, participants[2*i], participants[2*i+1]))
            for i in range((start_size - size//2)*2, start_size):
                self.matches[0].append(Match(0, i, participants[i], Participant(None)))
            size //= 2
            while size > 1:
                self.matches.append([])
                for i in range(size//2):
                    self.matches[-1].append(Match(len(self._matches)-1, i, Participant(None), Participant(None)))
                    if self.matches[-2][2*i].participant2.name is None and\
                            self.matches[-2][2*i].participant1.name is not None:
                        self.matches[-1][-1].participant1 = self.matches[-2][2*i].participant1
                    if self.matches[-2][2*i + 1].participant2.name is None and\
                            self.matches[-2][2*i + 1].participant1.name is not None:
                        self.matches[-1][-1].participant2 = self.matches[-2][2*i + 1].participant1
                size //= 2
        elif self.type == BracketType.LOWER:
            size //= 4
            while size >= 1:
                for _ in range(2):
                    self.matches.append([])
                    for i in range(size):
                        self.matches[-1].append(Match(len(self._matches)-1, i, Participant(None), Participant(None)))
                size //= 2
        else:
            raise ValueError

    def update_result(self, stage: int, match_number_stage: int, result: (int, int)):
        self.matches[stage][match_number_stage].score_participant1 = result[0]
        self.matches[stage][match_number_stage].score_participant2 = result[1]
        if result[0] > result[1]:
            winner = self.matches[stage][match_number_stage].participant1
            loser = self.matches[stage][match_number_stage].participant2
        else:
            winner = self.matches[stage][match_number_stage].participant2
            loser = self.matches[stage][match_number_stage].participant1

        if self.type == BracketType.UPPER or self.type == BracketType.SINGLE:   #TODO
            if match_number_stage % 2 == 0:
                self.matches[stage + 1][match_number_stage//2].participant1 = winner
            else:
                self.matches[stage + 1][match_number_stage//2].participant2 = winner
        elif self.type == BracketType.LOWER:
            pass
            # if match_number_stage % 4 == 0:
            #     self.matches[stage + 1][match_number_stage//4].participant1 = winner
            # else:
            #     self.matches[stage + 1][match_number_stage//4].participant2 = winner

