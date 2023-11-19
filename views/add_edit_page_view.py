from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QListWidget, QDialog, \
    QMainWindow


class AddEditPageView(QDialog):
    def __init__(self, parent: QMainWindow) -> None:
        super().__init__(parent)
        self.setMinimumSize(450, 500)

        self._create_add_edit_form()
        self.show()

    def _create_add_edit_form(self) -> None:
        name_label = QLabel('Tournament name:')
        self.name_edit = QLineEdit()
        self.name_edit.setMaxLength(20)

        sport_label = QLabel('Sport type:')
        self.sport_edit = QLineEdit()
        self.sport_edit.setMaxLength(20)

        date_label = QLabel('Date:')
        self.date_edit = QDateEdit()

        format_label = QLabel('Tournament type:')
        self.format_edit = QComboBox()
        # self.format_edit.addItems(['Single elimination', 'Double elimination'])
        self.format_edit.addItems(['Single elimination'])

        participants_label = QLabel('Participants amount:')
        self.participants_amount_choose = QComboBox()
        self.participants_amount_choose.addItems(['4', '8', '16', '32'])

        participants_form_label = QLabel('Participants:')
        self.participants_inputs_list = QListWidget()
        self.participants_inputs_list.setSpacing(1)

        self.save_button = QPushButton('Save')
        self.save_button.setDisabled(True)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(name_label)
        main_layout.addWidget(self.name_edit)
        main_layout.addWidget(sport_label)
        main_layout.addWidget(self.sport_edit)
        main_layout.addWidget(format_label)
        main_layout.addWidget(self.format_edit)
        main_layout.addWidget(participants_label)
        main_layout.addWidget(self.participants_amount_choose)
        main_layout.addWidget(date_label)
        main_layout.addWidget(self.date_edit)
        main_layout.addWidget(participants_form_label)
        main_layout.addWidget(self.participants_inputs_list, 1)
        main_layout.addWidget(self.save_button)

        self.setLayout(main_layout)
