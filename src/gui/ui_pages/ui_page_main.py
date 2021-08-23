# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesiiNfdJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

from gui.ui_pages.widgets.ui_server_descriptions import UiServerDescriptions
from gui.ui_pages.widgets.ui_servers_list import UiServersList

class UiPageMain(object):
    def setupUi(self, app_page):
        if not app_page.objectName():
            app_page.setObjectName(u"page_main")
        app_page.resize(600, 480)
        self.horizontal_layout = QHBoxLayout(app_page)
        self.horizontal_layout.setObjectName(u"horizontal_layout")

        self.server_descriptions = QWidget()
        self.server_descriptions.setObjectName(u"server_descriptions")
        self.ui_server_descriptions = UiServerDescriptions()
        self.ui_server_descriptions.setupUi(self.server_descriptions)

        self.servers_list = QWidget()
        self.servers_list.setObjectName(u"servers_list")
        self.ui_servers_list = UiServersList()
        self.ui_servers_list.setupUi(self.servers_list)


        self.horizontal_layout.addWidget(self.server_descriptions)
        self.horizontal_layout.addWidget(self.servers_list)

        QMetaObject.connectSlotsByName(app_page)



    #     self.page_home = QWidget()
    #     self.page_home.setObjectName(u"page_home")
    #     self.verticalLayout = QVBoxLayout(self.page_home)
    #     self.verticalLayout.setObjectName(u"verticalLayout")

    #     self.home = QLabel(self.page_home)
    #     self.home.setObjectName(u"home")
    #     self.home.setAlignment(Qt.AlignCenter)

    #     self.verticalLayout.addWidget(self.home)

    #     application_pages.addWidget(self.page_home)

    #     self.page_2 = QWidget()
    #     self.page_2.setObjectName(u"page_2")
    #     self.verticalLayout_2 = QVBoxLayout(self.page_2)
    #     self.verticalLayout_2.setObjectName(u"verticalLayout_2")
    #     self.label_2 = QLabel(self.page_2)
    #     self.label_2.setObjectName(u"label_2")
    #     self.label_2.setAlignment(Qt.AlignCenter)

    #     self.verticalLayout_2.addWidget(self.label_2)

    #     application_pages.addWidget(self.page_2)

    #     self.page_settings = QFrame()
    #     self.ui_page_settings = UiPageSettings()
    #     self.ui_page_settings.setupUi(self.page_settings)

    #     application_pages.addWidget(self.page_settings)

    #     self.retranslateUi(application_pages)

    #     QMetaObject.connectSlotsByName(application_pages)


    # def retranslateUi(self, application_pages):
    #     application_pages.setWindowTitle(
    #         QCoreApplication.translate(
    #             "application_pages", u"StackedWidget", None
    #         )
    #     )
    #     self.home.setText(QCoreApplication.translate("application_pages", u"Label 1", None))
    #     self.label_2.setText(QCoreApplication.translate("application_pages", u"Label 2", None))
    #     # self.page_settings.retranslateUi()
    #     # self.settings.setText(QCoreApplication.translate("application_pages", u"Label 3", None))

