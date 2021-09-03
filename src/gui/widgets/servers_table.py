from qt_core import *

from .server_table_style import style as servers_table_style


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
        text_font="9pt 'Segoe UI'"
    ):
        super().__init__()

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setFrameStyle(QFrame.Plain)

        #! for tests
        js_list = [
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"12/100"},
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"23/100"},
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"12/100"},
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"12/100"},
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"12/100"},
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"12/100"},
            {"name":"[RP] Legacy of the Dragons","ping":50,"online":"12/100"},
            {"name":"Hearthfire RP","ping":100,"online":"120/1000"}
        ]

        def dictToList(dict):
            lst = list()
            for value in dict.values():
                lst.append(value)

            return lst


        servers_tuple = list()
        for i in js_list:
            servers_tuple.append(dictToList(i))

        self.setModel(ServersTableModel(self))

        self.setHorizontalHeader(HorizontalHeader(self))
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.update(servers_tuple)

        self.set_style(
            radius=radius,
            color=color,
            bg_color=bg_color,
            border_color=border_color,
            context_color=context_color,
            selection_color=selection_color,
            transparent=transparent,
            header_background=header_background,
            text_font=text_font
        )


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
        text_font
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
            header_background=header_background
        )
        self.setStyleSheet(style)


    def update(self, new_list: tuple):
        self.model().updateData(new_list)


class HorizontalHeader(QHeaderView):
    def __init__(self, parent):
        QHeaderView.__init__(self, Qt.Horizontal, parent=parent)
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
        return super().headerData(section, orientation, role=role)


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.servers[index.row()][index.column()]


    def updateData(self, new_data: tuple):
        self.beginResetModel()
        self.servers = new_data
        self.endResetModel()