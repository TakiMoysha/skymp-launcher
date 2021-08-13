from qt_core import *
from main import *

STATE = 0

class UIFunctions(MainWindow):
    def remove_default_title_bar(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def maximize_window(self):
        pass