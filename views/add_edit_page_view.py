from datetime import date

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, \
    QDateEdit, QListWidget, QDialog, QMainWindow


class AddEditPageView(QDialog):
    form_submitted = pyqtSignal(str, str, str, date, str)

    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)
        self.setMinimumSize(450, 500)

        self._create_add_edit_form()
        self.show()

    def _create_add_edit_form(self) -> None:
        name_label = QLabel('Tournament name:')
        self.name_edit = QLineEdit()

        sport_label = QLabel('Sport type:')
        self.sport_edit = QLineEdit()

        date_label = QLabel('Date:')
        self.date_edit = QDateEdit()

        format_label = QLabel('Tournament type:')
        self.format_edit = QComboBox()
        self.format_edit.addItems(['Single elimination', 'Double elimination'])

        participants_label = QLabel('Participants amount:')
        self.participants_amount_choose = QComboBox()
        self.participants_amount_choose.addItems(['4', '8', '16', '32'])

        participants_form_label = QLabel('Participants:')
        self.participants_inputs_list = QListWidget()
        self.participants_inputs_list.setSpacing(1)

        self.save_button = QPushButton('Save')

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(name_label)
        main_layout.addWidget(self.name_edit)
        main_layout.addWidget(sport_label)
        main_layout.addWidget(self.sport_edit)
        main_layout.addWidget(format_label)
        main_layout.addWidget(self.format_edit)
        main_layout.addWidget(participants_label)
        main_layout.addWidget(self.participants_amount_choose)
        main_layout.addWidget(date_label)
        main_layout.addWidget(self.date_edit)
        main_layout.addWidget(participants_form_label)
        main_layout.addWidget(self.participants_inputs_list, 1)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)

    def send_data_to_main(self, participants: str) -> None:
        name = self.name_edit.text()
        sport = self.sport_edit.text()
        tournament_date = self.date_edit.date().toPyDate()
        tournament_format = self.format_edit.currentText()

        self.form_submitted.emit(
            name,
            sport,
            tournament_format,
            tournament_date,
            participants
        )

        self.close()
