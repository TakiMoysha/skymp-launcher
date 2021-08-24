from qt_core import *

from .server_table_style import style as servers_table_style


class ServersTable(QTableView):
    def __init__(
        self,
        radius = 8,
        color = "#FFF",
        bg_color = "#000",
        border_color = "#000",
        context_color = "#0F0F0F",
        selection_color = "#000"
    ):
        super().__init__()

        horizontalHeader = HorizontalHeader(self)
        self.setHorizontalHeader(horizontalHeader)

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().hide()
        self.setSortingEnabled(True)

        # Enchanting format for view
        js_list = [
            {"ip":"194.61.3.51","port":25520,"name":"[RP] Legacy of the Dragons","maxPlayers":50,"online":0},
            {"ip":"194.61.3.51","port":25590,"name":"Hearthfire RP","maxPlayers":100,"online":3}
            ]

        def dictToList(dict):
            lst = list()
            element = ("name", "ip", "port", "maxPlayers", "online")
            for key in element:
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

        servers_table_model = ServersItemModel(self, servers_tuple)
        self.setModel(servers_table_model)

        self.set_style(
            radius = radius,
            color = color,
            bg_color = bg_color,
            border_color = border_color,
            context_color = context_color,
            selection_color = selection_color
        )


    def set_style(
        self,
        radius,
        color,
        bg_color,
        border_color,
        context_color,
        selection_color
    ):
        style = servers_table_style.format(
            border_color = border_color,
            radius = radius,
            bg_color = bg_color,
            color = color,
            context_color = context_color,
            selection_color = selection_color
        )
        self.setStyleSheet(style)



class HorizontalHeader(QHeaderView):
    def __init__(self, parent):
        QHeaderView.__init__(self, Qt.Horizontal, parent=parent)
        self.setSectionResizeMode(QHeaderView.Stretch)



class ServersItemModel(QAbstractTableModel):
    def __init__(self, parent, servers_list, *args):
        super().__init__(parent)
        self.servers = servers_list


    def rowCount(self, parent):
        return len(self.servers)


    def columnCount(self, parent):
        return len(self.servers[0])


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.servers[index.row()][index.column()]