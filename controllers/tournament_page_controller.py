from Tournament import Tournament
from TournamentPageView import TournamentPageView


class TournamentPageController:
    def __init__(self, model: Tournament, view: TournamentPageView, main_controller):
        self._model = model
        self._view = view
        self._main_controller = main_controller

        self._view.back_button.clicked.connect(main_controller.show_main_page)

    # TODO: add logic