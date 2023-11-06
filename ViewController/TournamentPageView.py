from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton


class TournamentPageView(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.back_button = QPushButton('Back')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.back_button)

        self.setLayout(main_layout)
        # TODO: add logic
