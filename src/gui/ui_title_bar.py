from qt_core import *

from gui.ui_sys_buttons import Ui_SysButtons

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

        # self.top_label_right = QHBoxLayout(self.top_bar)
        self.sys_buttons = QWidget()
        self.ui_sys_buttons = Ui_SysButtons()
        self.ui_sys_buttons.setupUi(self.sys_buttons)

        self.title_bar_layout.addWidget(self.label)
        self.title_bar_layout.addItem(self.spacer)
        self.title_bar_layout.addWidget(self.sys_buttons)

        QMetaObject.connectSlotsByName(parent)