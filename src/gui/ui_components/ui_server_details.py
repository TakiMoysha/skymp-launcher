from qt_core import *

from auth_window import AuthWindow

from gui.widgets.server_tab_widget import ServerDetailsTabWidget

from controllers.server_details import filesInstalled
from controllers.theme_manager import Colors, ThemeManager

class UiServerDetails(object):
    def setupUi(self, parent_page):
        if not parent_page.objectName():
            parent_page.setObjectName(u"server_details")

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

        self.tabWidget = ServerDetailsTabWidget()
        self.tabWidget.setObjectName(u"tabWidget")

        self.description = QWidget()
        self.description.setObjectName(u"description")
        self.verticalLayout = QVBoxLayout(self.description)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.description)
        self.textBrowser.setObjectName(u"textBrowser")
        self.description.setStyleSheet(f"""
            QTextBrowser {{
                background-color: blue;
            }}
        """)

        self.verticalLayout.addWidget(self.textBrowser)

        self.mods = QWidget()
        self.mods.setObjectName(u"mods")
        self.modsTabHLayout = QHBoxLayout(self.mods)
        self.modsTabHLayout.setObjectName(u"modsTabHLayout")
        self.server_mods_list = QListWidget(self.mods)
        self.server_mods_list.setObjectName(u"server_mods_list")

        self.modsTabHLayout.addWidget(self.server_mods_list)

        self.dlls = QWidget()
        self.dlls.setObjectName(u'dlls')
        self.dllsTabHLayout = QHBoxLayout(self.dlls)
        self.dllsTabHLayout.setObjectName(u"dllsTabHLayout")
        self.server_dlls_list = QListWidget(self.dlls)
        self.server_dlls_list.setObjectName(u"server_dlls_list")
        self.server_dlls_list.addItems(["ui.dll", "client.dll"])

        self.dllsTabHLayout.addWidget(self.server_dlls_list)

        self.tabWidget.addTab(self.description, "")
        self.tabWidget.addTab(self.mods, "")
        self.tabWidget.addTab(self.dlls, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 2)

        self.play_button = QPushButton()
        self.play_button.setObjectName(u"main_button")
        self.play_button.setStyleSheet(u"QPushButton {{\n"
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

        self.gridLayout.addWidget(self.play_button, 3, 0, 1, 2)

        self.setupButtons()

        self.retranslateUi(parent_page)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(parent_page)
    # setupUi

    def retranslateUi(self, parent_page):
        parent_page.setWindowTitle(QCoreApplication.translate("parent_page", u"parent_page", None))
        self.server_icon.setText(QCoreApplication.translate("parent_page", u"Icon", None))
        self.server_name.setText(QCoreApplication.translate("parent_page", u"ServerName", None))
        self.server_address.setText(QCoreApplication.translate("parent_page", u"ServerAddress", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.description), QCoreApplication.translate("parent_page", u"Details", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mods), QCoreApplication.translate("parent_page", u"Mods", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dlls), QCoreApplication.translate("parent_page", u"Dlls", None))
        self.play_button.setText(QCoreApplication.translate("parent_page", u"Play", None))
    # retranslateUi


    def setupButtons(self):
        self.play_button.clicked.connect(self.playClick)


    def playClick(self):
        if not self._isUserAuth():
            auth_window = AuthWindow()
            auth_window.setWindowModality(Qt.ApplicationModal)
            auth_window.show()
        elif not filesInstalled():
            pass
        else:
            pass


    def _isUserAuth(self):
        return False

    def updateDetails(self, icon_url, name, address, descriptions, mods, dlls):
        # self.server_icon.setPixmap(pixmap)
        # qpixmap = QPixmap(icon_url)
        # QImage.loadFromData()
        self.server_name.setText(name)
        self.server_address.setText(address)
        self.textBrowser.setText(descriptions)
        self.server_mods_list.addItems(mods)
        self.server_dlls_list.addItems(dlls)

