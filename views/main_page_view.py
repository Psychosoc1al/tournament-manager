import qdarktheme  # install as pyqtdarktheme
from PyQt6.QtWidgets import (
    QMainWindow,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QStackedWidget,
    QApplication,
    QListWidgetItem,
    QHBoxLayout,
)

from model.tournament import Tournament


class MainPageView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Главное меню")
        self.setMinimumSize(800, 600)

        self.central_stacked_widget = QStackedWidget()
        self.setCentralWidget(self.central_stacked_widget)

        self._create_main_menu_widget()

        qdarktheme.setup_theme(custom_colors={"primary": "#d79df1"})
        self.show()

    def _create_main_menu_widget(self) -> None:
        main_widget = QWidget(self.central_stacked_widget)
        main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(main_layout)

        self.add_tournament_button = QPushButton("Добавить турнир", main_widget)
        main_layout.addWidget(self.add_tournament_button)

        self.tournaments_list_widget = QListWidget(main_widget)
        main_layout.addWidget(self.tournaments_list_widget)

        self.central_stacked_widget.addWidget(main_widget)

    def show_tournaments(
        self, tournaments: list[Tournament]
    ) -> dict[str, list[QPushButton]]:
        buttons = {"tournament": [], "update": [], "remove": []}

        for index, tournament in enumerate(tournaments):
            list_item = QListWidgetItem(self.tournaments_list_widget)
            item_inner_widget = QWidget(self.tournaments_list_widget)
            item_inner_layout = QHBoxLayout(item_inner_widget)

            # optimised
            tournament_button = QPushButton(
                tournament if isinstance(tournament, str) else tournament.name,
                item_inner_widget,
            )
            tournament_button.setStyleSheet(
                "padding: 5px 0px 5px 0px; margin: 3px 0px 3px 0px;"
            )
            buttons["tournament"].append(tournament_button)

            update_button = QPushButton("Редактировать", item_inner_widget)
            update_button.setStyleSheet("padding: 5px 10px 5px 10px;")
            buttons["update"].append(update_button)

            remove_button = QPushButton("Удалить", item_inner_widget)
            remove_button.setStyleSheet("padding: 5px 10px 5px 10px;")
            buttons["remove"].append(remove_button)

            item_inner_layout.addWidget(tournament_button, stretch=1)
            item_inner_layout.addWidget(update_button)
            item_inner_layout.addWidget(remove_button)
            item_inner_layout.setContentsMargins(0, 0, 0, 0)

            item_inner_widget.setLayout(item_inner_layout)
            list_item.setSizeHint(item_inner_widget.sizeHint())
            self.tournaments_list_widget.setItemWidget(list_item, item_inner_widget)

        return buttons

    def resize_screen_percent_and_center(
        self, width_percent: float, height_percent: float
    ) -> None:
        if self.isMaximized():
            return

        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_width, screen_height = screen_geometry.width(), screen_geometry.height()
        self.resize(
            int(width_percent * screen_width), int(height_percent * screen_height)
        )

        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)

        self.move(window_geometry.topLeft())
