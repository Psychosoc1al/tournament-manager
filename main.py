from PyQt6.QtWidgets import QApplication

from Model.MainPage import MainPage
from ViewController.MainPageView import MainPageView
from main_controller import MainController


def main():
    app = QApplication([])

    model = MainPage("data.json")
    window = MainPageView()
    _ = MainController(model, window)

    app.exec()


if __name__ == '__main__':
    main()
