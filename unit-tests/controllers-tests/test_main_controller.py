from unittest.mock import Mock, patch

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
        main_controller.view.setWindowTitle.assert_called_once_with("Main menu")
        main_controller.view.resize_screen_percent_and_center.assert_called_once_with(
            1 / 2, 1 / 2
        )

    # noinspection PyUnusedLocal
    @patch("controllers.main_controller.AddEditPageController")
    @patch("controllers.main_controller.AddEditPageView")
    def test_update_button_click(
        self, AddEditPageView, AddEditPageController, main_controller: MainController
    ):
        update_button = Mock()
        tournament = Mock()
        update_button.clicked.connect.side_effect = (
            lambda _: main_controller._update_tournament_show(tournament)
        )

        main_controller.view.show_tournaments.return_value = {"update": [update_button]}
        main_controller.show_main_page()

        assert main_controller._updating_tournament == tournament

    @pytest.fixture(autouse=True)
    def main_controller(self):
        main_page = Mock()
        main_page_view = Mock()

        main_page_view.show_tournaments.return_value = {}

        main_controller = MainController(main_page, main_page_view)

        yield main_controller
