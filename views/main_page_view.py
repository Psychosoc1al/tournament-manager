import qdarktheme  # install as pyqtdarktheme
from PyQt6.QtWidgets import QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QApplication

from views.tournament_page_view import TournamentPageView


class MainPageView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main menu')
        self.setMinimumSize(800, 600)

        self.central_stacked_widget = QStackedWidget()
        self.setCentralWidget(self.central_stacked_widget)

        self._create_main_menu_widget()

        qdarktheme.setup_theme(custom_colors={'primary': '#d79df1'})

    def _create_main_menu_widget(self):
        main_widget = QWidget(self.central_stacked_widget)
        main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(main_layout)

        self.add_tournament_button = QPushButton('Add tournament', main_widget)
        main_layout.addWidget(self.add_tournament_button)

        self.tournaments_list_widget = QListWidget(main_widget)
        main_layout.addWidget(self.tournaments_list_widget)

        self.central_stacked_widget.addWidget(main_widget)

    def resize_and_center(self, width, height):
        self.resize(width, height)

        window_geometry = self.frameGeometry()
        center_point = QApplication.primaryScreen().availableGeometry().center()
        window_geometry.moveCenter(center_point)

        self.move(window_geometry.topLeft())
