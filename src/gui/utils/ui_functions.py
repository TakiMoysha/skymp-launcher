from qt_core import *
from main import *

STATE = 0

class UIFunctions():
    def removeDefaultTitleBar(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def maximizeWindow(self):
        global STATE
        status = STATE

        if (status == 0):
            self.showMaximized()
            STATE = 1
            self.ui.ui_top_label_right.button_maximize.setToolTip("Restore")
        else:
            self.showNormal()
            STATE = 0
            self.ui.ui_top_label_right.button_maximize.setToolTip("Maximize")