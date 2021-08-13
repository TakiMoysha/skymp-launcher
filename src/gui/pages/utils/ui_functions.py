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

        if (status == 0):
            self.showMaximized()

            STATE = 1

            # self.ui.drop_shadow_frame.setContentsMargins(0, 0, 0, 0)
            # self.ui.drop_shadow_frame.setStyleSheet(
            #     ""
            # )
            self.ui.ui_top_label_right.button_maximize.setToolTip("Restore")
        else:
            STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            # self.ui.drop_shadow_frame.setContentsMargins(10, 10, 10, 10)
            # self.ui.drop_shadow_frame.setStyleSheet(
            #     ""
            # )
            self.ui.ui_top_label_right.button_maximize.setToolTip("Maximize")