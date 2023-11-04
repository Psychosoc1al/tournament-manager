from AddEditPageController import AddEditPageController
from AddEditPageView import AddEditPageView
from Tournament import Tournament
from TournamentPageController import TournamentPageController
from TournamentPageView import TournamentPageView


class MainPageController:

    def __init__(self, main_page, view, manager):
        self._main_page = main_page
        self._view = view
        self._manager = manager

    def run(self):
        self._view.display_menu()

    def add_tournament(self):
        add_edit_page_view = AddEditPageView()
        add_edit_page_controller = AddEditPageController(add_edit_page_view)
        add_edit_page_controller.run()

    def update_tournament(self):
        add_edit_page_view = AddEditPageView()
        add_edit_page_controller = AddEditPageController(add_edit_page_view)
        add_edit_page_controller.run()

    def go_to_tournament(self):
        tournament_model = Tournament()
        tournament_view = TournamentPageView()
        add_edit_page_controller = TournamentPageController(tournament_model, tournament_view)
        add_edit_page_controller.run()