import os

from qt_core import *

from gui.pages.widgets.title_bar_button import TitleBarButton

class SysButtons(QWidget):
    def setupUi(self, parent):
        if not parent.objectName():
            parent.setObjectName(u"parent")

        self.title_bar_sys_buttons_frame = QWidget()
        self.title_bar_sys_buttons_frame.setObjectName(u"title_bar_sys_buttons")
        self.title_bar_sys_buttons_frame.setMinimumWidth(70)
        self.title_bar_sys_buttons_frame.setMaximumWidth(80)
        self.horizontalLayout = QHBoxLayout(self.title_bar_sys_buttons_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayoutButtons")


        # Minimize
        self.button_minimize = TitleBarButton(
            background_color = "rgb(114, 255, 0);",
            hover_background_color = "rgba(114, 255, 0, 150)"
        )
        self.button_minimize.setObjectName(u"button_minimize")
        self.horizontalLayout.addWidget(self.button_minimize)

        # Maximize
        self.button_maximize = TitleBarButton(
            background_color = "rgb(255, 187, 0);",
            hover_background_color = "rgba(255, 187, 0, 150)"
        )
        self.button_maximize.setObjectName(u"button_maximize")
        self.horizontalLayout.addWidget(self.button_maximize)

        # Exit
        self.button_exit = TitleBarButton(
            background_color = "rgb(255, 0, 0);",
            hover_background_color = "rgba(255, 0, 0, 150)"
        )
        self.button_exit.setObjectName(u"button_exit")
        self.horizontalLayout.addWidget(self.button_exit)


        parent.addWidget(self.title_bar_sys_buttons_frame)

        self.retranslateUi(parent)


    def retranslateUi(self, parent):
        parent.setWindowTitle(QCoreApplication.translate("Frame", u"SysButons", None))