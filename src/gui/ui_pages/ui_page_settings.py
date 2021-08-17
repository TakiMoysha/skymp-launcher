# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages_settingstzPSND.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from gui.widgets.button_with_icon import ButtonWithIcon

class UiPageSettings(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"PageSettings")
        Frame.resize(640, 388)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pathToSkyrimFolder = QLineEdit(Frame)
        self.pathToSkyrimFolder.setObjectName(u"pathToSkyrimFolder")
        self.pathToSkyrimFolder.setMinimumSize(QSize(300, 24))
        self.pathToSkyrimFolder.setReadOnly(True)

        self.gridLayout.addWidget(self.pathToSkyrimFolder, 1, 0, 1, 1)

        self.openSkyrimFolder = ButtonWithIcon(
            text = "Open",
            text_color = "rgb(195, 204, 223);",
            icon_type = "images",
            icon_name = "folder.png",
        )
        self.pathToSkyrimFolder.setObjectName(u"openSkyrimFolder")

        self.gridLayout.addWidget(self.openSkyrimFolder, 1, 1, 1, 1)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("PageSettings", u"Settings", None))
        self.label.setText(QCoreApplication.translate("PageSettings", u"Path to Skyrim:", None))
        self.openSkyrimFolder.setText(QCoreApplication.translate("PageSettings", u"Open", None))
    # retranslateUi

