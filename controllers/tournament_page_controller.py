from tournament import Tournament
from tournament_page_view import TournamentPageView


class TournamentPageController:
    def __init__(self, model: Tournament, view: TournamentPageView, main_controller) -> None:
        self._model = model
        self._view = view
        self._main_controller = main_controller

        self._view.back_button.clicked.connect(self._main_controller.show_main_page)

        self._view.set_info_data(
            self._model.name,
            self._model.sport,
            self._model.tour_date.strftime('%d.%m.%Y'),
            str(len(self._model.participants))
        )
