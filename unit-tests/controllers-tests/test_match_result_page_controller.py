from unittest.mock import Mock

import pytest

from controllers.match_result_page_controller import MatchResultPageController


class TestMatchResultPageController:
    def test_handle_score_entering_equal_scores(
        self, match_result_page_controller: MatchResultPageController
    ):
        match_result_page_controller._handle_score_entering()

        match_result_page_controller._view.first_score.valueChanged.connect.called_once()
        match_result_page_controller._view.second_score.valueChanged.connect.called_once()

        match_result_page_controller._view.save_button.setDisabled.assert_called_once()
        assert match_result_page_controller._view.save_button.setEnabled.call_count == 0

    def test_handle_score_entering_not_equal_scores(
        self, match_result_page_controller: MatchResultPageController
    ):
        match_result_page_controller._view.second_score.value.return_value += 1
        match_result_page_controller._handle_score_entering()

        match_result_page_controller._view.first_score.valueChanged.connect.called_once()
        match_result_page_controller._view.second_score.valueChanged.connect.called_once()

        match_result_page_controller._view.save_button.setEnabled.assert_called_once()
        assert (
            match_result_page_controller._view.save_button.setDisabled.call_count == 0
        )

    def test_send_match_result(
        self, match_result_page_controller: MatchResultPageController
    ):
        match_result_page_controller.send_match_result()

        match_result_page_controller._view.save_button.clicked.connect.assert_called_once()
        match_result_page_controller.match_result_submitted.emit.assert_called_once_with(
            1, 1
        )

    @pytest.fixture()
    def match_result_page_controller(self):
        match_result_page_view = Mock()
        match_result_page_view.first_score.value.return_value = 1
        match_result_page_view.second_score.value.return_value = 1

        match_result_page_controller = MatchResultPageController(match_result_page_view)
        match_result_page_controller.match_result_submitted = Mock()

        yield match_result_page_controller
