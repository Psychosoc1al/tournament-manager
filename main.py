from unittest.mock import Mock, MagicMock

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget
from win32comext.shell.shell import (
    SetCurrentProcessExplicitAppUserModelID,
)  # install as pywin32

from add_edit_page_view import AddEditPageView
from controllers.main_controller import MainController
from match import Match
from match_result_page_view import MatchResultPageView
from model.main_page import MainPage
from tournament_page_view import TournamentPageView, GraphicsView
from views.main_page_view import MainPageView


def main():
    # app = QApplication([])
    # myappid = "tornament.manager"
    # SetCurrentProcessExplicitAppUserModelID(myappid)
    # app.setWindowIcon(QIcon("icon/icon.png"))
    #
    # model = MainPage()
    # window = MainPageView()
    # MainController(model, window)
    #
    # app.exec()
    app = QApplication([])
    myappid = "tornament.manager"
    SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QIcon("icon/icon.png"))

    # model = MainPage()
    # parent = QWidget()
    match = Mock(spec=Match)
    match.participant1.name = "Participant 1"
    match.participant2.name = "Participant 2"
    match.score_participant1 = 4
    match.score_participant2 = 3
    window = TournamentPageView(2, [[match, match], [match, match]])
    # name = "Tournament 1"
    # sport = "Football"
    # date = "2023-01-01"
    # participants_amount = "4"


    # match = Mock(spec=Match)
    # match.participant1.name = "Participant 1"
    # match.participant2.name = "Participant 2"
    # match.score_participant1 = 4
    # match.score_participant2 = 3
    # graphics_view = GraphicsView( 2, [[match, match], [match, match]])
    # graphics_view.show()




    # MainController(model, window)

    app.exec()


if __name__ == "__main__":
    main()
