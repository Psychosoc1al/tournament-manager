from datetime import date

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, \
    QDateEdit


class AddEditPageView(QWidget):
    form_submitted = pyqtSignal(str, str, int, int, date, str)

    def __init__(self, window_type: str):
        super().__init__()

        self.setMinimumSize(450, 500)

        self._window_type = window_type

        self._create_add_edit_form()

        self.show()

    def _create_add_edit_form(self):
        self.name_label = QLabel('Tournament name:')
        self.name_edit = QLineEdit()

        self.sport_label = QLabel('Sport type:')
        self.sport_edit = QLineEdit()

        self.date_label = QLabel('Date:')
        self.date_edit = QDateEdit()

        self.format_label = QLabel('Tournament type:')
        self.format_edit = QComboBox()
        self.format_edit.addItems(['Single elimination', 'Double elimination'])

        self.participants_label = QLabel('Participants amount:')
        self.participants_amount_choose = QComboBox()
        self.participants_amount_choose.addItems(['4', '8', '16', '32', '64'])

        self.participants_form_label = QLabel('Participants:')
        # TODO: add cycle
        self.participants_edit = QLineEdit()

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
        vbox.addWidget(self.participants_edit)
        vbox.addWidget(self.save_button)

        self.setLayout(vbox)

    def get_data(self):
        name = self.name_edit.text()
        sport = self.sport_edit.text()
        _format = self.format_edit.currentText()
        participants_amount = int(self.participants_amount_choose.currentText())
        _date = self.date_edit.date()
        participants = self.participants_edit.toPlainText()

        self.form_submitted.emit(
            name,
            sport,
            _format,
            participants_amount,
            _date.toPyDate(),
            participants
        )

        self.close()
