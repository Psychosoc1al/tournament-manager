from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QDialog, QGraphicsRectItem

from model.match import Match
from views.match_result_page_view import MatchResultPageView


class MatchResultPageController(QObject):
    match_result_submitted = pyqtSignal(int, int)

    def __init__(self, view: MatchResultPageView, match: Match) -> None:
        super().__init__()
        self._view = view

        self._view.show()
