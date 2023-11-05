import math

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QGraphicsView, QGraphicsScene, \
    QTreeWidgetItem, QTreeWidget

from Model.Bracket import *
from Model.MainPage import MainPage
from Model.Participant import Participant


class TournamentPageView(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self.setWindowTitle("Турнир")
        self.setFixedSize(QSize(800, 600))

        back_button = QPushButton("Back")
        back_button.setCheckable(True)
        back_button.clicked.connect(self.got_to_main_page)

        main_layout = QVBoxLayout()
        main_layout.addWidget(back_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.generate_bracket()

    def generate_bracket(self):
        pass

    def got_to_main_page(self):
        from ViewController.MainPageView import MainPageView
        model = MainPage("data.json")
        self.window = MainPageView(model)
        self.hide()
        self.window.show()


