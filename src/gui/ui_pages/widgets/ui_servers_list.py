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
        self.table_widget.setColumnCount(4)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        for i in range(2):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Test")))
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("Test")))
            self.table_widget.setItem(row_number, 2, QTableWidgetItem(str(23+row_number)))
            self.table_widget.setItem(row_number, 3, QTableWidgetItem(str(1234)))


        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.table_widget)

        QMetaObject.connectSlotsByName(parent_page)
