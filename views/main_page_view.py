import qdarktheme  # install as pyqtdarktheme
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QResizeEvent
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
    tournament_buttons_created_signal = pyqtSignal(int, object)

    def __init__(self) -> None:
        super().__init__()
        self._tournaments = []

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

        self.tournaments_list_widget = CustomListWidget(main_widget)
        self.tournaments_list_widget.show_item_signal.connect(self.show_tournaments)
        main_layout.addWidget(self.tournaments_list_widget)

        self.central_stacked_widget.addWidget(main_widget)

    def pre_show_tournaments(self, tournaments: list[Tournament]) -> None:
        self._tournaments = tournaments

        for _ in tournaments:
            self.tournaments_list_widget.add_empty_item()
        self.tournaments_list_widget.update_visible_items()

    def show_tournaments(self, index: int) -> None:
        inner_widget = CustomListInnerWidget(
            self._tournaments[index].name, self.tournaments_list_widget
        )

        self.tournaments_list_widget.add_buttons_if_not_yet(index, inner_widget)
        self.tournament_buttons_created_signal.emit(index, inner_widget)

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


class CustomListInnerWidget(QWidget):
    def __init__(self, tournament_name: str, parent: QWidget = None) -> None:
        super().__init__(parent)

        item_inner_layout = QHBoxLayout(self)

        self.tournament_button = QPushButton(tournament_name, self)
        self.tournament_button.setStyleSheet(
            "padding: 5px 0px 5px 0px; margin: 3px 0px 3px 0px;"
        )

        self.update_button = QPushButton("Редактировать", self)
        self.update_button.setStyleSheet("padding: 5px 10px 5px 10px;")

        self.remove_button = QPushButton("Удалить", self)
        self.remove_button.setStyleSheet("padding: 5px 10px 5px 10px;")

        item_inner_layout.addWidget(self.tournament_button, stretch=1)
        item_inner_layout.addWidget(self.update_button)
        item_inner_layout.addWidget(self.remove_button)
        item_inner_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(item_inner_layout)


class CustomListWidget(QListWidget):
    show_item_signal = pyqtSignal(int)

    def add_empty_item(self):
        list_item = QListWidgetItem(self)
        self.addItem(list_item)
        self.setItemWidget(list_item, None)

    def add_buttons_if_not_yet(
        self, index: int, item_inner_widget: CustomListInnerWidget
    ):
        list_item = self.item(index)
        if self.itemWidget(list_item) is None:
            list_item.setSizeHint(item_inner_widget.sizeHint())

            self.setItemWidget(list_item, item_inner_widget)

    def update_visible_items(self):
        for index in range(self.count()):
            list_item = self.item(index)
            list_shape = self.visualItemRect(list_item)

            if self.viewport().rect().intersects(list_shape):
                self.show_item_signal.emit(index)

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.update_visible_items()

    def scrollContentsBy(self, dx: int, dy: int):
        super().scrollContentsBy(dx, dy)
        self.update_visible_items()
