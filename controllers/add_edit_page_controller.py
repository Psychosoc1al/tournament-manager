from AddEditPageView import AddEditPageView
from Tournament import Tournament
from TournamentPageView import TournamentPageView


class AddEditPageController:
    def __init__(self, model: Tournament, view: AddEditPageView, page_type: str, main_controller):
        self._model = model
        self._view = view
        self._page_type = page_type
        self._main_controller = main_controller

        if self._page_type == 'edit':
            self._set_edit_form()
            self._view.setWindowTitle('Edit tournament')
        else:
            self._view.setWindowTitle('Add tournament')

    def _set_edit_form(self):
        self._view.name_edit.setReadOnly(True)
        self._view.name_edit.setText(self._model.name)
        self._view.sport_edit.setText(self._model.sport)
        self._view.date_edit.setDate(self._model.date)
        self._view.format_edit.setCurrentIndex(0 if len(self._model.brackets) == 1 else 1)
        self._view.participants_amount_edit.setReadOnly(True)
        self._view.participants_amount_edit.setText(self._model.participants)
        self._view.participants_edit.setReadOnly(True)
        self._view.participants_edit.setText('\n'.join(self._model.participants))

    # def on_form_submit
