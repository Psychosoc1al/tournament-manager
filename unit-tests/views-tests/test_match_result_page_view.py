from unittest.mock import Mock, MagicMock

import pytest
from PyQt6.QtWidgets import QMainWindow
from pytestqt.qtbot import QtBot

from match import Match
from match_result_page_view import MatchResultPageView


class TestMatchResultPageView:
    @pytest.fixture
    def match_result_page_view(self, qtbot: QtBot):
        # parent = Mock(spec=QMainWindow)
        parent = QMainWindow()
        match = Mock(spec=Match)
        match.participant1.name = "Participant 1"
        match.participant2.name = "Participant 2"
        match.score_participant1 = 4
        match.score_participant2 = 3
        window = MatchResultPageView(parent, match)
        qtbot.addWidget(window)

        yield window

        window.close()

    def test_save_button_inactive_by_default(
            self, qtbot: QtBot, match_result_page_view: MatchResultPageView
    ):
        with qtbot.waitExposed(match_result_page_view):
            assert not match_result_page_view.save_button.isEnabled()

    def test_change_score(self, qtbot: QtBot, match_result_page_view: MatchResultPageView):

        match_result_page_view.second_score.stepDown()

        with qtbot.waitExposed(match_result_page_view):
            assert match_result_page_view.second_score.text() == '2'

        match_result_page_view.second_score.stepUp()

        with qtbot.waitExposed(match_result_page_view):
            assert match_result_page_view.second_score.text() == '3'

        match_result_page_view.first_score.stepDown()

        with qtbot.waitExposed(match_result_page_view):
            assert match_result_page_view.first_score.text() == '3'

        match_result_page_view.first_score.stepUp()

        with qtbot.waitExposed(match_result_page_view):
            assert match_result_page_view.first_score.text() == '4'
