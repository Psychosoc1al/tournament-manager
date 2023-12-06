from unittest.mock import Mock, MagicMock, patch

import pytest

from controllers.tournament_page_controller import TournamentPageController
from views.tournament_page_view import RectangleObject


class TestTournamentPageController:
    def test_connect_match_areas(
        self, tournament_page_controller: TournamentPageController
    ):
        tournament_page_controller._view.graphics_view.scene.return_value.items.return_value = [
            MagicMock(spec=RectangleObject)
        ]
        tournament_page_controller._connect_match_areas()

        tournament_page_controller._view.graphics_view.scene().items.return_value[
            0
        ].clicked_signal.connect.assert_called_once()

    @patch("controllers.tournament_page_controller.MatchResultPageController")
    @patch("controllers.tournament_page_controller.MatchResultPageView")
    def test_show_match_result_page(
        self,
        MatchResultPageView,
        MatchResultPageController,
        tournament_page_controller: TournamentPageController,
    ):
        tournament_page_controller._show_match_result_page(0, 0)

        MatchResultPageView.assert_called_once()
        MatchResultPageController.assert_called_once_with(
            MatchResultPageView.return_value
        )

    def test_update_match_result(
        self, tournament_page_controller: TournamentPageController
    ):
        match = Mock()
        tournament_page_controller._update_match_result(match, 0, 0, 0, 0)

        tournament_page_controller._model.brackets[
            0
        ].update_result.assert_called_once_with(0, 0, (0, 0))

        match.score_participant1 = 0
        match.score_participant2 = 0
        tournament_page_controller._update_match_result(match, 0, 0, 0, 0)

        tournament_page_controller._model.brackets[
            0
        ].update_result.assert_called_once_with(0, 0, (0, 0))

    @pytest.fixture()
    def tournament_page_controller(self):
        tournament = MagicMock()
        tournament.participants.__len__.return_value = 4

        tournament_page_view = Mock()
        tournament_page_view.graphics_view.scene.return_value.items.return_value = []
        main_controller = Mock()

        tournament_page_controller = TournamentPageController(
            tournament, tournament_page_view, main_controller
        )
        tournament_page_controller.match_result_submitted = Mock()

        yield tournament_page_controller
