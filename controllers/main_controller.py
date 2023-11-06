from PyQt6.QtWidgets import QListWidgetItem, QWidget, QHBoxLayout, QPushButton, QStackedWidget

from AddEditPageView import AddEditPageView
from MainPage import MainPage
from MainPageView import MainPageView
from Tournament import Tournament
from TournamentPageView import TournamentPageView
from add_edit_page_controller import AddEditPageController
from tournament_page_controller import TournamentPageController

from datetime import date


class MainController:
    def __init__(self, model: MainPage, view: MainPageView):
        self._model = model
        self._view = view

        self.show_main_page()

    def show_main_page(self):
        self._view.add_tournament_button.clicked.connect(self._add_tournament)

        self._view.tournaments_list_widget.clear()
        tournaments = self._model.get_tournaments()

        for index, tournament in enumerate(tournaments):
            list_item = QListWidgetItem(self._view.tournaments_list_widget)
            item_inner_widget = QWidget()
            item_inner_layout = QHBoxLayout(item_inner_widget)

            tournament_button = QPushButton(tournament, item_inner_widget)
            tournament_button.setStyleSheet('padding: 5px 0px 5px 0px; margin: 3px 0px 3px 0px;')
            tournament_button.clicked.connect(lambda _, i=index: self.go_to_tournament(i))

            update_button = QPushButton('Edit', item_inner_widget)
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

        self._view.central_stacked_widget.setCurrentIndex(0)
        self._view.setWindowTitle('Main menu')
        self._view.show()

    def _add_tournament(self):
        self.add_tournament_window = AddEditPageView('add')
        _ = AddEditPageController(self.add_tournament_window, 'add', self)

        self.add_tournament_window.form_submitted.connect(self.add_data)
        # tournament, ok = QInputDialog.getText(self, 'Добавить турнир', 'Введите название турнира:')
        # if ok:
        #     self._model.add_tournament(tournament)
        #     self.update_view()

    def update_tournament(self, index):
        update_window = AddEditPageView(index)
        update_window.show()
        update_window.data[int, str, str, int, int, str, str].connect(self.update_data)
        # new_tournament, ok = QInputDialog.getText(self, 'Обновить турнир', 'Введите новое название турнира:')
        # if ok:
        #     self._model.update_tournament(index, new_tournament)
        #     self.update_view()

    def remove_tournament(self, tournament):
        self._model.delete_tournament(tournament)
        # TODO: add logic
        self.show_main_page()

    def go_to_tournament(self, tournament_index: int):
        tournaments = self._model.get_tournaments()
        tournament_view = TournamentPageView(self._view.central_stacked_widget)
        _ = TournamentPageController(tournaments[tournament_index], tournament_view, self)

        self._view.central_stacked_widget.addWidget(tournament_view)
        self._view.central_stacked_widget.setCurrentWidget(tournament_view)
        self._view.setWindowTitle(tournaments[tournament_index] + ' - bracket')

    def add_data(self, name: str, sport: str, d_format: int, participants_amount: int, start_date: date, participants: str):
        print('Название:', name)
        print('Вид спорта:', sport)
        print('Формат проведения:', d_format)
        print('Количество участников:', participants_amount)
        print('Дата проведения:', start_date)
        print('Участники:', participants)
        # new_tournament = Tournament(name, sport, start_date, participants, d_format)
        # self._model.add_tournament(new_tournament)
        self.show_main_page()

    def update_data(self, index, name, sport, d_format, participants, date, participants_form):
        print('Название:', name)
        print('Вид спорта:', sport)
        print('Формат проведения:', d_format)
        print('Количество участников:', participants)
        print('Дата проведения:', date)
        print('Участники:', participants_form)
        new_tournament = Tournament(name, sport, date, participants_form.split(','), d_format)
        self._model.update_tournament(index, new_tournament)
        self.show_main_page()

        # print('Название:', name)
        # print('Вид спорта:', sport)
        # print('Формат проведения:', d_format)
        # print('Количество участников:', participants)
        # print('Дата проведения:', date)
        # print('Участники:', participants_form)
