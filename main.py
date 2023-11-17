from PyQt6.QtWidgets import QApplication

from main_page import MainPage
from main_page_view import MainPageView
from main_controller import MainController


def main():
    app = QApplication([])

    model = MainPage()
    window = MainPageView()
    MainController(model, window)

    app.exec()


if __name__ == '__main__':
    main()
