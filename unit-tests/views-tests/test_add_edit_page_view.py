import pytest
from pytestqt.qtbot import QtBot  # install as pytest-qt

from views.add_edit_page_view import AddEditPageView


class TestAddEditPageView:
    def test_save_button_inactive_by_default(
        self, qtbot: QtBot, main_window: AddEditPageView
    ):
        with qtbot.waitExposed(main_window):
            assert not main_window.save_button.isEnabled()

    @pytest.fixture(autouse=True)
    def main_window(self, qtbot: QtBot):
        window = AddEditPageView()
        qtbot.addWidget(window)

        yield window

        window.close()
