from PyQt6.QtWidgets import QMainWindow, QListWidget

from ViewController.AddEditPageView import AddEditPageView
from ViewController.TournamentPageView import TournamentPageView


class MainPageView(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._tournamentWindow = TournamentPageView()
        self._addWindow = AddEditPageView()

        self.list_widget = QListWidget()
        # Тут долны создаться элементы и к ним должны привязаться обработчики(методы ниже)

        self.update_view()

    def update_view(self):  # обновляет список турниров
        self.list_widget.clear()  # Это список турниров
        tournaments = self._model.tournaments()
        for tournament in tournaments:
            self.list_widget.addItem(tournament)

    def add_tournament(self):
        # Тут должен создаться турнир
        self._addWindow.show()
        tournament = "New Tournament"
        self._model.add_tournament(tournament)
        self.update_view()

    def remove_tournament(self):
        # Тут как-то нужно получить индекс турнира
        tournament = "Deleted Tournament"
        self._model.remove_tournament(tournament)
        self.update_view()

    def update_tournament(self):
        # Тут как-то получаем индекс удаляемого турнира и вызываем нужный контроллер
        tournament = "Old Tournament"
        new_tournament = "Updated Tournament"
        self._model.update_tournament(tournament, new_tournament)
        self.update_view()

    def go_to_tournament(self):
        # Тут открывается окно турнира
        pass
