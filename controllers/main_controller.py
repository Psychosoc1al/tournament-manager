from PyQt6.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QPushButton, QStackedWidget

from AddEditPageView import AddPageView, UpdatePageView
from Tournament import Tournament
from TournamentPageView import TournamentPageView


PAGE_INDEX_BY_NAME = {
    'main': 0,
    'view': 1
}


class MainController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

        self.set_tournaments()

    def set_tournaments(self):
        self._view.tournaments_list_widget.clear()  # Это список турниров
        tournaments = self._model.get_tournaments()

        for index, tournament in enumerate(tournaments):
            item = QListWidgetItem(self._view.tournaments_list_widget)
            widget = QWidget()
            layout = QHBoxLayout(widget)

            tournament_button = QPushButton(tournament)
            tournament_button.setFixedSize(500, 24)
            tournament_button.clicked.connect(lambda _, t=tournament: self.go_to_tournament(t))
            remove_button = QPushButton("Delete")
            remove_button.clicked.connect(lambda _, t=tournament: self.remove_tournament(t))
            update_button = QPushButton("Update")
            update_button.clicked.connect(lambda _, i=index: self.update_tournament(i))

            layout.addWidget(tournament_button)
            layout.addWidget(update_button)
            layout.addWidget(remove_button)
            layout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            self._view.tournaments_list_widget.setItemWidget(item, widget)

    def add_tournament(self):
        self.add_window = AddPageView()
        self.add_window.show()
        self.add_window.data[str, str, int, int, str, str].connect(self.add_data)
        # tournament, ok = QInputDialog.getText(self, "Добавить турнир", "Введите название турнира:")
        # if ok:
        #     self._model.add_tournament(tournament)
        #     self.update_view()

    def remove_tournament(self, tournament):
        self._model.delete_tournament(tournament)
        self.update_view()

    def update_tournament(self, index):
        self.update_window = UpdatePageView(index)
        self.update_window.show()
        self.update_window.data[int, str, str, int, int, str, str].connect(self.update_data)
        # new_tournament, ok = QInputDialog.getText(self, "Обновить турнир", "Введите новое название турнира:")
        # if ok:
        #     self._model.update_tournament(index, new_tournament)
        #     self.update_view()

    def go_to_tournament(self, tournament):
        # Тут открывается окно турнира
        self.window = TournamentPageView(tournament)
        self.hide()
        self.window.show()

    def add_data(self, name, sport, d_format, participants, date, participants_form):
        new_tournament = Tournament(name, sport, date, participants_form.split(","), d_format)
        self._model.add_tournament(new_tournament)
        self.update_view()

        # print('Название:', name)
        # print('Вид спорта:', sport)
        # print('Формат проведения:', d_format)
        # print('Количество участников:', participants)
        # print('Дата проведения:', date)
        # print('Участники:', participants_form)

    def update_data(self, index, name, sport, d_format, participants, date, participants_form):
        new_tournament = Tournament(name, sport, date, participants_form.split(","), d_format)
        self._model.update_tournament(index, new_tournament)
        self.update_view()

        # print('Название:', name)
        # print('Вид спорта:', sport)
        # print('Формат проведения:', d_format)
        # print('Количество участников:', participants)
        # print('Дата проведения:', date)
        # print('Участники:', participants_form)
