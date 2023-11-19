from PyQt6.QtWidgets import QLineEdit, QListWidgetItem

from views.add_edit_page_view import AddEditPageView
from Model.tournament import Tournament


class AddEditPageController:
    def __init__(self, view: AddEditPageView, page_type: str, model: Tournament = None) -> None:
        self._model = model
        self._view = view
        self._page_type = page_type
        self._participants_items = []

        if self._page_type == 'edit':
            self._set_edit_form()
            self._view.setWindowTitle('Edit tournament - ' + self._model.name)
        else:
            self._handle_participants_enter()
            self._view.setWindowTitle('Add tournament')

        self._view.save_button.clicked.connect(self.send_data_to_main)
        self._view.participants_amount_choose.currentIndexChanged.connect(lambda _: self._handle_participants_enter())

    def _set_edit_form(self) -> None:
        self._view.name_edit.setText(self._model.name)
        self._view.sport_edit.setText(self._model.sport)
        self._view.date_edit.setDate(self._model.tour_date)
        self._view.format_edit.setCurrentIndex(len(self._model.brackets) - 1)
        self._view.participants_amount_choose.setCurrentText(str(len(self._model.participants)))
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
        self._view.participants_inputs_list.clear()
        self._participants_items.clear()
        current_amount_str = self._view.participants_amount_choose.currentText()

        for i in range(int(current_amount_str)):
            list_item = QListWidgetItem(self._view.participants_inputs_list)

            new_line = QLineEdit(self._view)
            new_line.setPlaceholderText(f'Participant {i + 1}')

            list_item.setSizeHint(new_line.sizeHint())
            self._view.participants_inputs_list.setItemWidget(list_item, new_line)
            self._participants_items.append(new_line)

    def send_data_to_main(self) -> None:
        participants = [list_item.text() for list_item in self._participants_items]

        self._view.send_data_to_main('\n'.join(participants))
