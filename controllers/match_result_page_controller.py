from PyQt6.QtCore import QObject, pyqtSignal

from views.match_result_page_view import MatchResultPageView


class MatchResultPageController(QObject):
    match_result_submitted = pyqtSignal(int, int)

    def __init__(self, view: MatchResultPageView) -> None:
        super().__init__()
        self._view = view

        self._view.save_button.clicked.connect(  # pragma: no branch
            lambda _: self.send_match_result()
        )
        self._view.first_score.valueChanged.connect(  # pragma: no branch
            lambda _: self._handle_score_entering()
        )
        self._view.second_score.valueChanged.connect(  # pragma: no branch
            lambda _: self._handle_score_entering()
        )

    def _handle_score_entering(self):
        if self._view.first_score.value() != self._view.second_score.value():
            self._view.save_button.setEnabled(True)
        else:
            self._view.save_button.setDisabled(True)

    def send_match_result(self) -> None:
        self.match_result_submitted.emit(
            int(self._view.first_score.value()), int(self._view.second_score.value())
        )

        self._view.close()
