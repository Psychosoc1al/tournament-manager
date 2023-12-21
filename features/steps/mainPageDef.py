import time

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton
from behave import *  # pip install behave
from win32comext.shell.shell import SetCurrentProcessExplicitAppUserModelID
from controllers.main_controller import MainController
from model.main_page import MainPage
from views.main_page_view import MainPageView


@given('I open the program')
def step_impl(context):
    context.app = QApplication([])
    myappid = "tornament.manager"
    SetCurrentProcessExplicitAppUserModelID(myappid)
    context.app.setWindowIcon(QIcon("icon/icon.png"))

    context.model = MainPage()
    context.window = MainPageView()
    context.controller = MainController(context.model, context.window)


@then('I see add button')
def step_impl(context):
    assert context.window.findChild(QPushButton).text() == "Добавить турнир"
