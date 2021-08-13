from qt_core import *
from main import *

STATE = 0

class UIFunctions(MainWindow):
    def removeDefaultTitleBar(self):
        self.setWindowFlog(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def maximize_window(self):
        pass
