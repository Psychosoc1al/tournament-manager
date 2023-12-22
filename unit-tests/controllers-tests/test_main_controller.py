from datetime import date
from unittest.mock import Mock, patch, MagicMock

import pytest

from controllers.main_controller import MainController


class TestMainController:
    def test_view_property(self, main_controller: MainController):
        assert main_controller.view == main_controller._view

    def test_model_property(self, main_controller: MainController):
        assert main_controller.model == main_controller._model

    def test_shows_right_main_page(self, main_controller: MainController):
        main_controller.view.central_stacked_widget.setCurrentIndex.assert_called_once_with(
            0
        )
        main_controller.view.setWindowTitle.assert_called_once_with("Главное меню")
        main_controller.view.resize_screen_percent_and_center.assert_called_once_with(
            1 / 2, 1 / 2
        )

    @patch("controllers.main_controller.Tournament")
    @patch("controllers.main_controller.Participant")
    @patch("controllers.main_controller.AddEditPageController")
    @patch("controllers.main_controller.AddEditPageView")
    def test_add_button_click(
        self,
        _,
        AddEditPageController: MagicMock,
        Participant: MagicMock,
        Tournament: MagicMock,
        main_controller: MainController,
    ):
        Tournament.return_value = MagicMock()

        main_controller.view.add_tournament_button.clicked.connect.assert_called_once()

        main_controller._add_tournament_show()

        AddEditPageController.return_value.form_submitted.connect.assert_called_once()

        main_controller._add_tournament(
            "Name",
            "Sport",
            "Type",
            date(2020, 1, 1),
            "Participants",
        )

        Tournament.assert_called_once_with(
            "Name", "Sport", "Type", date(2020, 1, 1), [Participant("Participants")]
        )

    @pytest.fixture()
    def main_controller(self):
        main_page = Mock()
        main_page_view = Mock()

        main_page_view.show_tournaments.return_value = {}

        main_controller = MainController(main_page, main_page_view)

        yield main_controller
