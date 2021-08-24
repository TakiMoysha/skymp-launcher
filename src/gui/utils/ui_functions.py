from qt_core import *
from main import *

class UIFunctions():
    def removeDefaultTitleBar(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setMouseTracking(True)


    def maximizeWindow(self: QMainWindow, called_button: QPushButton):
        if (self.windowState() == Qt.WindowNoState):
            called_button.setToolTip("Restore")
            self.setWindowState(Qt.WindowMaximized)
        else:
            called_button.setToolTip("Maximize")
            self.setWindowState(Qt.WindowNoState)