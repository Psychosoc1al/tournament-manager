from PyQt6.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QPushButton, QStackedWidget

from AddEditPageView import AddPageView, UpdatePageView
from MainPage import MainPage
from MainPageView import MainPageView
from Tournament import Tournament
from TournamentPageView import TournamentPageView


PAGE_INDEX_BY_NAME = {
    'main': 0,
    'view': 1
}


class MainController:
    def __init__(self, model: MainPage, view: MainPageView):
        self._model = model
        self._view = view

        self.set_tournaments()

    def set_tournaments(self):
        self._view.tournaments_list_widget.clear()  # Это список турниров
        tournaments = self._model.get_tournaments()

        for index, tournament in enumerate(tournaments):
            list_item = QListWidgetItem(self._view.tournaments_list_widget)
            item_inner_widget = QWidget()
            item_inner_layout = QHBoxLayout(item_inner_widget)

            tournament_button = QPushButton(tournament, item_inner_widget)
            tournament_button.setStyleSheet('padding: 5px 0px 5px 0px; margin: 3px 0px 3px 0px;')
            tournament_button.clicked.connect(lambda _, t=tournament: self.go_to_tournament(t))

            update_button = QPushButton('Update', item_inner_widget)
            update_button.setStyleSheet('padding: 5px 10px 5px 10px;')
            update_button.clicked.connect(lambda _, i=index: self.update_tournament(i))

            remove_button = QPushButton('Delete', item_inner_widget)
            remove_button.setStyleSheet('padding: 5px 10px 5px 10px;')
            remove_button.clicked.connect(lambda _, t=tournament: self.remove_tournament(t))

            item_inner_layout.addWidget(tournament_button, stretch=1)
            item_inner_layout.addWidget(update_button)
            item_inner_layout.addWidget(remove_button)
            item_inner_layout.setContentsMargins(0, 0, 0, 0)

            item_inner_widget.setLayout(item_inner_layout)
            list_item.setSizeHint(item_inner_widget.sizeHint())
            self._view.tournaments_list_widget.setItemWidget(list_item, item_inner_widget)

    def add_tournament(self):
        add_window = AddPageView()
        add_window.show()
        add_window.data[str, str, int, int, str, str].connect(self.add_data)
        # tournament, ok = QInputDialog.getText(self, 'Добавить турнир', 'Введите название турнира:')
        # if ok:
        #     self._model.add_tournament(tournament)
        #     self.update_view()

    def remove_tournament(self, tournament):
        self._model.delete_tournament(tournament)
        # TODO: add logic
        self.set_tournaments()

    def update_tournament(self, index):
        self.update_window = UpdatePageView(index)
        self.update_window.show()
        self.update_window.data[int, str, str, int, int, str, str].connect(self.update_data)
        # new_tournament, ok = QInputDialog.getText(self, 'Обновить турнир', 'Введите новое название турнира:')
        # if ok:
        #     self._model.update_tournament(index, new_tournament)
        #     self.update_view()

    def go_to_tournament(self, tournament):
        # Тут открывается окно турнира
        self._view.central_stacked_widget.setCurrentIndex(PAGE_INDEX_BY_NAME['view'])

    def add_data(self, name, sport, d_format, participants, date, participants_form):
        new_tournament = Tournament(name, sport, date, participants_form.split(','), d_format)
        self._model.add_tournament(new_tournament)
        self.set_tournaments()

    def update_data(self, index, name, sport, d_format, participants, date, participants_form):
        print('Название:', name)
        print('Вид спорта:', sport)
        print('Формат проведения:', d_format)
        print('Количество участников:', participants)
        print('Дата проведения:', date)
        print('Участники:', participants_form)
        new_tournament = Tournament(name, sport, date, participants_form.split(','), d_format)
        self._model.update_tournament(index, new_tournament)
        self.set_tournaments()

        # print('Название:', name)
        # print('Вид спорта:', sport)
        # print('Формат проведения:', d_format)
        # print('Количество участников:', participants)
        # print('Дата проведения:', date)
        # print('Участники:', participants_form)
