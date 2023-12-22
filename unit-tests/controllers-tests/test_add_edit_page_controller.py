from datetime import date
from unittest.mock import Mock, MagicMock, patch

import pytest

from controllers.add_edit_page_controller import AddEditPageController


@patch("controllers.add_edit_page_controller.QRegularExpressionValidator")
@patch("controllers.add_edit_page_controller.QRegularExpression")
class TestAddEditPageController:
    def test_correct_add_window_title(
        self, _, __, add_controller: AddEditPageController
    ):
        add_controller._view.setWindowTitle.assert_called_once_with("Добавить турнир")

    def test_correct_edit_window_title(
        self, _, __, edit_controller: AddEditPageController
    ):
        edit_controller._view.setWindowTitle.assert_called_once_with(
            "Edit tournament - Name"
        )

    @patch("controllers.add_edit_page_controller.QLineEdit")
    @patch("controllers.add_edit_page_controller.QListWidgetItem")
    def test_set_edit_form(
        self, _, __, ___, ____, edit_controller: AddEditPageController
    ):
        edit_controller._model.participants = [Mock(), Mock(), Mock(), Mock()]

        edit_controller._set_edit_form()

        assert len(edit_controller._participants_items) == 4
        assert (
            edit_controller._view.participants_inputs_list.setItemWidget.call_count == 4
        )

    # noinspection PyUnresolvedReferences
    def test_handle_button_enabling(
        self, _, __, edit_controller: AddEditPageController
    ):
        for elem in edit_controller._view.findChildren.return_value:
            elem.textChanged.connect.assert_called_once()

        edit_controller._view.findChildren.return_value[
            0
        ].text.side_effect = RuntimeError()
        edit_controller._view.findChildren.return_value[-1].text.return_value = "Name"
        edit_controller._handle_button_enabling()

        for elem in edit_controller._view.findChildren.return_value:
            elem.text.assert_called_once()

    # noinspection PyUnresolvedReferences
    def test_false_handle_button_enabling(
        self, _, __, edit_controller: AddEditPageController
    ):
        edit_controller._view.findChildren.return_value[0].text.return_value = ""
        edit_controller._handle_button_enabling()

        edit_controller._view.save_button.setEnabled.assert_called_once()

    def test_send_data_to_main(self, _, __, edit_controller: AddEditPageController):
        edit_controller._view.save_button.clicked.connect.assert_called_once()

        edit_controller._view.name_edit.text.return_value = "Name"
        edit_controller._view.sport_edit.text.return_value = "Sport"
        edit_controller._view.format_edit.currentText.return_value = "Type"
        edit_controller._view.date_edit.date.return_value.toPyDate.return_value = date(
            2020, 1, 1
        )

        edit_controller.send_data_to_main()

        edit_controller.form_submitted.emit.assert_called_once_with(
            "Name", "Sport", "Type", date(2020, 1, 1), ""
        )

    @pytest.fixture()
    def add_controller(self):
        add_page_view = Mock()
        add_page_view.show_tournaments.return_value = {}
        add_page_view.findChildren.return_value = [Mock(), Mock(), Mock(), Mock()]

        add_controller = AddEditPageController(add_page_view, "add")
        add_controller.form_submitted = Mock()

        yield add_controller

    @pytest.fixture()
    def edit_controller(self):
        tournament = MagicMock()
        tournament.name = "Name"
        tournament.brackets.__len__.return_value = 1
        edit_page_view = Mock()
        edit_page_view.show_tournaments.return_value = {}
        edit_page_view.findChildren.return_value = [Mock(), Mock(), Mock(), Mock()]

        edit_controller = AddEditPageController(edit_page_view, "edit", tournament)
        edit_controller.form_submitted = Mock()

        yield edit_controller
