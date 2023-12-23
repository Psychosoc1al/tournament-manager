from os.path import abspath, dirname

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from win32comext.shell.shell import (
    SetCurrentProcessExplicitAppUserModelID,
)  # install as pywin32

from controllers.main_controller import MainController
from model.main_page import MainPage
from views.main_page_view import MainPageView


def main():
    app = QApplication([])
    myappid = "tornament.manager"
    SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QIcon(dirname(abspath(__file__)) + "/icon/icon.ico"))

    model = MainPage()
    window = MainPageView()
    MainController(model, window)

    # splash closing for a .exe dist
    try:
        import pyi_splash

        pyi_splash.close()
    except ModuleNotFoundError:
        ...

    app.exec()


if __name__ == "__main__":
    main()
