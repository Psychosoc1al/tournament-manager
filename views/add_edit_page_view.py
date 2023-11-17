from datetime import date

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, \
    QDateEdit, QListWidget, QDialog, QMainWindow


class AddEditPageView(QDialog):
    form_submitted = pyqtSignal(str, str, str, date, str)

    def __init__(self, parent: QMainWindow):
        super().__init__(parent)
        self.setMinimumSize(450, 500)

        self._create_add_edit_form()

    def _create_add_edit_form(self):
        self.name_label = QLabel('Tournament name:')
        self.name_edit = QLineEdit()

        self.sport_label = QLabel('Sport type:')
        self.sport_edit = QLineEdit()

        self.date_label = QLabel('Date:')
        self.date_edit = QDateEdit()

        self.format_label = QLabel('Tournament type:')
        self.format_edit = QComboBox()
        # self.format_edit.addItems(['Single elimination', 'Double elimination'])
        self.format_edit.addItems(['Single elimination'])

        self.participants_label = QLabel('Participants amount:')
        self.participants_amount_choose = QComboBox()
        self.participants_amount_choose.addItems(['4', '8', '16', '32'])

        self.participants_form_label = QLabel('Participants:')

        self.participants_inputs_list = QListWidget()
        self.participants_inputs_list.setSpacing(1)

        self.save_button = QPushButton('Save')

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_edit)
        vbox.addWidget(self.sport_label)
        vbox.addWidget(self.sport_edit)
        vbox.addWidget(self.format_label)
        vbox.addWidget(self.format_edit)
        vbox.addWidget(self.participants_label)
        vbox.addWidget(self.participants_amount_choose)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.participants_form_label)
        vbox.addWidget(self.participants_inputs_list, 1)
        vbox.addWidget(self.save_button)

        self.setLayout(vbox)

    def send_data_to_main(self, participants: str):
        name = self.name_edit.text()
        sport = self.sport_edit.text()
        tournament_format = self.format_edit.currentText()
        tournament_date = self.date_edit.date()

        self.form_submitted.emit(
            name,
            sport,
            tournament_format,
            tournament_date.toPyDate(),
            participants
        )

        self.close()
