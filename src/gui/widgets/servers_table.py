from qt_core import *

from .server_table_style import style as servers_table_style


class ServersTable(QTableView):
    COLUMNS_NAME = ("name", "ip", "port", "maxPlayers", "online")
    def __init__(
        self,
        radius = 8,
        color = "#FFF",
        bg_color = "#000",
        border_color = "#000",
        context_color = "#0F0F0F",
        selection_color = "#000",
        transparent = "#00000000"
    ):
        super().__init__()

        horizontalHeader = HorizontalHeader(self)
        self.setHorizontalHeader(horizontalHeader)

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setFrameStyle(QFrame.Plain)

        # Enchanting format for view
        js_list = [
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25590,"name":"Hearthfire RP","maxPlayers":100,"online":3}
        ]

        def dictToList(dict):
            lst = list()
            for key in self.COLUMNS_NAME:
                try:
                    value = dict.get(key)
                    lst.append(value)
                except KeyError:
                    pass
                except Exception as err:
                    print(err)

            return lst

        servers_tuple = list()
        for i in js_list:
            servers_tuple.append(dictToList(i))

        self.setModel(ServersTableModel(self, servers_tuple))

        self.set_style(
            radius = radius,
            color = color,
            bg_color = bg_color,
            border_color = border_color,
            context_color = context_color,
            selection_color = selection_color,
            transparent = transparent
        )


    def set_style(
        self,
        radius,
        color,
        bg_color,
        border_color,
        context_color,
        selection_color,
        transparent
    ):
        style = servers_table_style.format(
            border_color = border_color,
            radius = radius,
            bg_color = bg_color,
            color = color,
            context_color = context_color,
            selection_color = selection_color,
            transparent = transparent
        )
        self.setStyleSheet(style)

    def update(self, new_list: tuple):
        self.model().beginResetModel()
        self.model().updateData(new_list)
        self.model().endResetModel()



class HorizontalHeader(QHeaderView):
    def __init__(self, parent):
        QHeaderView.__init__(self, Qt.Horizontal, parent=parent)
        self.setSectionResizeMode(QHeaderView.Stretch)


class ServersTableModel(QAbstractTableModel):
    servers = tuple()
    COLUMNS_NAME = {
        "name": "Name",
        "ip": "Address",
        "port": "Port",
        "maxPlayers": "Players",
        "online": "Online"
    }

    def __init__(self, parent, *args):
        super().__init__(parent)
        self.servers = args[0]


    def rowCount(self, parent):
        return len(self.servers)


    def columnCount(self, parent):
        """sets the number of columns"""
        return len(self.COLUMNS_NAME)


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.servers[index.row()][index.column()]


    def updateData(self, new_data: tuple):
        self.servers = new_data