from qt_core import *

from gui.ui_pages.ui_server_descriptions import UiServerDescriptions
from gui.ui_pages.ui_servers_list import UiServersList

class UiPageMain(object):
    def setupUi(self, app_page):
        if not app_page.objectName():
            app_page.setObjectName(u"page_main")
        # app_page.resize(600, 480)
        self.horizontal_layout = QHBoxLayout(app_page)
        self.horizontal_layout.setObjectName(u"horizontal_layout")

        self.server_descriptions = QWidget()
        self.server_descriptions.setObjectName(u"server_descriptions")
        self.ui_server_descriptions = UiServerDescriptions()
        self.ui_server_descriptions.setupUi(self.server_descriptions)
        size_policy_descriptions = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy_descriptions.setHorizontalStretch(1)
        self.server_descriptions.setMinimumWidth(app_page.width() * 0.6)
        self.server_descriptions.setSizePolicy(size_policy_descriptions)

        self.servers_list = QWidget()
        self.servers_list.setObjectName(u"servers_list")
        self.ui_servers_list = UiServersList()
        self.ui_servers_list.setupUi(self.servers_list)
        size_policy_servers_list = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy_servers_list.setHorizontalStretch(2)
        self.servers_list.setSizePolicy(size_policy_servers_list)

        self.horizontal_layout.addWidget(self.server_descriptions)
        self.horizontal_layout.addWidget(self.servers_list)

        QMetaObject.connectSlotsByName(app_page)


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

