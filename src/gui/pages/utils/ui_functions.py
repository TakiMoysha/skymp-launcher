from qt_core import *
from main import *

STATE = 0

class UIFunctions(MainWindow):
    def removeDefaultTitleBar(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def maximizeWindow(self):
        global STATE
        status = STATE
