from qt_core import *

from gui.ui_sys_buttons import Ui_SysButtons
from gui.utils.ui_functions import UIFunctions

class Ui_TitleBar(QWidget):

    def setupUi(self, parent: QWidget):
        self.title_bar_layout = QHBoxLayout(parent)
        self.title_bar_layout.setContentsMargins(10, 0, 4, 0)

        self.label = QLabel("SkyMP Launcher")

        self.spacer = QSpacerItem(
            10,
            20,
            QSizePolicy.MinimumExpanding,
            QSizePolicy.Minimum
        )

        self.sys_buttons = QWidget()
        self.ui_sys_buttons = Ui_SysButtons()
        self.ui_sys_buttons.setupUi(self.sys_buttons)

        self.title_bar_layout.addWidget(self.label)
        self.title_bar_layout.addItem(self.spacer)
        self.title_bar_layout.addWidget(self.sys_buttons)

        QMetaObject.connectSlotsByName(parent)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        super().mouseDoubleClickEvent(event)
        print("asdf")


    def moveWindow(self, mouse_pos):
        if mouse_pos.y() <= self.height():
                self.startSystemMove()

    # def moveOrResize(self, window, pos, width, height):
    #     edges = UIFunctions._getEdges(self, pos, width, height)
    #     if edges:
    #         if window.windowState() == Qt.WindowNoState:
    #             window.startSystemResize(edges)
    #     else:
    #         if pos.y() <= self.ui.title_bar.height():
    #             window.startSystemMove()

