from datetime import date

from PyQt6.QtCore import QRegularExpression, pyqtSignal, QObject
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QLineEdit, QListWidgetItem

from model.tournament import Tournament
from views.add_edit_page_view import AddEditPageView


class AddEditPageController(QObject):
    form_submitted = pyqtSignal(str, str, str, date, str)

    def __init__(
        self, view: AddEditPageView, page_type: str, model: Tournament = None
    ) -> None:
        super().__init__()
        self._model = model
        self._view = view
        self._page_type = page_type
        self._participants_items = []

        if self._page_type == "edit":
            self._set_edit_form()
            self._view.setWindowTitle("Edit tournament - " + self._model.name)
            self._view.save_button.setEnabled(True)
        else:
            self._handle_participants_enter()
            self._view.setWindowTitle("Add tournament")

        self._handle_input_validation()
        self._view.save_button.clicked.connect(self.send_data_to_main)
        self._view.participants_amount_choose.currentIndexChanged.connect(
            lambda _: self._handle_participants_enter()
        )

    def _set_edit_form(self) -> None:
        self._view.name_edit.setText(self._model.name)
        self._view.sport_edit.setText(self._model.sport)
        self._view.date_edit.setDate(self._model.tour_date)
        self._view.format_edit.setCurrentIndex(len(self._model.brackets) - 1)
        self._view.format_edit.setDisabled(True)
        self._view.participants_amount_choose.setCurrentText(
            str(len(self._model.participants))
        )
        self._view.participants_amount_choose.setDisabled(True)

        for ind, participant in enumerate(self._model.participants):
            list_item = QListWidgetItem(self._view.participants_inputs_list)

            new_line = QLineEdit(self._view)
            new_line.setText(participant.name)
            new_line.setDisabled(True)

            list_item.setSizeHint(new_line.sizeHint())
            self._view.participants_inputs_list.setItemWidget(list_item, new_line)
            self._participants_items.append(new_line)

    def _handle_participants_enter(self) -> None:
        self._participants_items.clear()
        self._participants_items = self._view.create_participants_form()

        self._handle_input_validation()

    def _handle_input_validation(self) -> None:
        self._view.save_button.setDisabled(True)
        self._view.name_edit.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(r"[\wа-яА-ЯёЁ][\wа-яА-ЯёЁ ]{19}"),
            )
        )

        self._view.sport_edit.setValidator(
            QRegularExpressionValidator(
                QRegularExpression(r"[\wа-яА-ЯёЁ][\wа-яА-ЯёЁ ]{19}"),
            )
        )

        self._line_edits = self._view.findChildren(QLineEdit)
        for ind, widget in enumerate(self._line_edits):
            if ind < 3:
                widget.setValidator(
                    QRegularExpressionValidator(
                        QRegularExpression(r"[\wа-яА-ЯёЁ][\wа-яА-ЯёЁ ]{9}"),
                    )
                )

            widget.textChanged.connect(self._handle_button_enabling)

    def _handle_button_enabling(self):
        self._view.save_button.setDisabled(True)

        for widget in self._line_edits:
            try:
                if not widget.text():
                    return
            except RuntimeError:
                ...

        self._view.save_button.setEnabled(True)

    def send_data_to_main(self) -> None:
        participants = "\n".join(
            list_item.text() for list_item in self._participants_items
        )

        name = self._view.name_edit.text()
        sport = self._view.sport_edit.text()
        tournament_date = self._view.date_edit.date().toPyDate()
        tournament_format = self._view.format_edit.currentText()

        self.form_submitted.emit(
            name, sport, tournament_format, tournament_date, participants
        )

        self._view.close()
