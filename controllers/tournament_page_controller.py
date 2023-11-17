from tournament import Tournament
from tournament_page_view import TournamentPageView


class TournamentPageController:
    def __init__(self, model: Tournament, view: TournamentPageView, main_controller):
        self._model = model
        self._view = view
        self._main_controller = main_controller

        self._view.back_button.clicked.connect(self._main_controller.show_main_page)
