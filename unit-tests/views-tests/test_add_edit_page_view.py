import time

import pytest
from pytestqt.qtbot import QtBot  # install as pytest-qt

from views.add_edit_page_view import AddEditPageView


class TestAddEditPageView:
    def test_save_button_inactive_by_default(
            self, qtbot: QtBot, main_window: AddEditPageView
    ):
        with qtbot.waitExposed(main_window):
            assert not main_window.save_button.isEnabled()

    def test_create_participants_form(app, qtbot: QtBot, main_window: AddEditPageView):
        main_window.participants_amount_choose.setCurrentText("4")

        participants_qlines = main_window.create_participants_form()

        with qtbot.waitExposed(main_window):
            assert len(participants_qlines) == 4

        main_window.participants_amount_choose.setCurrentText("8")

        participants_qlines = main_window.create_participants_form()

        with qtbot.waitExposed(main_window):
            assert len(participants_qlines) == 8

        main_window.participants_amount_choose.setCurrentText("16")

        participants_qlines = main_window.create_participants_form()

        with qtbot.waitExposed(main_window):
            assert len(participants_qlines) == 16

    @pytest.fixture(autouse=True)
    def main_window(self, qtbot: QtBot):
        window = AddEditPageView()
        qtbot.addWidget(window)

        yield window
        window.close()
