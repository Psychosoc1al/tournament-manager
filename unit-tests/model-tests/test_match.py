from unittest.mock import Mock, MagicMock

import pytest

from model.match import Match


class TestMatch:
    @pytest.fixture
    def participant1(self):
        participant = MagicMock()
        participant.__str__.return_value = "Participant 1"
        return participant

    @pytest.fixture
    def participant2(self):
        participant = MagicMock()
        participant.__str__.return_value = "Participant 2"
        return participant

    def test_str_return(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2, 3, 2)

        assert str(match) == "Participant 1 3 vs 2 Participant 2"

    def test_stage_getter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        assert match.stage == 1

    def test_stage_setter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        match.stage = 2

        assert match.stage == 2

    def test_match_number_stage_getter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        assert match.match_number_stage == 1

    def test_match_number_stage_setter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        match.match_number_stage = 2

        assert match.match_number_stage == 2

    def test_participant1_getter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        assert match.participant1 == participant1

    def test_participant1_setter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        new_participant = Mock()
        match.participant1 = new_participant

        assert match.participant1 == new_participant

    def test_participant2_getter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        assert match.participant2 == participant2

    def test_participant2_setter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2)

        new_participant = Mock()
        match.participant2 = new_participant

        assert match.participant2 == new_participant

    def test_score_participant1_getter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2, 3, 2)

        assert match.score_participant1 == 3

    def test_score_participant1_setter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2, 3, 2)

        match.score_participant1 = 4

        assert match.score_participant1 == 4

    def test_score_participant2_getter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2, 3, 2)

        assert match.score_participant2 == 2

    def test_score_participant2_setter(self, participant1, participant2):
        match = Match(1, 1, participant1, participant2, 3, 2)
        match.score_participant2 = 1
        assert match.score_participant2 == 1
