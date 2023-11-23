from PyQt6.QtCore import Qt
from pytestqt.qtbot import QtBot  # install as pytest-qt

from views.main_page_view import MainPageView


class TestMainPageView:
    def test_add_button_click(self, qtbot: QtBot):
        window = MainPageView()
        qtbot.addWidget(window)

        with qtbot.waitActive(window):
            qtbot.mouseClick(window.add_tournament_button, Qt.MouseButton.LeftButton)

        assert window.tournaments_list_widget.count() == 0
