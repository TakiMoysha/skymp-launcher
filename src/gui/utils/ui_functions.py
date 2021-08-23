from qt_core import *
from main import *

class UIFunctions():
    def removeDefaultTitleBar(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def maximizeWindow(self: QMainWindow):
        if (self.windowState() == Qt.WindowNoState):
            self.ui.ui_top_label_right.button_maximize.setToolTip("Restore")
            self.setWindowState(Qt.WindowMaximized)
        else:
            self.ui.ui_top_label_right.button_maximize.setToolTip("Maximize")
            self.setWindowState(Qt.WindowNoState)