from match_result_page_controller import MatchResultPageController
from match_result_page_view import MatchResultPageView
from model.tournament import Tournament
from views.tournament_page_view import TournamentPageView, RectangleObject


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

        match_result_areas = [item for item in self._view.graphics_view.scene().items()
                              if isinstance(item, RectangleObject)]
        for area in match_result_areas:
            area.clicked_signal.connect(lambda x, y: self._show_match_result_page(x, y))

    def _show_match_result_page(self, match_stage: int, match_number: int) -> None:
        try:
            match = self._model.brackets[0].matches[match_stage][match_number]
            match_result_window = MatchResultPageView(
                self._main_controller.view,
                match
            )
            MatchResultPageController(match_result_window, match)
        except Exception as e:
            print(e)
