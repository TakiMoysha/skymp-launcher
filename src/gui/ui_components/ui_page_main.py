from qt_core import *

from gui.ui_components.ui_server_details import UiServerDetails
from gui.ui_components.ui_servers_list import UiServersList

from controllers.server_details import get_details_by_server_name


class UiPageMain(object):
    def setupUi(self, app_page):
        if not app_page.objectName():
            app_page.setObjectName(u"page_main")
        # app_page.resize(600, 480)
        self.horizontal_layout = QHBoxLayout(app_page)
        self.horizontal_layout.setObjectName(u"horizontal_layout")

        self.server_descriptions = QWidget()
        self.server_descriptions.setObjectName(u"server_descriptions")
        self.ui_server_descriptions = UiServerDetails()
        self.ui_server_descriptions.setupUi(self.server_descriptions)
        size_policy_descriptions = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy_descriptions.setHorizontalStretch(1)
        self.server_descriptions.setMinimumWidth(app_page.width() * 0.6)
        self.server_descriptions.setSizePolicy(size_policy_descriptions)
        self.server_descriptions.setFixedWidth(0)

        self.servers_list = QWidget()
        self.servers_list.setObjectName(u"servers_list")
        self.ui_servers_list = UiServersList()
        self.ui_servers_list.setupUi(self.servers_list)
        size_policy_servers_list = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy_servers_list.setHorizontalStretch(2)
        self.servers_list.setSizePolicy(size_policy_servers_list)

        self.horizontal_layout.addWidget(self.server_descriptions)
        self.horizontal_layout.addWidget(self.servers_list)

        self.setupButtons()

        QMetaObject.connectSlotsByName(app_page)


    def setupButtons(self):
        self.ui_servers_list.table.selectionModel().selectionChanged.connect(
            self.selectGameServer
        )


    def selectGameServer(self, selected: QItemSelection, deselected: QItemSelection):
        def updateGameServerDetails(selected: QItemSelection, deselected: QItemSelection):
            name_game_server = selected.indexes()[0].data()
            server_details = get_details_by_server_name(name_game_server)
            server_logo = server_details.get('logo')
            server_name = server_details.get('name')
            server_address = server_details.get('address')
            server_desc = server_details.get('desc')
            server_mods = server_details.get('mods')

        updateGameServerDetails(selected, deselected)
        maximum_width = 600
        print(self.server_descriptions.maximumWidth())
        if (self.server_descriptions.maximumWidth() != maximum_width):
            self.animation = QPropertyAnimation(self.server_descriptions, b"maximumWidth")
            self.animation.setStartValue(0)
            self.animation.setEndValue(maximum_width)
            self.animation.setDuration(200)
            self.animation.setEasingCurve(QEasingCurve.Linear)
            self.animation.start()



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

