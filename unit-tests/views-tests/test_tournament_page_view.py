from unittest.mock import Mock

import pytest
from PyQt6.QtWidgets import QPushButton
from pytestqt.qtbot import QtBot

from model.match import Match
from views.tournament_page_view import TournamentPageView


class TestTournamentPageView:
    @pytest.fixture
    def tournament_page_view(self, qtbot: QtBot):
        match = Mock(spec=Match)
        match.participant1.name = "Participant 1"
        match.participant2.name = "Participant 2"
        match.score_participant1 = 4
        match.score_participant2 = 3
        window = TournamentPageView(2, [[match, match], [match, match]])
        qtbot.addWidget(window)

        yield window

        window.close()

    def test_set_info_data(self, tournament_page_view, qtbot):
        name = "Tournament 1"
        sport = "Football"
        date = "2023-01-01"
        participants_amount = "4"

        tournament_page_view.set_info_data(name, sport, date, participants_amount)
        with qtbot.waitExposed(tournament_page_view):
            assert tournament_page_view._name_label.text() == "Name: " + name
            assert tournament_page_view._sport_label.text() == "Sport: " + sport
            assert tournament_page_view._date_label.text() == "Date: " + date
            assert (
                tournament_page_view._participants_amount_label.text()
                == "Participants: " + participants_amount
            )

    def test_back_to_main_menu(self, tournament_page_view, qtbot):
        with qtbot.waitExposed(tournament_page_view):
            assert (
                tournament_page_view.findChild(QPushButton).text()
                == "Back to main menu"
            )

    def test_redraw(self, tournament_page_view, qtbot, monkeypatch):
        mock_create_bracket = Mock()
        monkeypatch.setattr(
            "views.tournament_page_view.GraphicsView.create_bracket",
            mock_create_bracket,
        )
        tournament_page_view.redraw()

        mock_create_bracket.assert_called_once()
