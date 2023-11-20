from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QDoubleSpinBox, \
    QPushButton

from model.match import Match


class MatchResultPageView(QDialog):
    def __init__(self, parent: QMainWindow, match: Match) -> None:
        super().__init__(parent)
        self.setMinimumSize(320, 150)
        self.setWindowTitle('Match result')
        self.setModal(True)

        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        first_widget = QWidget(self)
        first_layout = QHBoxLayout(first_widget)
        first_label = QLabel(match.participant1.name + ' score:', first_widget)
        first_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.first_score = QDoubleSpinBox(first_widget)
        self.first_score.setValue(match.score_participant1)
        self.first_score.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.first_score.setMaximumWidth(100)
        self.first_score.setDecimals(0)
        self.first_score.setRange(0, 999)

        first_layout.addWidget(first_label)
        first_layout.addWidget(self.first_score)
        first_widget.setLayout(first_layout)

        second_widget = QWidget(self)
        second_layout = QHBoxLayout(second_widget)
        second_label = QLabel(match.participant2.name + ' score:', second_widget)
        second_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.second_score = QDoubleSpinBox(second_widget)
        self.second_score.setValue(match.score_participant2)
        self.second_score.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.second_score.setMaximumWidth(100)
        self.second_score.setDecimals(0)
        self.second_score.setRange(0, 999)

        second_layout.addWidget(second_label)
        second_layout.addWidget(self.second_score)
        second_widget.setLayout(second_layout)

        main_layout.addWidget(first_widget)
        vs_label = QLabel('VS', self)
        vs_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(vs_label)
        main_layout.addWidget(second_widget)

        self.save_button = QPushButton('Save')
        main_layout.addWidget(self.save_button)

        self.show()
