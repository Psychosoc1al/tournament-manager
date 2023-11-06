import math

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QGraphicsView, QGraphicsScene, \
    QTreeWidgetItem, QTreeWidget

from Model.Bracket import *
from Model.MainPage import MainPage
from Model.Participant import Participant


class TournamentPageView(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.back_button = QPushButton('Back')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.back_button)

        self.setLayout(main_layout)
        # TODO: add logic
