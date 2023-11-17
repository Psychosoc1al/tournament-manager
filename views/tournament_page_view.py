from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QColor, QPainter, QWheelEvent
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QGraphicsScene, QGraphicsView, QGraphicsLineItem


class TournamentPageView(QWidget):
    _scene_height = 400
    _round_width = 300
    _round_height = 900
    _round_x = 20
    _round_y = _scene_height / 2 - _round_height / 2

    def __init__(self, parent: QWidget, depth: int):
        super().__init__(parent)

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        self.back_button = QPushButton('Back to main menu', self)
        main_layout.addWidget(self.back_button)

        graphics_view = GraphicsView(self)
        graphics_view.installEventFilter(self)
        main_layout.addWidget(graphics_view)

        graphics_view.create_bracket(self._round_x, self._round_y, self._round_width, self._round_height, depth)

        self.show()


class GraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pen = QPen(QColor(175, 177, 179), 2)
        self._scene = QGraphicsScene(self)

        self.setRenderHints(self.renderHints() | QPainter.RenderHint.Antialiasing)
        self.setScene(self._scene)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            scaleFactor = 1.15

            if event.angleDelta().y() > 0:
                self.scale(scaleFactor, scaleFactor)
            elif event.angleDelta().y() < 0:
                self.scale(1.0 / scaleFactor, 1.0 / scaleFactor)

        elif event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + event.angleDelta().y())

        else:
            super().wheelEvent(event)

    def create_bracket(self, round_x, round_y, round_width, round_height, stage):
        if stage == 0:
            return

        top = round_y + round_height / 4
        bottom = round_y + round_height / 4 * 3

        vertical_line = QGraphicsLineItem(
            round_x,
            top,
            round_x,
            bottom
        )
        vertical_line.setPen(self._pen)
        self._scene.addItem(vertical_line)

        horizontal_line_right = QGraphicsLineItem(
            round_x,
            (top + bottom) / 2,
            round_x + round_width / 2,
            (top + bottom) / 2
        )
        horizontal_line_right.setPen(self._pen)
        self._scene.addItem(horizontal_line_right)

        self.create_bracket(
            round_x - round_width / 2,
            round_y,
            round_width,
            round_height / 2,
            stage - 1
        )
        self.create_bracket(
            round_x - round_width / 2,
            round_y + round_height / 2,
            round_width,
            round_height / 2,
            stage - 1
        )
