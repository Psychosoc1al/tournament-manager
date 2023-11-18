import math
from datetime import date

from add_edit_page_controller import AddEditPageController
from add_edit_page_view import AddEditPageView
from main_page import MainPage
from main_page_view import MainPageView
from Participant import Participant
from Tournament import Tournament
from tournament_page_controller import TournamentPageController
from tournament_page_view import TournamentPageView


class MainController:
    def __init__(self, model: MainPage, view: MainPageView) -> None:
        self._model = model
        self._view = view

        self._view.add_tournament_button.clicked.connect(lambda _: self._add_tournament_show())
        self.show_main_page()

    def show_main_page(self) -> None:
        self._view.tournaments_list_widget.clear()
        tournaments = self._model.get_tournaments()
        buttons_to_connect = self._view.show_tournaments(tournaments)

        for button_type, buttons in buttons_to_connect.items():
            for index, button in enumerate(buttons):
                if button_type == 'update':
                    button.clicked.connect(lambda _, ind=index: self._update_tournament_show(tournaments[ind]))
                elif button_type == 'remove':
                    button.clicked.connect(lambda _, ind=index: self._remove_tournament(tournaments[ind]))
                else:
                    button.clicked.connect(lambda _, ind=index: self._go_to_tournament(tournaments[ind]))

        self._view.central_stacked_widget.setCurrentIndex(0)
        self._view.setWindowTitle('Main menu')
        self._view.resize_and_center(800, 600)

    def _add_tournament_show(self) -> None:
        add_tournament_window = AddEditPageView(self._view)
        AddEditPageController(add_tournament_window, 'add')

        add_tournament_window.form_submitted.connect(self._add_tournament)

        # TODO: connect with Model

    def _update_tournament_show(self, tournament: Tournament) -> None:
        update_tournament_window = AddEditPageView(self._view)
        AddEditPageController(update_tournament_window, 'edit', tournament)

        update_tournament_window.form_submitted.connect(self._update_tournament)

        # TODO: connect with Model

    def _remove_tournament(self, tournament: Tournament) -> None:
        self._model.delete_tournament(tournament)
        self.show_main_page()

    def _go_to_tournament(self, tournament: Tournament) -> None:
        tournament_view = TournamentPageView(
            self._view.central_stacked_widget,
            int(math.log2(len(tournament.participants)))
        )
        TournamentPageController(tournament, tournament_view, self)

        self._view.resize_and_center(1200, 900)
        self._view.central_stacked_widget.addWidget(tournament_view)
        self._view.central_stacked_widget.setCurrentWidget(tournament_view)
        self._view.setWindowTitle(tournament.name + ' - bracket')

    def _add_tournament(self,
                        name: str,
                        sport: str,
                        tournament_type: str,
                        start_date: date,
                        participants_string: str,
                        created_tournament: Tournament = None
                        ) -> None:
        
        if created_tournament:
            self._model.add_tournament(created_tournament)
        else:
            participants = [Participant(name) for name in participants_string.split('\n')]
            new_tournament = Tournament(name, sport, tournament_type, start_date, participants)
            self._model.add_tournament(new_tournament)

        self.show_main_page()

    def _update_tournament(self,
                           name: str,
                           sport: str,
                           tournament_type: str,
                           start_date: date,
                           participants_string: str
                           ) -> None:
        participants = [Participant(name) for name in participants_string.split('\n')]
        new_tournament = Tournament(name, sport, tournament_type, start_date, participants)
        self._remove_tournament(new_tournament)

        self._add_tournament(name, sport, tournament_type, start_date, participants_string, new_tournament)
