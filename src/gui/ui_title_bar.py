from qt_core import *

from gui.ui_sys_buttons import UiSysButtons

class UiTitleBar(QWidget):

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
        self.ui_sys_buttons = UiSysButtons()
        self.ui_sys_buttons.setupUi(self.sys_buttons)

        self.title_bar_layout.addWidget(self.label)
        self.title_bar_layout.addItem(self.spacer)
        self.title_bar_layout.addWidget(self.sys_buttons)

        QMetaObject.connectSlotsByName(parent)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        super().mouseDoubleClickEvent(event)


    def moveWindow(self, mouse_pos):
        if mouse_pos.y() <= self.height():
                self.startSystemMove()
