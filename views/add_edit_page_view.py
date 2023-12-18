from PyQt6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QDateEdit,
    QListWidget,
    QDialog,
    QMainWindow,
    QListWidgetItem,
)


class AddEditPageView(QDialog):
    def __init__(self, parent: QMainWindow = None) -> None:
        super().__init__(parent)
        self.setMinimumSize(450, 500)

        self._create_add_edit_form()
        self.show()

    def _create_add_edit_form(self) -> None:
        name_label = QLabel("Название:")
        self.name_edit = QLineEdit(self)

        sport_label = QLabel("Вид спорта:")
        self.sport_edit = QLineEdit(self)

        date_label = QLabel("Дата проведения:")
        self.date_edit = QDateEdit(self)

        format_label = QLabel("Тип турнира:")
        self.format_edit = QComboBox(self)
        # self.format_edit.addItems(['Single elimination', 'Double elimination'])
        self.format_edit.addItems(["Single elimination"])

        participants_label = QLabel("Количество участников:")
        self.participants_amount_choose = QComboBox(self)
        self.participants_amount_choose.addItems(["4", "8", "16"])

        participants_form_label = QLabel("Участники:")
        self.participants_inputs_list = QListWidget(self)
        self.participants_inputs_list.setSpacing(1)
        self.create_participants_form()

        self.save_button = QPushButton("Сохранить")
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

    def create_participants_form(self) -> list[QLineEdit]:
        participants_qlines = []

        self.participants_inputs_list.clear()
        current_amount = int(self.participants_amount_choose.currentText())

        for i in range(current_amount):
            list_item = QListWidgetItem(self.participants_inputs_list)

            new_line = QLineEdit(self)
            new_line.setPlaceholderText(f"Участник {i + 1}")

            list_item.setSizeHint(new_line.sizeHint())
            self.participants_inputs_list.setItemWidget(list_item, new_line)
            participants_qlines.append(new_line)

        return participants_qlines
