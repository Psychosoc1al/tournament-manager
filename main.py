from PyQt6.QtWidgets import QApplication

from Model.MainPage import MainPage
from ViewController.MainPageView import MainPageView

app = QApplication([])

model = MainPage("data.json")
window = MainPageView(model)
window.show()

app.exec()

