import os

from qt_core import *

from gui.widgets.title_bar_button import TitleBarButton

class UiSysButtons(QWidget):
    def setupUi(self, parent: QWidget):
        if not parent.objectName():
            parent.setObjectName(u"horizontalLayoutButtons")

        # Minimize
        self.horizontal_layout = QHBoxLayout(parent)

        self.button_minimize = TitleBarButton(
            background_color = "rgb(114, 255, 0);",
            hover_background_color = "rgba(114, 255, 0, 150)"
        )
        self.button_minimize.setObjectName(u"button_minimize")
        self.horizontal_layout.addWidget(self.button_minimize)

        # Maximize
        self.button_maximize = TitleBarButton(
            background_color = "rgb(255, 187, 0);",
            hover_background_color = "rgba(255, 187, 0, 150)"
        )
        self.button_maximize.setObjectName(u"button_maximize")
        self.horizontal_layout.addWidget(self.button_maximize)

        # Exit
        self.button_exit = TitleBarButton(
            background_color = "rgb(255, 0, 0);",
            hover_background_color = "rgba(255, 0, 0, 150)"
        )
        self.button_exit.setObjectName(u"button_exit")
        self.horizontal_layout.addWidget(self.button_exit)

        QMetaObject.connectSlotsByName(parent)

        self.retranslateUi(parent)


    def retranslateUi(self, parent):
        self.button_minimize.setToolTip(u"Minimize")
        self.button_maximize.setToolTip(u"Maximize")
        self.button_exit.setToolTip(u"Close app")