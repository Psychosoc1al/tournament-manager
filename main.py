from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from win32comext.shell.shell import SetCurrentProcessExplicitAppUserModelID  # install as pywin3

from controllers.main_controller import MainController
from model.main_page import MainPage
from views.main_page_view import MainPageView


def main():
    app = QApplication([])
    myappid = 'tornament.manager'
    SetCurrentProcessExplicitAppUserModelID(myappid)
    app.setWindowIcon(QIcon('icon/icon.png'))

    model = MainPage()
    window = MainPageView()
    MainController(model, window)

    app.exec()


if __name__ == '__main__':
    main()
