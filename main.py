from PyQt6.QtWidgets import QApplication

from Model.MainPage import MainPage
from ViewController.MainPageView import MainPageView


def main():
    app = QApplication([])

    model = MainPage("data.json")
    window = MainPageView(model)
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
