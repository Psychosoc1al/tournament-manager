from datetime import datetime

from PyQt6.QtCore import QSize, pyqtSignal, QDate
from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, \
    QDateEdit


class AddEditPageView(QWidget):
    form_submitted = pyqtSignal(str, str, int, int, str, str)

    def __init__(self, parent: QWidget, window_type: str):
        super().__init__()

        self.setFixedSize(QSize(450, 500))

        self._create_add_edit_form()

    def _create_add_edit_form(self):
        self.name_label = QLabel('Tournament name:')
        self.name_edit = QLineEdit()

        self.sport_label = QLabel('Sport type:')
        self.sport_edit = QLineEdit()

        self.date_label = QLabel('Дата проведения:')
        self.date_edit = QDateEdit()

        self.format_label = QLabel('Tournament type:')
        self.format_edit = QComboBox()
        self.format_edit.addItems(['Single elimination', 'Double elimination'])

        self.participants_label = QLabel('Participants amount:')
        self.participants_amount_edit = QLineEdit()

        self.participants_form_label = QLabel('Participants:')
        self.participants_edit = QTextEdit()

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.saveData)

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_edit)
        vbox.addWidget(self.sport_label)
        vbox.addWidget(self.sport_edit)
        vbox.addWidget(self.format_label)
        vbox.addWidget(self.format_edit)
        vbox.addWidget(self.participants_label)
        vbox.addWidget(self.participants_amount_edit)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.participants_form_label)
        vbox.addWidget(self.participants_edit)
        vbox.addWidget(self.save_button)

        self.setLayout(vbox)

    def saveData(self): # Нужно как-то вернуть эти данные
        name = self.name_edit.text()
        sport = self.sport_edit.text()
        format = self.format_edit.currentIndex()
        participants = int(self.participants_amount_edit.text())
        date = self.date_edit.date()
        participants_form = self.participants_edit.toPlainText()
        self.form_submitted.emit(name, sport, format, participants, date.toPyDate(), participants_form)
        self.close()
