from datetime import datetime

from PyQt6.QtCore import QSize, pyqtSignal, QDate
from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, \
    QDateEdit


class AddPageView(QWidget):
    data = pyqtSignal(str, str, int, int, str, str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавление турнира")
        self.setFixedSize(QSize(450, 500))
        self.initUI()

    def initUI(self):
        self.name_label = QLabel('Название турнира:')
        self.name_edit = QLineEdit()

        self.sport_label = QLabel('Вид спорта:')
        self.sport_edit = QLineEdit()

        self.format_label = QLabel('Формат проведения:')
        self.format_edit = QComboBox()
        self.format_edit.addItems(['Single elimination', 'Double elimination'])

        self.participants_label = QLabel('Количество участников:')
        self.participants_edit = QLineEdit()

        self.date_label = QLabel('Дата проведения:')
        self.date_edit = QDateEdit()

        self.participants_form_label = QLabel('Участники:')
        self.participants_form_edit = QTextEdit()

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.saveData)

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_edit)
        vbox.addWidget(self.sport_label)
        vbox.addWidget(self.sport_edit)
        vbox.addWidget(self.format_label)
        vbox.addWidget(self.format_edit)
        vbox.addWidget(self.participants_label)
        vbox.addWidget(self.participants_edit)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.participants_form_label)
        vbox.addWidget(self.participants_form_edit)
        vbox.addWidget(self.save_button)

        self.setLayout(vbox)

    def saveData(self): # Нужно как-то вернуть эти данные
        self.name = self.name_edit.text()
        self.sport = self.sport_edit.text()
        self.format = self.format_edit.currentIndex()
        self.participants = int(self.participants_edit.text())
        self.date = self.date_edit.date()
        self.participants_form = self.participants_form_edit.toPlainText()
        self.data.emit(self.name, self.sport, self.format, self.participants, self.date.toPyDate(), self.participants_form)
        self.close()



class UpdatePageView(QWidget):
    data = pyqtSignal(int, str, str, int, int, str, str)
    def __init__(self, index):
        super().__init__()
        self._index = index
        self.setWindowTitle("Изменение турнира")
        self.setFixedSize(QSize(450, 450))
        self.initUI()

    def initUI(self):
        self.name_label = QLabel('Название турнира:')
        self.name_edit = QLineEdit()

        self.sport_label = QLabel('Вид спорта:')
        self.sport_edit = QLineEdit()

        self.format_label = QLabel('Формат проведения:')
        self.format_edit = QComboBox()
        self.format_edit.addItems(['Single elimination', 'Double elimination'])

        self.participants_label = QLabel('Количество участников:')
        self.participants_edit = QLineEdit()

        self.date_label = QLabel('Дата проведения:')
        self.date_edit = QDateEdit()

        self.participants_form_label = QLabel('Участники:')
        self.participants_form_edit = QTextEdit()

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.saveData)

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_edit)
        vbox.addWidget(self.sport_label)
        vbox.addWidget(self.sport_edit)
        vbox.addWidget(self.format_label)
        vbox.addWidget(self.format_edit)
        vbox.addWidget(self.participants_label)
        vbox.addWidget(self.participants_edit)
        vbox.addWidget(self.date_label)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.participants_form_label)
        vbox.addWidget(self.participants_form_edit)
        vbox.addWidget(self.save_button)

        self.setLayout(vbox)

    def saveData(self): # Нужно как-то вернуть эти данные
        self.name = self.name_edit.text()
        self.sport = self.sport_edit.text()
        self.format = self.format_edit.currentIndex()
        self.participants = self.participants_edit.text()
        self.date = self.date_edit.text()
        self.participants_form = self.participants_form_edit.toPlainText()
        self.data.emit(self._index, self.name, self.sport, self.format, self.participants, self.date.toPyDate(), self.participants_form)
        self.close()




