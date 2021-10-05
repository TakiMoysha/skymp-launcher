# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesiiNfdJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from gui.ui_components.ui_page_settings import UiPageSettings
from gui.ui_components.ui_page_main import UiPageMain

class UiApplicationPages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")

        application_pages.resize(640, 480)

        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.ui_page_home = UiPageMain()
        self.ui_page_home.setupUi(self.page_home)

        application_pages.addWidget(self.page_home)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)

        self.page_settings = QFrame()
        self.ui_page_settings = UiPageSettings()
        self.ui_page_settings.setupUi(self.page_settings)

        application_pages.addWidget(self.page_settings)

        self.retranslateUi(application_pages)

        QMetaObject.connectSlotsByName(application_pages)


    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(
            QCoreApplication.translate(
                "application_pages", u"StackedWidget", None
            )
        )
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Label 2", None))
        # self.page_settings.retranslateUi()
        # self.settings.setText(QCoreApplication.translate("application_pages", u"Label 3", None))

