from unittest import mock

import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton
from pytestqt.qtbot import QtBot  # install as pytest-qt

from views.main_page_view import MainPageView


class TestMainPageView:
    def test_add_button_shown(self, qtbot: QtBot, window: MainPageView):
        with qtbot.waitActive(window):
            assert window.findChild(QPushButton).text() == "Add tournament"

    def test_add_button_click(self, qtbot: QtBot, window: MainPageView):
        is_button_clicked = False

        def _set_clicked_true():
            nonlocal is_button_clicked
            is_button_clicked = True

        window.add_tournament_button.clicked.connect(_set_clicked_true)

        with qtbot.waitActive(window):
            qtbot.mouseClick(window.add_tournament_button, Qt.MouseButton.LeftButton)

        assert is_button_clicked

    def test_tournament_added(self, qtbot: QtBot, window: MainPageView):
        with mock.patch("model.tournament.Tournament") as MockTournament:
            tournament = MockTournament.return_value
            tournament.name = "Mocked Tournament"

            window.show_tournaments(
                [
                    tournament,
                ]
            )

            with qtbot.waitActive(window):
                qtbot.mouseClick(
                    window.add_tournament_button, Qt.MouseButton.LeftButton
                )

        assert (
            window.tournaments_list_widget.findChild(QPushButton).text()
            == "Mocked Tournament"
        )

    @pytest.fixture(autouse=True)
    def window(self, qtbot: QtBot):
        window = MainPageView()
        qtbot.addWidget(window)

        yield window

        window.close()
