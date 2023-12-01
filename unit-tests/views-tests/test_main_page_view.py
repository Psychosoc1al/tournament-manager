from unittest.mock import Mock

import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton
from pytestqt.qtbot import QtBot  # install as pytest-qt

from model.tournament import Tournament
from views.main_page_view import MainPageView


class TestMainPageView:
    def test_add_button_shown(self, qtbot: QtBot, main_window: MainPageView):
        with qtbot.waitActive(main_window):
            assert main_window.findChild(QPushButton).text() == "Add tournament"

    def test_add_button_click(self, qtbot: QtBot, main_window: MainPageView):
        is_button_clicked = False

        def _set_clicked_true():
            nonlocal is_button_clicked
            is_button_clicked = True

        main_window.add_tournament_button.clicked.connect(_set_clicked_true)

        with qtbot.waitActive(main_window):
            qtbot.mouseClick(
                main_window.add_tournament_button, Qt.MouseButton.LeftButton
            )

        assert is_button_clicked

    def test_tournament_added(self, qtbot: QtBot, main_window: MainPageView):
        mock_tournament = Mock()
        mock_tournament.name = "Mocked Tournament"

        main_window.show_tournaments(
            [
                mock_tournament,
            ]
        )

        with qtbot.waitActive(main_window):
            qtbot.mouseClick(
                main_window.add_tournament_button, Qt.MouseButton.LeftButton
            )

        assert (
            main_window.tournaments_list_widget.findChild(QPushButton).text()
            == "Mocked Tournament"
        )

    def test_multiple_tournaments_added(self, qtbot: QtBot, main_window: MainPageView):
        tournaments_amount = 10
        tournaments_list: list[Tournament] = []

        for i in range(tournaments_amount):
            tournament = Mock()
            tournament.name = f"Mocked Tournament {i}"
            tournaments_list.append(tournament)

        main_window.show_tournaments(tournaments_list)

        for elem in tournaments_list:
            print(elem.name, id(elem))

        with qtbot.waitActive(main_window):
            qtbot.mouseClick(
                main_window.add_tournament_button, Qt.MouseButton.LeftButton
            )

        assert main_window.tournaments_list_widget.count() == tournaments_amount

    @pytest.fixture(autouse=True)
    def main_window(self, qtbot: QtBot):
        window = MainPageView()
        qtbot.addWidget(window)

        yield window

        window.close()
