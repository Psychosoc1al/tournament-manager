class AddEditPageController:
    def __init__(self, view):
        self._view = view

    def run(self):
        self._view.display_menu()
