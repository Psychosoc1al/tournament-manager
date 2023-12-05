from datetime import date
from typing import Any
from unittest.mock import Mock, MagicMock, patch

import pytest
from model.tournament import (
    Tournament,
    TournamentType,
    Bracket,
    BracketType,
    Participant,
)


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


class MockBracket(MagicMock):
    def __init__(self, bracket_type: BracketType) -> None:
        super().__init__()
        self.bracket_type = bracket_type
        self.matches = []

    @property
    def bracket_type(self) -> BracketType:
        return self._type

    @bracket_type.setter
    def bracket_type(self, value: BracketType) -> None:
        self._type = value

    @property
    def matches(self) -> list[list[MockMatch]]:
        return self._matches

    @matches.setter
    def matches(self, value: list[list[MockMatch]]) -> None:
        self._matches = value


class TestTournament:
    @patch("model.bracket.Participant", new=MockParticipant)
    @patch("model.bracket.Match", new=MockMatch)
    @patch("model.bracket.Bracket", new=MockBracket)
    def test_create_bracket_positive(self):
        participants = [MockParticipant(str(x)) for x in range(1, 17)]
        tournament = Tournament(
            "name", "sport", TournamentType.SINGLE, date(2021, 1, 1), participants
        )
        bracket = tournament.brackets[0]
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
    @patch("model.bracket.Bracket", new=MockBracket)
    def test_create_bracket_negative(self):
        participants = [MockParticipant(str(x)) for x in range(1, 15)]
        tournament = Tournament(
            "name", "sport", TournamentType.SINGLE, date(2021, 1, 1), participants
        )
        bracket = tournament.brackets[0]
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
    @patch("model.bracket.Bracket", new=MockBracket)
    def test_update_result_negative(self):
        participants = [MockParticipant(str(x)) for x in range(1, 15)]
        tournament = Tournament(
            "name", "sport", TournamentType.SINGLE, date(2021, 1, 1), participants
        )
        tournament.update_result(0, 0, (1, 0))
        tournament.update_result(0, 1, (1, 0))
        tournament.update_result(0, 2, (1, 0))
        tournament.update_result(0, 3, (1, 0))
        tournament.update_result(0, 4, (1, 0))
        tournament.update_result(0, 5, (1, 0))
        tournament.update_result(0, 6, (1, 0))
        tournament.update_result(0, 7, (1, 0))
        tournament.update_result(1, 0, (1, 0))
        tournament.update_result(1, 1, (1, 0))
        tournament.update_result(1, 2, (1, 0))
        tournament.update_result(1, 3, (1, 0))
        tournament.update_result(2, 0, (1, 0))
        tournament.update_result(2, 1, (1, 0))
        tournament.update_result(3, 0, (1, 0))

        assert tournament.winner == participants[0]
        assert len(tournament.brackets) == 1
        assert len(tournament.brackets[0].matches) == 4
        assert len(tournament.brackets[0].matches[0]) == 8
        assert len(tournament.brackets[0].matches[1]) == 4
        assert len(tournament.brackets[0].matches[2]) == 2
        assert len(tournament.brackets[0].matches[3]) == 1
        assert tournament.brackets[0].matches[0][0].participant1 == participants[0]
        assert tournament.brackets[0].matches[0][0].participant2 == participants[1]
        assert tournament.brackets[0].matches[0][1].participant1 == participants[2]
        assert tournament.brackets[0].matches[0][1].participant2 == participants[3]
        assert tournament.brackets[0].matches[0][2].participant1 == participants[4]
        assert tournament.brackets[0].matches[0][2].participant2 == participants[5]
        assert tournament.brackets[0].matches[0][3].participant1 == participants[6]
        assert tournament.brackets[0].matches[0][3].participant2 == participants[7]
        assert tournament.brackets[0].matches[0][4].participant1 == participants[8]
        assert tournament.brackets[0].matches[0][4].participant2 == participants[9]
        assert tournament.brackets[0].matches[0][5].participant1 == participants[10]
        assert tournament.brackets[0].matches[0][5].participant2 == participants[11]
        assert tournament.brackets[0].matches[0][6].participant1 == participants[12]
        assert tournament.brackets[0].matches[0][6].participant2.name == "???"
        assert tournament.brackets[0].matches[0][7].participant1 == participants[13]
        assert tournament.brackets[0].matches[0][7].participant2.name == "???"
        assert tournament.brackets[0].matches[1][0].participant1 == participants[0]
        assert tournament.brackets[0].matches[1][0].participant2 == participants[2]
        assert tournament.brackets[0].matches[1][1].participant1 == participants[4]
        assert tournament.brackets[0].matches[1][1].participant2 == participants[6]
        assert tournament.brackets[0].matches[1][2].participant1 == participants[8]
        assert tournament.brackets[0].matches[1][2].participant2 == participants[10]
        assert tournament.brackets[0].matches[1][3].participant1 == participants[12]
        assert tournament.brackets[0].matches[1][3].participant2 == participants[13]
        assert tournament.brackets[0].matches[2][0].participant1 == participants[0]
        assert tournament.brackets[0].matches[2][0].participant2 == participants[4]
        assert tournament.brackets[0].matches[2][1].participant1 == participants[8]
        assert tournament.brackets[0].matches[2][1].participant2 == participants[12]
        assert tournament.brackets[0].matches[3][0].participant1 == participants[0]
        assert tournament.brackets[0].matches[3][0].participant2 == participants[8]
