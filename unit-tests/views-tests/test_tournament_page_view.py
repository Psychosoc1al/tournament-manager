from unittest.mock import Mock

import pytest
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QWheelEvent
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

    def test_set_info_data(
        self, tournament_page_view: TournamentPageView, qtbot: QtBot
    ):
        name = "Tournament 1"
        sport = "Football"
        date = "2023-01-01"
        participants_amount = "4"

        tournament_page_view.set_info_data(name, sport, date, participants_amount)
        with qtbot.waitExposed(tournament_page_view):
            assert tournament_page_view._name_label.text() == "Название: " + name
            assert tournament_page_view._sport_label.text() == "Вид спорта: " + sport
            assert tournament_page_view._date_label.text() == "Дата проведения: " + date
            assert (
                tournament_page_view._participants_amount_label.text()
                == "Участники: " + participants_amount
            )

    def test_back_to_main_menu(
        self, tournament_page_view: TournamentPageView, qtbot: QtBot
    ):
        with qtbot.waitExposed(tournament_page_view):
            assert (
                tournament_page_view.findChild(QPushButton).text() == "В главное меню"
            )

    def test_redraw(self, tournament_page_view: TournamentPageView, monkeypatch):
        mock_create_bracket = Mock()
        monkeypatch.setattr(
            "views.tournament_page_view.GraphicsView.create_bracket",
            mock_create_bracket,
        )
        tournament_page_view.redraw()

        mock_create_bracket.assert_called_once()

    def test_wheel_event(self, tournament_page_view: TournamentPageView, qtbot: QtBot):
        with qtbot.waitExposed(tournament_page_view):
            qtbot.keyPress(
                tournament_page_view, " ", Qt.KeyboardModifier.ControlModifier
            )
            event = Mock(spec=QWheelEvent)
            event.angleDelta.return_value.y.return_value = 1
            event.modifiers.return_value = Qt.KeyboardModifier.ControlModifier
            tournament_page_view.graphics_view.wheelEvent(event)

            event.angleDelta.return_value.y.assert_called_once()

            event.angleDelta.return_value.y.return_value = -1
            event.modifiers.return_value = Qt.KeyboardModifier.ControlModifier
            tournament_page_view.graphics_view.wheelEvent(event)
            qtbot.keyRelease(
                tournament_page_view, " ", Qt.KeyboardModifier.ControlModifier
            )
            assert event.angleDelta.return_value.y.call_count == 3

            event.modifiers.return_value = Qt.KeyboardModifier.NoModifier
            with pytest.raises(TypeError):
                tournament_page_view.graphics_view.wheelEvent(event)

    def test_wheel_event_with_shift(
        self, tournament_page_view: TournamentPageView, qtbot: QtBot
    ):
        with qtbot.waitExposed(tournament_page_view):
            event = Mock(spec=QWheelEvent)
            event.angleDelta.return_value.y.return_value = 1
            event.modifiers.return_value = Qt.KeyboardModifier.ShiftModifier

            qtbot.keyPress(tournament_page_view, " ", Qt.KeyboardModifier.ShiftModifier)
            tournament_page_view.graphics_view.wheelEvent(event)

            event.angleDelta.return_value.y.assert_called_once()

    def test_mouse_double_click_event(self, tournament_page_view, qtbot):
        with qtbot.waitExposed(tournament_page_view):
            qtbot.mouseClick(
                tournament_page_view.graphics_view, Qt.MouseButton.LeftButton
            )
            event = Mock()
            event.button.return_value = Qt.MouseButton.LeftButton
            event.pos.return_value = QPoint(0, 0)
            tournament_page_view.graphics_view.mouseDoubleClickEvent(event)

            event.pos.assert_called_once()
