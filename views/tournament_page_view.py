from PyQt6.QtCore import Qt, QRectF, pyqtSignal
from PyQt6.QtGui import QPen, QColor, QPainter, QBrush, QWheelEvent
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QPushButton,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsLineItem,
    QHBoxLayout,
    QGraphicsTextItem,
    QGraphicsObject,
)

from model.match import Match


class TournamentPageView(QWidget):
    _scene_height = 900
    _round_width = 500
    _round_height = _scene_height
    _round_x = 0
    _round_y = -_scene_height / 2

    def __init__(
        self, stages_amount: int, matches: list[list[Match]], parent: QWidget = None
    ) -> None:
        super().__init__(parent)
        self._stages_amount = stages_amount

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        self.back_button = QPushButton("В главное меню", self)
        main_layout.addWidget(self.back_button)

        self._info_widget = QWidget(self)
        self._create_info_widget()
        main_layout.addWidget(self._info_widget)

        self.graphics_view = GraphicsView(self, stages_amount, matches)
        self.graphics_view.installEventFilter(self)
        main_layout.addWidget(self.graphics_view)

        self.graphics_view.create_bracket(
            self._round_x,
            self._round_y,
            self._round_width,
            self._round_height,
            stages_amount,
            0,
        )

        self.show()

    def redraw(self) -> None:
        self.graphics_view.scene().clear()

        self.graphics_view.create_bracket(
            self._round_x,
            self._round_y,
            self._round_width,
            self._round_height,
            self._stages_amount,
            0,
        )

    def _create_info_widget(self) -> None:
        info_layout = QHBoxLayout(self._info_widget)
        info_layout.setContentsMargins(0, 0, 0, 0)
        self._info_widget.setLayout(info_layout)

        self._name_label = InfoButton(self._info_widget)
        info_layout.addWidget(self._name_label)

        self._sport_label = InfoButton(self._info_widget)
        info_layout.addWidget(self._sport_label)

        self._date_label = InfoButton(self._info_widget)
        info_layout.addWidget(self._date_label)

        self._participants_amount_label = InfoButton(self._info_widget)
        info_layout.addWidget(self._participants_amount_label)

    def set_info_data(
        self, name: str, sport: str, date: str, participants_amount: str
    ) -> None:
        self._name_label.setText("Название: " + name)
        self._sport_label.setText("Вид спорта: " + sport)
        self._date_label.setText("Дата проведения: " + date)
        self._participants_amount_label.setText("Участники: " + participants_amount)


class GraphicsView(QGraphicsView):
    def __init__(
        self, parent: QWidget, stages_amount: int, matches: list[list[Match]]
    ) -> None:
        super().__init__(parent)
        self._initial_stages_amount = stages_amount
        self._matches = matches
        self._is_final = False

        self._pen = QPen(QColor(175, 177, 179), 2)
        self._scene = QGraphicsScene(self)
        self._general_stages_left = stages_amount

        self.setRenderHints(self.renderHints() | QPainter.RenderHint.Antialiasing)
        self.setScene(self._scene)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            scaleFactor = 1.15

            if event.angleDelta().y() > 0:
                self.scale(scaleFactor, scaleFactor)
            elif event.angleDelta().y() < 0:
                self.scale(1.0 / scaleFactor, 1.0 / scaleFactor)

        elif event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() + event.angleDelta().y()
            )

        else:
            super().wheelEvent(event)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            position = self.mapToScene(event.pos())
            for item in self.items():
                if isinstance(item, RectangleObject) and item.contains(position):
                    item.handle_click()

    def create_bracket(
        self,
        round_x: float,
        round_y: float,
        round_width: float,
        round_height: float,
        stages_left: int,
        branch_index: int,
    ) -> None:
        top = round_y + round_height / 4
        bottom = round_y + round_height / 4 * 3

        if stages_left == 0:
            horizontal_line = QGraphicsLineItem(
                round_x,
                (top + bottom) / 2,
                round_x + round_width / 2,
                (top + bottom) / 2,
            )
            horizontal_line.setPen(self._pen)
            self._scene.addItem(horizontal_line)

            self._print_name_and_score(
                round_x,
                (top + bottom) / 2,
                round_width,
                stages_left,
                branch_index,
                round_height,
            )

            self._general_stages_left -= 1
            if self._general_stages_left:
                return

            self._scale_view(round_width)
            return

        vertical_line = QGraphicsLineItem(round_x, top, round_x, bottom)
        vertical_line.setPen(self._pen)
        self._scene.addItem(vertical_line)

        horizontal_line = QGraphicsLineItem(
            round_x, (top + bottom) / 2, round_x + round_width / 2, (top + bottom) / 2
        )
        horizontal_line.setPen(self._pen)
        self._scene.addItem(horizontal_line)

        if stages_left != self._initial_stages_amount:
            self._print_name_and_score(
                round_x,
                (top + bottom) / 2,
                round_width,
                stages_left,
                branch_index,
                round_height,
            )

        self.create_bracket(
            round_x - round_width / 2,
            round_y,
            round_width,
            round_height / 2,
            stages_left - 1,
            branch_index * 2,
        )
        self.create_bracket(
            round_x - round_width / 2,
            round_y + round_height / 2,
            round_width,
            round_height / 2,
            stages_left - 1,
            branch_index * 2 + 1,
        )

    def _print_name_and_score(
        self,
        round_x: float,
        round_y: float,
        round_width: float,
        stages_left: int,
        branch_index: int,
        round_height: float = 0,
    ) -> None:
        match = self._matches[stages_left][branch_index // 2]
        if match.participant1.name == "???" and match.participant2.name == "???":
            return

        if branch_index % 2 == 0:
            name = QGraphicsTextItem(match.participant1.name)
            score = QGraphicsTextItem(str(match.score_participant1))
        else:
            name = QGraphicsTextItem(match.participant2.name)
            score = QGraphicsTextItem(str(match.score_participant2))

        name.setScale(1.75)
        score.setScale(2)
        name.setPos(round_x, round_y - 40)
        score.setPos(
            round_x + round_width / 2 - 25 - score.boundingRect().width(), round_y - 45
        )

        self._scene.addItem(name)
        self._scene.addItem(score)

        if (
            match.participant1.name != "???"
            and match.participant2.name != "???"
            and branch_index % 2 == 1
        ):
            # if not (match.score_participant1 > 0 or match.score_participant2 > 0):
            background_rect = RectangleObject(
                round_x,
                round_y,
                round_width / 2,
                -(round_height + 40),
                stages_left,
                branch_index // 2,
            )
            self._scene.addItem(background_rect)

            if self._initial_stages_amount - stages_left == 1 and (
                match.score_participant1 > 0 or match.score_participant2 > 0
            ):
                self._print_winner(round_width)

    def _print_winner(self, round_width: float) -> None:
        match = self._matches[-1][0]
        winner = (
            match.participant1
            if match.score_participant1 > match.score_participant2
            else match.participant2
        )

        name = QGraphicsTextItem(winner.name)
        name.setPos(round_width / 2, -25)
        name.setScale(1.75)

        self._scene.addItem(name)

    def _scale_view(self, round_width: float) -> None:
        x_center = -(self._initial_stages_amount - 1) / 2 * round_width / 2

        horizontal_aligning_line = QGraphicsLineItem(
            x_center - self._scene.width() * 3 / 4,
            0,
            x_center + self._scene.width() * 3 / 4,
            0,
        )
        horizontal_aligning_line.setOpacity(0)
        self._scene.addItem(horizontal_aligning_line)

        vertical_aligning_line = QGraphicsLineItem(
            x_center,
            -self._scene.height() * 3 / 4,
            x_center,
            self._scene.height() * 3 / 4,
        )
        vertical_aligning_line.setOpacity(0)
        self._scene.addItem(vertical_aligning_line)

        self.scale(
            1 / (self._initial_stages_amount * 1.5),
            1 / (self._initial_stages_amount * 1.5),
        )
        self.scale(self._initial_stages_amount, self._initial_stages_amount)


class RectangleObject(QGraphicsObject):
    clicked_signal = pyqtSignal(int, int)

    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        stage: int,
        match_number: int,
    ):
        super().__init__()
        self._x = int(x)
        self._y = int(y)
        self._width = int(width)
        self._height = int(height)

        self._stage = stage
        self._match_number = match_number

        self.setOpacity(0.2)

    def paint(self, painter, options, widget=None):
        painter.setBrush(QBrush(QColor(100, 100, 100)))
        painter.drawRect(self._x, self._y, self._width, self._height)

    def boundingRect(self):
        return QRectF(self._x, self._y, self._width, self._height)

    def handle_click(self):
        self.clicked_signal.emit(self._stage, self._match_number)


class InfoButton(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self._is_enabled = True
        self.setDown(True)
        self.setStyleSheet("font-size: 14px")

    def event(self, event):
        self.setDown(True)
        return super().event(event)
