# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages_settingstzPSND.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from controllers.theme_manager import ThemeManager, Colors
from gui.widgets.button_with_icon import ButtonWithIcon

class UiPageSettings(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"PageSettings")
        Frame.resize(640, 388)
        Frame.setStyleSheet("padding: 4px")

        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        tm = ThemeManager()

        self.pathToSkyrimFolder = QLineEdit(Frame)
        self.pathToSkyrimFolder.setObjectName(u"pathToSkyrimFolder")
        self.pathToSkyrimFolder.setMinimumSize(QSize(300, 24))
        self.pathToSkyrimFolder.setReadOnly(True)
        self.pathToSkyrimFolder.setStyleSheet(f"""
            QLineEdit {{
                border-style: outset;
                border-width: 2px;
                border-radius: 8px;
                border-color: { tm.getColor(Colors.button) };
                font: 12px;
                padding: 4px;
            }}
        """)

        self.gridLayout.addWidget(self.pathToSkyrimFolder, 1, 0, 1, 1)

        self.openSkyrimFolder = ButtonWithIcon(
            text = "Open",
            text_color = tm.getColor(Colors.text_light),
            icon_type = "images",
            icon_name = "folder.png",
            btn_color = tm.getColor(Colors.button),
            btn_hover = tm.getColor(Colors.button_hover),
            btn_press = tm.getColor(Colors.button_press)
        )
        self.pathToSkyrimFolder.setObjectName(u"openSkyrimFolder")

        self.gridLayout.addWidget(self.openSkyrimFolder, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("PageSettings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("PageSettings", u"Path to Skyrim:", None))
        self.openSkyrimFolder.setText(QCoreApplication.translate("PageSettings", u"Open", None))
    # retranslateUi

