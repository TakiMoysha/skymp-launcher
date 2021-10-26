from qt_core import *

from .servers_table_style import style as servers_table_style

class ServersTable(QTableView):
    def __init__(
        self,
        radius=8,
        color="#FFF",
        bg_color="#000",
        border_color="#000",
        context_color="#0F0F0F",
        selection_color="#000",
        transparent="#00000000",
        header_background="#000000",
        item_hover_color="#000000ff",
        text_font="9pt 'Segoe UI'"
    ):
        super().__init__()

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().hide()

        self.serversTableModel = ServersTableModel(self)

        self.sortProxyModel = QSortFilterProxyModel()
        self.sortProxyModel.setSourceModel(self.serversTableModel)

        self.setModel(self.sortProxyModel)
        self.setSortingEnabled(True)

        self.setHorizontalHeader(HorizontalHeader(self))
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.setShowGrid(False)

        self.set_style(
            color=color,
            radius=radius,
            bg_color=bg_color,
            text_font=text_font,
            transparent=transparent,
            border_color=border_color,
            context_color=context_color,
            selection_color=selection_color,
            item_hover_color=item_hover_color,
            header_background=header_background,
        )


    def selectionChanged(self, selected: QItemSelection, deselected: QItemSelection) -> None:
        return super().selectionChanged(selected, deselected)

    def set_style(
        self,
        radius,
        color,
        bg_color,
        border_color,
        context_color,
        selection_color,
        transparent,
        header_background,
        text_font,
        item_hover_color
    ):
        style = servers_table_style.format(
            color=color,
            radius=radius,
            bg_color=bg_color,
            text_font=text_font,
            transparent=transparent,
            border_color=border_color,
            context_color=context_color,
            selection_color=selection_color,
            item_hover_color=item_hover_color,
            header_background=header_background,
        )
        self.setStyleSheet(style)

    def updateGameServersList(self, game_servers_list):
        self.serversTableModel.updateData(game_servers_list)


class HorizontalHeader(QHeaderView):
    def __init__(self, parent):
        QHeaderView.__init__(self, Qt.Horizontal, parent=parent)
        self.setSectionsClickable(True)
        self.setSectionResizeMode(QHeaderView.Stretch)


class ServersTableModel(QAbstractTableModel):
    servers = tuple()
    COLUMNS_ID = ("Name", "Ping", "Online")

    def __init__(self, parent, *args):
        super().__init__(parent)

    def rowCount(self, parent):
        """sets the number of rows"""
        return len(self.servers)


    def columnCount(self, parent):
        """sets the number of columns"""
        return len(self.COLUMNS_ID)


    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.COLUMNS_ID[section]
        # table.horizontalHeaderItem(0).setIcon("qrc://path/to/icon.png")
        return super().headerData(section, orientation, role=role)


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.servers[index.row()][index.column()]


    def updateData(self, new_data: tuple):
        self.beginResetModel()
        self.servers = new_data
        self.endResetModel()