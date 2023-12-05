from typing import Any
from unittest.mock import MagicMock, patch

from model.bracket import Bracket, BracketType, Participant


class MockParticipant(MagicMock):
    def __init__(self, name: str = "???"):
        super().__init__()
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class MockMatch(MagicMock):
    def __init__(
        self,
        stage: int,
        match_number_stage: int,
        participant1: Participant,
        participant2: Participant,
        score_participant1: int = 0,
        score_participant2: int = 0,
        *args: Any,
        **kw: Any,
    ):
        super().__init__(*args, **kw)
        self.stage = stage
        self.match_number_stage = match_number_stage
        self.participant1 = participant1
        self.participant2 = participant2
        self.score_participant1 = score_participant1
        self.score_participant2 = score_participant2

    @property
    def participant2(self) -> Participant:
        return self._participant2

    @participant2.setter
    def participant2(self, value):
        self._participant2 = value


class TestBracket:
    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_generate_bracket_single_positive(self):
        bracket = Bracket(BracketType.SINGLE)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)

        assert len(bracket.matches) == 4
        assert len(bracket.matches[0]) == 8
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 1
        assert bracket.matches[0][0].participant1 == participants[0]
        assert bracket.matches[0][0].participant2 == participants[1]
        assert bracket.matches[0][1].participant1 == participants[2]
        assert bracket.matches[0][1].participant2 == participants[3]
        assert bracket.matches[0][2].participant1 == participants[4]
        assert bracket.matches[0][2].participant2 == participants[5]
        assert bracket.matches[0][3].participant1 == participants[6]
        assert bracket.matches[0][3].participant2 == participants[7]
        assert bracket.matches[0][4].participant1 == participants[8]
        assert bracket.matches[0][4].participant2 == participants[9]
        assert bracket.matches[0][5].participant1 == participants[10]
        assert bracket.matches[0][5].participant2 == participants[11]
        assert bracket.matches[0][6].participant1 == participants[12]
        assert bracket.matches[0][6].participant2 == participants[13]
        assert bracket.matches[0][7].participant1 == participants[14]
        assert bracket.matches[0][7].participant2 == participants[15]
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1.name == "???"
        assert bracket.matches[1][3].participant2.name == "???"
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_generate_bracket_single_negative(self):
        bracket = Bracket(BracketType.SINGLE)
        participants = [MockParticipant(str(x)) for x in range(1, 15)]
        bracket.generate_bracket(participants)

        assert len(bracket.matches) == 4
        assert len(bracket.matches[0]) == 8
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 1
        assert bracket.matches[0][0].participant1 == participants[0]
        assert bracket.matches[0][0].participant2 == participants[1]
        assert bracket.matches[0][1].participant1 == participants[2]
        assert bracket.matches[0][1].participant2 == participants[3]
        assert bracket.matches[0][2].participant1 == participants[4]
        assert bracket.matches[0][2].participant2 == participants[5]
        assert bracket.matches[0][3].participant1 == participants[6]
        assert bracket.matches[0][3].participant2 == participants[7]
        assert bracket.matches[0][4].participant1 == participants[8]
        assert bracket.matches[0][4].participant2 == participants[9]
        assert bracket.matches[0][5].participant1 == participants[10]
        assert bracket.matches[0][5].participant2 == participants[11]
        assert bracket.matches[0][6].participant1 == participants[12]
        assert bracket.matches[0][6].participant2.name == "???"
        assert bracket.matches[0][7].participant1 == participants[13]
        assert bracket.matches[0][7].participant2.name == "???"
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1 == participants[12]
        assert bracket.matches[1][3].participant2 == participants[13]
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_generate_bracket_upper_positive(self):
        bracket = Bracket(BracketType.UPPER)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)

        assert len(bracket.matches) == 4
        assert len(bracket.matches[0]) == 8
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 1
        assert bracket.matches[0][0].participant1 == participants[0]
        assert bracket.matches[0][0].participant2 == participants[1]
        assert bracket.matches[0][1].participant1 == participants[2]
        assert bracket.matches[0][1].participant2 == participants[3]
        assert bracket.matches[0][2].participant1 == participants[4]
        assert bracket.matches[0][2].participant2 == participants[5]
        assert bracket.matches[0][3].participant1 == participants[6]
        assert bracket.matches[0][3].participant2 == participants[7]
        assert bracket.matches[0][4].participant1 == participants[8]
        assert bracket.matches[0][4].participant2 == participants[9]
        assert bracket.matches[0][5].participant1 == participants[10]
        assert bracket.matches[0][5].participant2 == participants[11]
        assert bracket.matches[0][6].participant1 == participants[12]
        assert bracket.matches[0][6].participant2 == participants[13]
        assert bracket.matches[0][7].participant1 == participants[14]
        assert bracket.matches[0][7].participant2 == participants[15]
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1.name == "???"
        assert bracket.matches[1][3].participant2.name == "???"
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_generate_bracket_upper_negative(self):
        bracket = Bracket(BracketType.UPPER)
        participants = [MockParticipant(str(x)) for x in range(1, 15)]
        bracket.generate_bracket(participants)

        assert len(bracket.matches) == 4
        assert len(bracket.matches[0]) == 8
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 1
        assert bracket.matches[0][0].participant1 == participants[0]
        assert bracket.matches[0][0].participant2 == participants[1]
        assert bracket.matches[0][1].participant1 == participants[2]
        assert bracket.matches[0][1].participant2 == participants[3]
        assert bracket.matches[0][2].participant1 == participants[4]
        assert bracket.matches[0][2].participant2 == participants[5]
        assert bracket.matches[0][3].participant1 == participants[6]
        assert bracket.matches[0][3].participant2 == participants[7]
        assert bracket.matches[0][4].participant1 == participants[8]
        assert bracket.matches[0][4].participant2 == participants[9]
        assert bracket.matches[0][5].participant1 == participants[10]
        assert bracket.matches[0][5].participant2 == participants[11]
        assert bracket.matches[0][6].participant1 == participants[12]
        assert bracket.matches[0][6].participant2.name == "???"
        assert bracket.matches[0][7].participant1 == participants[13]
        assert bracket.matches[0][7].participant2.name == "???"
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1 == participants[12]
        assert bracket.matches[1][3].participant2 == participants[13]
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_generate_bracket_lower_positive(self):
        bracket = Bracket(BracketType.LOWER)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)

        assert len(bracket.matches) == 7
        assert len(bracket.matches[0]) == 4
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 2
        assert len(bracket.matches[4]) == 1
        assert len(bracket.matches[5]) == 1
        assert len(bracket.matches[6]) == 1
        assert bracket.matches[0][0].participant1.name == "???"
        assert bracket.matches[0][0].participant2.name == "???"
        assert bracket.matches[0][1].participant1.name == "???"
        assert bracket.matches[0][1].participant2.name == "???"
        assert bracket.matches[0][2].participant1.name == "???"
        assert bracket.matches[0][2].participant2.name == "???"
        assert bracket.matches[0][3].participant1.name == "???"
        assert bracket.matches[0][3].participant2.name == "???"
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1.name == "???"
        assert bracket.matches[1][3].participant2.name == "???"
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"
        assert bracket.matches[3][1].participant1.name == "???"
        assert bracket.matches[3][1].participant2.name == "???"
        assert bracket.matches[4][0].participant1.name == "???"
        assert bracket.matches[4][0].participant2.name == "???"
        assert bracket.matches[5][0].participant1.name == "???"
        assert bracket.matches[5][0].participant2.name == "???"
        assert bracket.matches[6][0].participant1.name == "???"
        assert bracket.matches[6][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_generate_bracket_lower_negative(self):
        bracket = Bracket(BracketType.LOWER)
        participants = [MockParticipant(str(x)) for x in range(1, 15)]
        bracket.generate_bracket(participants)

        assert len(bracket.matches) == 7
        assert len(bracket.matches[0]) == 4
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 2
        assert len(bracket.matches[4]) == 1
        assert len(bracket.matches[5]) == 1
        assert bracket.matches[0][0].participant1.name == "???"
        assert bracket.matches[0][0].participant2.name == "???"
        assert bracket.matches[0][1].participant1.name == "???"
        assert bracket.matches[0][1].participant2.name == "???"
        assert bracket.matches[0][2].participant1.name == "???"
        assert bracket.matches[0][2].participant2.name == "???"
        assert bracket.matches[0][3].participant1.name == "???"
        assert bracket.matches[0][3].participant2.name == "???"
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1.name == "???"
        assert bracket.matches[1][3].participant2.name == "???"
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"
        assert bracket.matches[3][1].participant1.name == "???"
        assert bracket.matches[3][1].participant2.name == "???"
        assert bracket.matches[4][0].participant1.name == "???"
        assert bracket.matches[4][0].participant2.name == "???"
        assert bracket.matches[5][0].participant1.name == "???"
        assert bracket.matches[5][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_update_result(self):
        bracket = Bracket(BracketType.SINGLE)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)
        bracket.update_result(0, 0, (-1, 0))
        bracket.update_result(0, 1, (0, 1))
        bracket.update_result(0, 2, (0, 2))
        bracket.update_result(0, 3, (0, 3))
        bracket.update_result(0, 4, (0, 4))
        bracket.update_result(0, 5, (0, 5))
        bracket.update_result(0, 6, (0, 6))
        bracket.update_result(0, 7, (0, 7))
        bracket.update_result(1, 0, (-1, 0))

        assert bracket.matches[1][0].participant1 == participants[1]
        assert bracket.matches[1][0].participant2 == participants[3]
        assert bracket.matches[1][1].participant1 == participants[5]
        assert bracket.matches[1][1].participant2 == participants[7]
        assert bracket.matches[1][2].participant1 == participants[9]
        assert bracket.matches[1][2].participant2 == participants[11]
        assert bracket.matches[1][3].participant1 == participants[13]
        assert bracket.matches[1][3].participant2 == participants[15]
        assert bracket.matches[2][0].participant1 == participants[3]
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_take_winner(self):
        bracket = Bracket(BracketType.SINGLE)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)
        bracket.update_result(0, 0, (-1, 0))
        bracket.update_result(0, 1, (0, 1))
        bracket.update_result(0, 2, (0, 2))
        bracket.update_result(0, 3, (0, 3))
        bracket.update_result(0, 4, (0, 4))
        bracket.update_result(0, 5, (0, 5))
        bracket.update_result(0, 6, (0, 6))
        bracket.update_result(0, 7, (0, 7))
        bracket.update_result(1, 0, (-1, 0))
        bracket.update_result(1, 1, (0, 1))
        bracket.update_result(1, 2, (0, 2))
        bracket.update_result(1, 3, (0, 3))
        bracket.update_result(2, 0, (-1, 0))
        bracket.update_result(2, 1, (0, 1))
        bracket.update_result(3, 0, (-1, 0))
        winner = bracket.take_winner()
        assert winner == participants[15]

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_take_loser(self):
        bracket = Bracket(BracketType.LOWER)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)
        match = MockMatch(0, 0, participants[0], participants[1], 0, 1)
        bracket.take_loser(match)
        print("qwertyuiopokjhgfdszxcvbnm,l;poiuytreds")

        assert len(bracket.matches) == 7
        assert len(bracket.matches[0]) == 4
        assert len(bracket.matches[1]) == 4
        assert len(bracket.matches[2]) == 2
        assert len(bracket.matches[3]) == 2
        assert len(bracket.matches[4]) == 1
        assert len(bracket.matches[5]) == 1
        assert len(bracket.matches[6]) == 1
        assert bracket.matches[0][0].participant1 == participants[0]
        assert bracket.matches[0][0].participant2.name == "???"
        assert bracket.matches[0][1].participant1.name == "???"
        assert bracket.matches[0][1].participant2.name == "???"
        assert bracket.matches[0][2].participant1.name == "???"
        assert bracket.matches[0][2].participant2.name == "???"
        assert bracket.matches[0][3].participant1.name == "???"
        assert bracket.matches[0][3].participant2.name == "???"
        assert bracket.matches[1][0].participant1.name == "???"
        assert bracket.matches[1][0].participant2.name == "???"
        assert bracket.matches[1][1].participant1.name == "???"
        assert bracket.matches[1][1].participant2.name == "???"
        assert bracket.matches[1][2].participant1.name == "???"
        assert bracket.matches[1][2].participant2.name == "???"
        assert bracket.matches[1][3].participant1.name == "???"
        assert bracket.matches[1][3].participant2.name == "???"
        assert bracket.matches[2][0].participant1.name == "???"
        assert bracket.matches[2][0].participant2.name == "???"
        assert bracket.matches[2][1].participant1.name == "???"
        assert bracket.matches[2][1].participant2.name == "???"
        assert bracket.matches[3][0].participant1.name == "???"
        assert bracket.matches[3][0].participant2.name == "???"
        assert bracket.matches[3][1].participant1.name == "???"
        assert bracket.matches[3][1].participant2.name == "???"
        assert bracket.matches[4][0].participant1.name == "???"
        assert bracket.matches[4][0].participant2.name == "???"
        assert bracket.matches[5][0].participant1.name == "???"
        assert bracket.matches[5][0].participant2.name == "???"
        assert bracket.matches[6][0].participant1.name == "???"
        assert bracket.matches[6][0].participant2.name == "???"

    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    def test_create_final(self):
        bracket = Bracket(BracketType.LOWER)
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        bracket.generate_bracket(participants)
        bracket.create_final(MockParticipant("test"))

        assert bracket.matches[-1][0].participant2.name == "test"
