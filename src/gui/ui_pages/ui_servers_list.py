from gui.widgets.button_with_icon import ButtonWithIcon
from qt_core import *

from controllers.theme_manager import ThemeManager, Colors
from gui.widgets.servers_table import ServersTable

class UiServersList(object):
    def setupUi(self, parent_page):
        if not parent_page.objectName():
            parent_page.setObjectName(u"page_home")
        parent_page.resize(680, 480)
        self.vertical_layout = QVBoxLayout(parent_page)
        self.vertical_layout.setObjectName(u"vertical_layout")

        tm = ThemeManager()

        self.small_horizontal_layout = QHBoxLayout()
        self.label = QLabel()
        self.label.setObjectName(u"label")
        self.label.setText("ServersList")
        self.label.setAlignment(Qt.AlignCenter)

        self.add_new_master_server = ButtonWithIcon(
            icon_name="plus.svg",
            icon_type="icons",
            btn_color=tm.getColor(Colors.button),
            btn_hover=tm.getColor(Colors.button_hover),
            btn_press=tm.getColor(Colors.button_press)
        )
        self.add_new_master_server.setMaximumWidth(32)
        self.add_new_master_server.setToolTip("Add new master server")

        self.refresh_btn = ButtonWithIcon(
            icon_name="refresh.svg",
            icon_type="icons",
            btn_color=tm.getColor(Colors.button),
            btn_hover=tm.getColor(Colors.button_hover),
            btn_press=tm.getColor(Colors.button_press)
        )
        self.refresh_btn.setMaximumWidth(32)
        self.refresh_btn.setToolTip("Update server list")

        self.small_horizontal_layout.addWidget(self.label)
        self.small_horizontal_layout.addWidget(self.add_new_master_server)
        self.small_horizontal_layout.addWidget(self.refresh_btn)

        self.table = ServersTable(
            radius=8,
            color=tm.getColor(Colors.text),
            bg_color=tm.getColor(Colors.background),
            border_color=tm.getColor(Colors.button),
            context_color=tm.getColor(Colors.debug),
            selection_color=tm.getColor(Colors.button),
            header_background=tm.getColor(Colors.background_dark)
        )

        self.vertical_layout.addLayout(self.small_horizontal_layout)
        self.vertical_layout.addWidget(self.table)

        self.handel_buttons()
        QMetaObject.connectSlotsByName(parent_page)

    def handel_buttons(self):
        servers_tuple: tuple = tuple()
        self.refresh_btn.clicked.connect(
            lambda: self.table.update(servers_tuple)
        )