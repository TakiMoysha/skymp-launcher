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

        self.label = QLabel()
        self.label.setObjectName(u"label")
        self.label.setText("ServersList")
        self.label.setAlignment(Qt.AlignCenter)
        tm = ThemeManager()
        self.table_widget = ServersTable(
            radius = 8,
            color = tm.getColor(Colors.text),
            bg_color = tm.getColor(Colors.background),
            border_color = tm.getColor(Colors.button),
            context_color = tm.getColor(Colors.debug),
            selection_color = tm.getColor(Colors.button)
        )

        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.table_widget)

        QMetaObject.connectSlotsByName(parent_page)
