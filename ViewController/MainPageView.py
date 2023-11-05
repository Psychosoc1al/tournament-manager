from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QListWidgetItem, QHBoxLayout, \
    QInputDialog

from ViewController.AddEditPageView import AddEditPageView
from ViewController.TournamentPageView import TournamentPageView


class MainPageView(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self.setWindowTitle("Главное меню")
        # self._tournamentWindow = TournamentPageView()
        # self._addWindow = AddEditPageView()
        self.setFixedSize(QSize(800, 600))

        self.list_widget = QListWidget()
        add_button = QPushButton("Add")
        add_button.setCheckable(True)
        add_button.clicked.connect(self.add_tournament)

        main_layout = QVBoxLayout()
        main_layout.addWidget(add_button)
        main_layout.addWidget(self.list_widget)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.update_view()

    def update_view(self):  # обновляет список турниров
        self.list_widget.clear()  # Это список турниров
        tournaments = self._model.get_tournaments()
        ind = 0
        for tournament in tournaments:
            item = QListWidgetItem(self.list_widget)
            widget = QWidget()
            layout = QHBoxLayout(widget)

            tournament_button = QPushButton(tournament)
            tournament_button.clicked.connect(lambda _, t=tournament: self.go_to_tournament(t))
            remove_button = QPushButton("Delete")
            remove_button.clicked.connect(lambda _, t=tournament: self.remove_tournament(t))
            update_button = QPushButton("Update")
            update_button.clicked.connect(lambda _, t=ind: self.update_tournament(t))

            layout.addWidget(tournament_button)
            layout.addWidget(update_button)
            layout.addWidget(remove_button)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            self.list_widget.setItemWidget(item, widget)
            ind += 1

    def add_tournament(self):
        # Тут должен создаться турнир
        tournament, ok = QInputDialog.getText(self, "Добавить турнир", "Введите название турнира:")
        if ok:
            self._model.add_tournament(tournament)
            self.update_view()

    def remove_tournament(self, tournament):
        self._model.delete_tournament(tournament)
        self.update_view()

    def update_tournament(self, index):
        new_tournament, ok = QInputDialog.getText(self, "Обновить турнир", "Введите новое название турнира:")
        if ok:
            self._model.update_tournament(index, new_tournament)
            self.update_view()

    def go_to_tournament(self, tournament):
        # Тут открывается окно турнира
        self.window = TournamentPageView(tournament)
        self.hide()
        self.window.show()

