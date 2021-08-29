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

        self.small_horizontal_layout = QHBoxLayout()
        self.label = QLabel()
        self.label.setObjectName(u"label")
        self.label.setText("ServersList")
        self.label.setAlignment(Qt.AlignCenter)
        self.refresh_btn = ButtonWithIcon(
            icon_name="refresh.svg",
            icon_type="icons"
        )
        self.refresh_btn.setMaximumWidth(32)

        self.small_horizontal_layout.addWidget(self.label)
        self.small_horizontal_layout.addWidget(self.refresh_btn)

        tm = ThemeManager()

        self.table = ServersTable(
            radius = 8,
            color = tm.getColor(Colors.text),
            bg_color = tm.getColor(Colors.background),
            border_color = tm.getColor(Colors.button),
            context_color = tm.getColor(Colors.debug),
            selection_color = tm.getColor(Colors.button)
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