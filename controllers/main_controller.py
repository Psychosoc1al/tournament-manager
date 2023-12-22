import math
from datetime import date

from controllers.add_edit_page_controller import AddEditPageController
from controllers.tournament_page_controller import TournamentPageController
from model.main_page import MainPage
from model.participant import Participant
from model.tournament import Tournament
from views.add_edit_page_view import AddEditPageView
from views.main_page_view import MainPageView, CustomListInnerWidget
from views.tournament_page_view import TournamentPageView


class MainController:
    def __init__(self, model: MainPage, view: MainPageView) -> None:
        self._model = model
        self._view = view
        self.tournaments_to_show = []

        self._view.tournament_buttons_created_signal.connect(
            self._connect_tournament_buttons
        )

        self._view.add_tournament_button.clicked.connect(self._add_tournament_show)
        self.show_main_page()

    @property
    def view(self) -> MainPageView:
        return self._view

    @property
    def model(self) -> MainPage:
        return self._model

    def show_main_page(self) -> None:
        self._view.tournaments_list_widget.clear()
        self._view.pre_show_tournaments(self._model.get_tournaments())

        self._view.central_stacked_widget.setCurrentIndex(0)
        self._view.setWindowTitle("Главное меню")
        self._view.resize_screen_percent_and_center(1 / 2, 1 / 2)

    def _connect_tournament_buttons(
        self,
        tournament_index: int,
        item_inner_widget: CustomListInnerWidget,
    ) -> None:
        tournaments = self._model.get_tournaments()

        item_inner_widget.update_button.clicked.connect(  # pragma: no branch
            lambda _, ind=tournament_index: self._update_tournament_show(
                tournaments[ind]
            )
        )

        item_inner_widget.remove_button.clicked.connect(  # pragma: no branch
            lambda _, ind=tournament_index: self._remove_tournament(tournaments[ind])
        )

        item_inner_widget.tournament_button.clicked.connect(  # pragma: no branch
            lambda _, ind=tournament_index: self._go_to_tournament(tournaments[ind])
        )

    def _add_tournament_show(self, _: bool = False) -> None:
        add_tournament_window = AddEditPageView(self._view)
        add_tournament_controller = AddEditPageController(add_tournament_window, "add")

        add_tournament_controller.form_submitted.connect(self._add_tournament)

    def _update_tournament_show(self, tournament: Tournament) -> None:
        update_tournament_window = AddEditPageView(self._view)
        update_tournament_controller = AddEditPageController(
            update_tournament_window, "edit", tournament
        )
        self._updating_tournament = tournament

        update_tournament_controller.form_submitted.connect(self._update_tournament)

    def _remove_tournament(self, tournament: Tournament) -> None:
        self._model.delete_tournament(tournament)
        self.show_main_page()

    def _go_to_tournament(self, tournament: Tournament) -> None:
        tournament_view = TournamentPageView(
            int(math.log2(len(tournament.participants))),
            tournament.brackets[0].matches,
            self._view.central_stacked_widget,
        )
        TournamentPageController(tournament, tournament_view, self)

        self._view.resize_screen_percent_and_center(3 / 4, 5 / 6)
        self._view.central_stacked_widget.addWidget(tournament_view)
        self._view.central_stacked_widget.setCurrentWidget(tournament_view)
        self._view.setWindowTitle("Сетка турнира " + tournament.name)

    def _add_tournament(
        self,
        name: str,
        sport: str,
        tournament_type: str,
        start_date: date,
        participants_string: str,
    ) -> None:
        participants = [Participant(name) for name in participants_string.split("\n")]
        new_tournament = Tournament(
            name, sport, tournament_type, start_date, participants
        )
        self._model.add_tournament(new_tournament)

        self.show_main_page()

    def _update_tournament(
        self, name: str, sport: str, _: str, start_date: date, __: str
    ) -> None:
        self._model.update_tournament(
            self._updating_tournament, name, sport, start_date
        )

        self.show_main_page()
