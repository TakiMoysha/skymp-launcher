from controllers.theme_manager import Colors, ThemeManager
from gui.widgets.server_tab_widget import ServerTabWidget
from qt_core import *

class UiServerDescriptions(object):
    def setupUi(self, parent_page):
        if not parent_page.objectName():
            parent_page.setObjectName(u"server_descri")

        self.gridLayout = QGridLayout(parent_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.server_icon = QLabel()
        self.server_icon.setObjectName(u"server_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_icon.sizePolicy().hasHeightForWidth())
        self.server_icon.setSizePolicy(sizePolicy)
        self.server_icon.setMinimumSize(QSize(64, 64))

        self.gridLayout.addWidget(self.server_icon, 0, 0, 2, 1)

        self.server_name = QLabel()
        self.server_name.setObjectName(u"server_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.server_name.sizePolicy().hasHeightForWidth())
        self.server_name.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.server_name, 0, 1, 1, 1)

        self.server_address = QLabel()
        self.server_address.setObjectName(u"server_address")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.server_address.sizePolicy().hasHeightForWidth())
        self.server_address.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.server_address, 1, 1, 1, 1)

        self.tabWidget = ServerTabWidget()
        self.tabWidget.setObjectName(u"tabWidget")

        self.Description = QWidget()
        self.Description.setObjectName(u"Description")
        self.verticalLayout = QVBoxLayout(self.Description)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.Description)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.tabWidget.addTab(self.Description, "")
        self.Mods = QWidget()
        self.Mods.setObjectName(u"Mods")
        self.horizontalLayout = QHBoxLayout(self.Mods)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.server_mods_list = QListView(self.Mods)
        self.server_mods_list.setObjectName(u"server_mods_list")

        self.horizontalLayout.addWidget(self.server_mods_list)

        self.tabWidget.addTab(self.Mods, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.main_button = QPushButton()
        self.main_button.setObjectName(u"main_button")
        self.main_button.setStyleSheet(u"QPushButton {{\n"
"                color: red;\n"
"                background-color: blue;\n"
"                padding-left: 20px;\n"
"	            padding-right: 20px;\n"
"                text-align: center;\n"
"                border: none;\n"
"            }}\n"
"            ButtonWithIcon:hover {{\n"
"                background-color: blue;\n"
"            }}")

        self.gridLayout.addWidget(self.main_button, 3, 0, 1, 2)


        self.retranslateUi(parent_page)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(parent_page)
    # setupUi

    def retranslateUi(self, parent_page):
        parent_page.setWindowTitle(QCoreApplication.translate("parent_page", u"parent_page", None))
        self.server_icon.setText(QCoreApplication.translate("parent_page", u"TextLabel", None))
        self.server_name.setText(QCoreApplication.translate("parent_page", u"TextLabel", None))
        self.server_address.setText(QCoreApplication.translate("parent_page", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Description), QCoreApplication.translate("parent_page", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Mods), QCoreApplication.translate("parent_page", u"Tab 2", None))
        self.main_button.setText(QCoreApplication.translate("parent_page", u"Play", None))
    # retranslateUi
